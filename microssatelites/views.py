from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NameForm, LoginForm, UploadFileForm, DownloadForm
from .tables import PersonTable
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from zipfile import ZipFile
from .models import User, Project, ProjectData, DataStatistic
import pandas as pd
import os, re
import sys
import time

# Celery Task
from .tasks import ProcessDownload

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # CRIAR O USER NO DB COM OS DADOS DO FORMULÁRIO
            user = User.objects.create(name=request.POST['name'], email=request.POST['email'])
            user.save()
            # ARMAZENA AS INFORMAÇÕES NA SESSÃO
            request.session['name'] = request.POST['name']  
            request.session['email'] = request.POST['email']
            # CRIAR O PROJETO NO DB
            project = Project.objects.create(user=user)
            project.save()
            request.session['project'] = project.pk
            request.session.save()

            # CRIAR PASTA DO PROJETO USER[PK]_PROJECT[PK]
            dirproject = f'USER{user.pk}_PROJECT{project.pk}'
            os.system(f'mkdir {dirproject}')

            # CRIAR SUBPASTAS DO PROJETO
            subdirectories = ['UserOutputs', 'UserData', 'UserData/FASTA', 'UserData/GBKs']
            for subdir in subdirectories:
                os.system(f'mkdir {dirproject}/{subdir}')

            # TRANSFERIR OS ARQUIVOS PARAS AS SUBPASTAS
            # |---FASTAs
            request.session['statusProcessament'] = "Uploading files..."
            request.session.save()
            listGBK = request.FILES.getlist('fileGBK')
            
            if len(listGBK) == 0:
                useGKB = False
            else:
                useGKB = True
                # |---GBKs
                for f in request.FILES.getlist('fileGBK'):
                    handle_uploaded_file(request, f, f'{dirproject}/{subdirectories[3]}')

            for f in request.FILES.getlist('fileFasta'):
                handle_uploaded_file(request, f, f'{dirproject}/{subdirectories[2]}')
                if useGKB == False:
                    os.system(f'{dirproject}/{subdirectories[3]}')
                    name = str(f).split(".f")
                    os.system(f'cp defaultgbk.gb {dirproject}/{subdirectories[3]}/{name[0]}.gb')

            
            # request.session['totalUpload'] = True
            request.session.save()
            start_time = time.time()
            
            print('================================================================')
            print('=                 Convertendo Arquivos GBKtoPTT                =')
            print('================================================================')
            request.session['statusProcessament'] = "Converting GBK to PTT..."
            request.session.save()

            os.system(f'python3 microssatelites/Scripts/GBKtoPTT.py {dirproject}')
            request.session['step01'] = True
            request.session.save()
            print('================================================================')
            print('=                       Executando o IMEx                      =')
            print('================================================================')
            request.session['statusProcessament'] = "Extracting Microsatellites..."
            request.session.save()
            paramsDefaul = request.POST['paramsRadio']
            
            if paramsDefaul == '0':
                params = '1 1 1 2 2 2 10 10 10 10 10 10 12 6 4 3 3 3 15 1 1 1 100 3 0'
            else:
                impMono = request.POST['impMono'] 
                impDi = request.POST['impDi']
                impTri = request.POST['impTri']
                impTetra = request.POST['impTetra']
                impPenta = request.POST['impPenta']
                impHexa = request.POST['impHexa']
                impPerMono = request.POST['impPerMono'] 
                impPerDi = request.POST['impPerDi']
                impPerTri = request.POST['impPerTri']
                impPerTetra = request.POST['impPerTetra']
                impPerPenta = request.POST['impPerPenta']
                impPerHexa = request.POST['impPerHexa']
                minRepMono = request.POST['minRepMono'] 
                minRepDi = request.POST['minRepDi']
                minRepTri = request.POST['minRepTri']
                minRepTetra = request.POST['minRepTetra']
                minRepPenta = request.POST['minRepPenta']
                minRepHexa = request.POST['minRepHexa']
                sizeFlan = request.POST['sizeFlan']
                genAlin = request.POST.get('genAlin')
                if genAlin == 'on':
                    genAlin = 1
                else:
                    genAlin = 0
                idCod = request.POST.get('idCod')
                if idCod == 'on':
                    idCod = 1
                else:
                    idCod = 0
                maxComp = request.POST['maxComp']
                standLevel = request.POST['standLevel']
                ssrType = request.POST['ssrType']
                
                params = f"{impMono} {impDi} {impTri} {impTetra} {impPenta} {impHexa} {impPerMono} {impPerDi} {impPerTri} {impPerTetra} {impPerPenta} {impPerHexa} {minRepMono} {minRepDi} {minRepTri} {minRepTetra} {minRepPenta} {minRepHexa} {sizeFlan} {genAlin} 1 {idCod} {maxComp} {standLevel} {ssrType}"

            os.system(f'mkdir {dirproject}/{subdirectories[0]}/OutPutProcessed')
            os.system(f'python3 microssatelites/Scripts/IMEX.py {dirproject} {params}')
            request.session['step02'] = True
            request.session.save()

            # os.system(f'mkdir {dirproject}/{subdirectories[0]}/OutPutProcessed')
            # os.system(f'cp -R IMEx_OUTPUT {dirproject}/{subdirectories[0]}/OutPutProcessed')

            print('================================================================')
            print('=                Processando Arquivos do IMEx                  =')
            print('================================================================')
            request.session['statusProcessament'] = "Extracting SSR Data..."
            request.session.save()
            # Ler Pasta do IMEx_OUTPUT
            files = os.listdir(f'{dirproject}/UserOutputs/OutPutProcessed/IMEx_OUTPUT')
            if '.DS_Store' in files:
                files.remove('.DS_Store')
            cont = 1
            for i in files:
                path_file_summary = f'{dirproject}/UserOutputs/OutPutProcessed/IMEx_OUTPUT/'+ i +'/TEXT_OUTPUT/'+ i + '_summary.txt'
                path_file_aln = f'{dirproject}/UserOutputs/OutPutProcessed/IMEx_OUTPUT/'+ i +'/TEXT_OUTPUT/'+ i + '_aln.txt'
                # Extrair Dados do Summary
                print('Extraindo dados do Arquivo Summary')
                extractSummary(path_file_summary, project)
                if os.path.exists(path_file_aln):
                    print(f'Lendo arquivo {cont} de {len(files)}')
                    # path_file_out = 'UserOutputs/OutPutProcessed/'
                    # os.system('python3 microssatelites/Scripts/newRead.py ' + path_file_aln + ' ' + str(project.pk))
                    doc2db(request, path_file_aln, project)
                    request.session['percent03'] = round(cont/len(files) * 100, 1)
                    request.session.save()
                else:
                    print('Arquivo de Entrada não encontrado!')
                cont+=1
            request.session['statusProcessament'] = "Finishing..."
            request.session['step03'] = True
            request.session.save()
            print('================================================================')
            print('=                  Dados para os Graficos                      =')
            print('================================================================')
            dataStatistics = DataStatistic.objects.filter(project=project)
            projectdata = ProjectData.get_data(project.pk)
            totalDataStatistic = DataStatistic.get_total_data_statistic(project.pk)
            motifs = ProjectData.get_motifs(project.pk)
            lista = []
            listaCepas = []
            listaCepasTotais = []
            for i in motifs:
                lista.append(i)
                listaCepas.append(ProjectData.get_cepas(i[0], project.pk, i[2]))

            for list in listaCepas:
                for l in list:
                    if l[1] not in listaCepasTotais:
                        listaCepasTotais.append(l[1])
            motifs2 = ProjectData.get_motifs2(project.pk)
            lista2 = []
            listaCepas2 = []
            listaCepasTotais2 = []
            for j in motifs2:
                lista2.append(j)
                listaCepas2.append(ProjectData.get_cepas2(j[0], project.pk))
            for list2 in listaCepas2:
                for l2 in list2:
                    if l2[1] not in listaCepasTotais2:
                        listaCepasTotais2.append(l2[1])
            end_time = time.time()
            time_exec = time.strftime('%H:%M:%S', time.localtime(end_time - start_time))
            return render(request,'result.html', {'user': user, 'project': project, 'dataStatistics': dataStatistics, 'projectdata': projectdata, 'totalDataStatistic': totalDataStatistic, 'lista':lista, 'lista2':lista2, 'listaCepas':listaCepas, 'listaCepas2': listaCepas2, 'listaCepasTotais':listaCepasTotais, 'listaCepasTotais2':listaCepasTotais2, 'time_exec': time_exec})
    else:
        request.session['project'] = None
        request.session['statusProcessament'] = None
        request.session['step01'] = False
        request.session['step02'] = False
        request.session['step03'] = False
        request.session['percent03'] = 0
        request.session['filePercent'] = 0
        request.session['totalUpload'] = False
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

# FUNÇÕES ACESSÓRIAS
def handle_uploaded_file(request, f, directory):
    destination = open(f'{directory}/{f}', 'wb+')
    file_size = f.size
    uploaded_size = 0
    for chunk in f.chunks():
        destination.write(chunk)
        uploaded_size += len(chunk)
        percentage = round((uploaded_size / file_size) * 100)
        request.session['statusProcessament'] = f'Sending file {f} {percentage}%'
        request.session['filePercent'] = percentage
        request.session.save()
    destination.close()


def processament(request):
    # Seu código de processamento aqui
    for i in range(100):
        username = f"user{i}"
        request.session['temp_username'] = username
        # request.session.save()
        time.sleep(1)
    # Atualizando valor 'executing' após o loop
    return render(request, 'processament.html')

def get_processing_status(request):
    # Insira aqui o código para obter o status do processamento atual
    project = request.session.get('project', None)
    
    if project:
        data = {
            'statusProcessament': request.session['statusProcessament'],
            'step01' : request.session['step01'],
            'step02' : request.session['step02'],
            'step03' : request.session['step03'],
            'percent03' : request.session['percent03']
        }
    else:
        data = {
            'statusProcessament': 'Starting...',
            'step01' : False,
            'step02' : False,
            'step03' : False,
            'percent03' : 0
        }
    return JsonResponse(data)

def get_uploaded_file(request):
    file = request.session.get('file', None)

    if file:
        data = {
            'file' : request.session['file'],
            'filePercent' : request.session['filePercent'],
            'totalUpload' : request.session['totalUpload']
        }
    else:
        data = {
            'file' : 'Analyzing your dataset...',
            'filePercent' : 0,
            'totalUpload' : False
        }
    return JsonResponse(data)

def dadosGrafico(request):
    projectdata = ProjectData.get_motifs(57)
    lista = []
    listaCepas = []
    listaCepasTotais = []
    for i in projectdata:
        lista.append(i)
        listaCepas.append(ProjectData.get_cepas(i[0], 57))

    for list in listaCepas:
        for l in list:
            if l[1] not in listaCepasTotais:
                listaCepasTotais.append(l[1])
    print(listaCepasTotais)
    
    context = {
        'lista': lista,
        'listaCepas': listaCepas,
        'listaCepasTotais': listaCepasTotais
    }
    return render(request,'datateste.html', context)

def extractSummary(file, project):
    perfeitos = 0
    imperfeitos = 0
    codificante = 0
    naoCodificante = 0
    perfCoding = 0
    perfNonCoding = 0
    impCoding = 0
    impNonCoding = 0

    perfMono = 0
    perfDi = 0
    perfTri = 0
    perfTetra = 0
    perfPenta = 0
    perfHexa = 0
    impMono = 0
    impDi = 0
    impTri = 0
    impTetra = 0
    impPenta = 0
    impHexa = 0

    with open(file, 'r') as arquivo:
        linhas = arquivo.readlines()
    #Count do total de SSR (-2 para desconsiderar as duas primeiras linhas, cabeçalho e divisor)
    totalSSR = len(linhas)-2

    # Percorre as linhas do arquivo
    for linha in linhas:
        # Desconsidera as linhas 1 e 2
        
        if not((linha == linhas[0]) or (linha == linhas[1])):
            # Separa as colunas baseado no espaço em branco entre elas
            linhaIndex = linha.split()

            # Consulta a coluna 6
            if int(linhaIndex[5]) == 0:
                # Perfeitos
                perfeitos += 1

                if len(linhaIndex[0]) == 1:
                    perfMono += 1

                if len(linhaIndex[0]) == 2:
                    perfDi += 1

                if len(linhaIndex[0]) == 3:
                    perfTri += 1

                if len(linhaIndex[0]) == 4:
                    perfTetra += 1

                if len(linhaIndex[0]) == 5:
                    perfPenta += 1

                if len(linhaIndex[0]) == 6:
                    perfHexa += 1

                if "Coding" in linhaIndex:
                    perfCoding += 1
                else:
                    perfNonCoding += 1
            else:
                # Imperfeitos
                imperfeitos += 1

                if len(linhaIndex[0]) == 1:
                    impMono += 1

                if len(linhaIndex[0]) == 2:
                    impDi += 1

                if len(linhaIndex[0]) == 3:
                    impTri += 1

                if len(linhaIndex[0]) == 4:
                    impTetra += 1

                if len(linhaIndex[0]) == 5:
                    impPenta += 1

                if len(linhaIndex[0]) == 6:
                    impHexa += 1

                if "Coding" in linhaIndex:
                    impCoding += 1
                else:
                    impNonCoding += 1
        codificante = perfCoding + impCoding
        naoCodificante = perfNonCoding + impNonCoding
        cepa = file.split("/")[-1].replace('_summary.txt',"")

    # data = {'Total SSR': totalSSR,
    # 'Total Codificante': codificante,
    # 'Total não Codificante': naoCodificante,
    # 'Mono': perfMono + impMono,
    # 'Di': perfDi + impDi,
    # 'Tri': perfTri + impTri,
    # 'Tetra': perfTetra + impTetra,
    # 'Penta': perfPenta + impPenta,
    # 'Hexa': perfHexa + impHexa,
    # 'Total Perfeitos': perfeitos,
    # 'Total Perfeitos Codificantes': perfCoding,
    # 'Total Perfeitos não Codificantes': perfNonCoding,
    # 'Perfeito Mono': perfMono,
    # 'Perfeito Di': perfDi,
    # 'Perfeito Tri': perfTri,
    # 'Perfeito Tetra': perfTetra,
    # 'Perfeito Penta': perfPenta,
    # 'Perfeito Hexa': perfHexa,
    # 'Total Imperfeitos': imperfeitos,
    # 'Total Imperfeitos Codificantes': impCoding,
    # 'Total Imperfeitos não Codificantes': impNonCoding,
    # 'Imperfeito Mono': impMono,
    # 'Imperfeito Di': impDi,
    # 'Imperfeito Tri': impTri,
    # 'Imperfeito Tetra': impTetra,
    # 'Imperfeito Penta': impPenta,
    # 'Imperfeito Hexa': impHexa}

    dataStatistic = DataStatistic.objects.create(
               cepa = cepa,
               totalSSR = totalSSR,
               totalCodificante = codificante,
               totalNaoCodificante = naoCodificante,
               mono = perfMono + impMono,
               di = perfDi + impDi,
               tri = perfTri + impTri,
               tetra = perfTetra + impTetra,
               penta = perfPenta + impPenta,
               hexa = perfHexa + impHexa,
               totalPerfeitos = perfeitos,
               totalPerfeitosCodificantes = perfCoding,
               totalPerfeitosNaoCodificantes = perfNonCoding,
               perfeitoMono = perfMono,
               perfeitoDi = perfDi,
               perfeitoTri = perfTri,
               perfeitoTetra = perfTetra,
               perfeitoPenta = perfPenta,
               perfeitoHexa = perfHexa,
               totalImperfeitos = imperfeitos,
               totalImperfeitosCodificantes = impCoding,
               totalImperfeitosNaoCodificantes = impNonCoding,
               imperfeitoMono = impMono,
               imperfeitoDi = impDi,
               imperfeitoTri = impTri,
               imperfeitoTetra = impTetra,
               imperfeitoPenta = impPenta,
               imperfeitoHexa = impHexa,
               project = project
    )
    dataStatistic.save()
    return dataStatistic

def doc2db(request, path, project):
    arquivo = open(path, 'r')
    linhas = arquivo.readlines()
    cont = 0

    objetos = []
    repeatMotif = ''
    lflanking = ''
    rflanking = ''
    consensus = ''
    iterations = ''
    tractLength = ''
    repeatMotifList = []
    motif = []
    cepa = path.split("/")[-1].replace('_aln.txt',"")

    # Ler o arquivo aln e extrai as informações dele
    for line in linhas:
        if(line.startswith('Consensus:')):
            repeatMotif = line.split(':')[1].replace("\n","")
            # repeatMotifList.append(repeatMotif)
            # print ('Repeat motif: ', line.split(':')[1])
        if(line.startswith('Start:')):
            match = re.findall(r'\d+', line)
            pos_start = int(match[0])
            pos_end = int(match[1])
            iterations = int(match[2])

        if(line.startswith('Total Imperfections:')):
            tractLength = line.split()[-1].replace("\n","")
            # print(line.split()[-1])
        if(line.startswith('Left Flanking Sequence:')):
            lflanking = linhas[cont+1].replace("\n","")
            consensus = linhas[cont+3].replace("\n","")
            # print('Left Flanking Sequence: ',linhas[cont+1])
        if(line.startswith('Right Flanking Sequence:')):
            rflanking = linhas[cont+1].replace("\n","")
            motif = [
                        { 'repeat': repeatMotif,
                          'iterations': iterations,
                          'tractLength': tractLength,
                          'lflanking': lflanking,
                          'consensus': consensus,
                          'rflanking': rflanking,
                        }
                    ]
            repeatMotifList.append(motif)
            projectdata = ProjectData.objects.create(cepa = cepa, motif = repeatMotif, lflanking = lflanking ,  rflanking = rflanking , iterations = iterations, tractlength = tractLength,  consensus = consensus, pos_start = pos_start, pos_end = pos_end, project = project)
            request.session['statusProcessament'] = f'Processing in the Database {cont} / {len(linhas)}'
            request.session.save()
            projectdata.save()
            
            # cursor.execute(f"INSERT INTO DATA (MOTIF, LFLANK, RFLANK, ITERATIONS, TRACKLENGTH, CONSENSUS, CONSULTA, CEPA) VALUES ('{repeatMotif}', ' {lflanking} ', ' {rflanking} ', {iterations}, {tractLength}, '{ consensus}', {1}, '{cepa}');")
        # objetos.append(File(cepa, repeatMotifList))
        cont += 1
    arquivo.close()

    print("Done.")

def result(request):
    if request.method == 'POST':
        context = {
            'projectdata' : request.POST['projectdata'],
            'dataStatistics': request.POST['dataStatistics'],
            'totalDataStatistic': request.POST['totalDataStatistic'],
            'lista': request.POST['lista'],
            'listaCepas': request.POST['listaCepas'],
            'listaCepasTotais': request.POST['listaCepasTotais']
        }
    else:
        dataStatistics = DataStatistic.objects.filter(project=1)
        totalDataStatistic = DataStatistic.get_total_data_statistic(1)
        projectdata = ProjectData.get_data(1)
        motifs = ProjectData.get_motifs(1)
        lista = []
        listaCepas = []
        listaCepasTotais = []
        for i in motifs:
            lista.append(i)
            listaCepas.append(ProjectData.get_cepas(i[0], 1, i[2]))

        for list in listaCepas:
            for l in list:
                if l[1] not in listaCepasTotais:
                    listaCepasTotais.append(l[1])
        
        motifs2 = ProjectData.get_motifs2(1)
        lista2 = []
        listaCepas2 = []
        listaCepasTotais2 = []
        for j in motifs2:
            lista2.append(j)
            listaCepas2.append(ProjectData.get_cepas2(j[0], 1))
        
        for list2 in listaCepas2:
            for l2 in list2:
                if l2[1] not in listaCepasTotais2:
                    listaCepasTotais2.append(l2[1])
        pk = {'pk': 1}
        context = {
            'projectdata' : projectdata,
            'project': pk,
            'dataStatistics': dataStatistics,
            'totalDataStatistic': totalDataStatistic,
            'lista': lista,
            'listaCepas': listaCepas,
            'listaCepasTotais': listaCepasTotais,
            'lista2': lista2,
            'listaCepas2': listaCepas2,
            'listaCepasTotais2': listaCepasTotais2,
        }
    return render(request,'result.html', context)

def download_folder(request, project):

    folder_name = 'USER'+ project + '_PROJECT' + project
    
    # Caminho completo para a pasta a ser compactada e baixada
    folder_path = os.path.join(folder_name)

    # Nome do arquivo zip que será baixado
    zip_filename = f'{folder_name}.zip'

    # Abre o arquivo zip para gravação
    with ZipFile(zip_filename, 'w') as zip_file:
        # Percorre a pasta e adiciona cada arquivo a o arquivo zip
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

    # Abre o arquivo zip para leitura e cria uma resposta HTTP para download
    with open(zip_filename, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'

    # Remove o arquivo zip do disco rígido
    os.remove(zip_filename)

    # Retorna a resposta HTTP para download
    return response

def viewgen(request):
    return render(request, 'viewgen.html')

