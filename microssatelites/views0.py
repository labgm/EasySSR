from django.shortcuts import render, redirect
from .forms import NameForm, LoginForm, UploadFileForm, DownloadForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
import os
import time
from .models import User, Project, ProjectData
# Celery Task
from .tasks import ProcessDownload

# Create your views here.

def demo_view(request):
    # If method is POST, process form data and start task
    files = []
    # Create Task
    download_task = ProcessDownload.delay()
    # Get ID
    print (download_task)
    task_id = download_task.task_id

    # Print Task ID
    print(f'Celery Task ID: {task_id}')
    # Return demo view with Task ID
    return render(request, 'progress.html', {'task_id': task_id})

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Create Task
            download_task = ProcessDownload.delay()
            # Get ID
            print (download_task)
            task_id = download_task.task_id

            # Print Task ID
            print(f'Celery Task ID: {task_id}')
            # Return demo view with Task ID
            return render(request, 'progress.html', {'task_id': task_id})
    else:
        # Return demo view
        return render(request, 'progress.html', {})

# def demo_view(request):
#     # If method is POST, process form data and start task
#     if request.method == 'POST':
#         # Get form instance
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             arquivo = request.FILES.getlist('fileFasta')[0]
#             print(f'Uploading: {arquivo}')
# 			# Create Task
#             upload_task = ProcessDownload.delay(url)
# 			# Get ID
#             task_id = upload_task.task_id
# 			# Print Task ID
#             print (f'Celery Task ID: {task_id}')
#
# 			# Return demo view with Task ID
#             return render(request, 'progress.html', {'task_id': task_id})
#         else:
#             # Return demo view
#             return render(request, 'progress.html', {'form': form})
#
#
#     else:
#         # Get form instance
#         form = UploadFileForm()
#         # Return demo view
#         return render(request, 'progress.html', {'form': form})


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

            # CRIAR O PROJETO NO DB
            project = Project.objects.create(user=user)
            project.save()

            # CRIAR PASTA DO PROJETO USER[PK]_PROJECT[PK]
            dirproject = f'USER{user.pk}_PROJECT{project.pk}'
            os.system(f'mkdir {dirproject}')

            # CRIAR SUBPASTAS DO PROJETO
            subdirectories = ['UserOutputs', 'UserData', 'UserData/FASTA', 'UserData/GBKs']
            for subdir in subdirectories:
                os.system(f'mkdir {dirproject}/{subdir}')

            # TRANSFERIR OS ARQUIVOS PARAS AS SUBPASTAS
            # FASTAs
            for f in request.FILES.getlist('fileFasta'):
                handle_uploaded_file(f, f'{dirproject}/{subdirectories[2]}')

            # GBKs
            for f in request.FILES.getlist('fileGBK'):
                handle_uploaded_file(f, f'{dirproject}/{subdirectories[3]}')


            print('================================================================')
            print('=                 Convertendo Arquivos GBKtoPTT                =')
            print('================================================================')
            os.system(f'python3 microssatelites/Scripts/GBKtoPTT.py {dirproject}')

            print('================================================================')
            print('=                       Executando o IMEx                      =')
            print('================================================================')
            # os.system(f'python3 microssatelites/Scripts/IMEX.py {dirproject}')
            os.system(f'mkdir {dirproject}/{subdirectories[0]}/OutPutProcessed')
            os.system(f'cp -R IMEx_OUTPUT {dirproject}/{subdirectories[0]}/OutPutProcessed')

            print('================================================================')
            print('=            Processando Arquivos Summary do IMEx              =')
            print('================================================================')

            files = os.listdir(f'{dirproject}/UserOutputs/OutPutProcessed/IMEx_OUTPUT')
            for i in files:
                path_file = f'{dirproject}/UserOutputs/OutPutProcessed/IMEx_OUTPUT/'+ i +'/TEXT_OUTPUT/'+ i + '_summary.txt'
                print (path_file)
                if os.path.exists(f'{dirproject}/UserOutputs/OutPutProcessed'):
                    path_file_out = f'{dirproject}/UserOutputs/OutPutProcessed/'
                    os.system('python3 microssatelites/Scripts/read.py ' + path_file + ' > '+ path_file_out + i +'.txt')
                else:
                    os.system('mkdir UserOutputs UserOutputs/OutPutProcessed')
            print('================================================================')
            print('=                      Criando Tabela 01                       =')
            print('================================================================')
            os.system(f'python3 microssatelites/Scripts/createTable.py --input {dirproject}/UserOutputs/OutPutProcessed/ --output_file {dirproject}/UserOutputs/Microsat')

            print('================================================================')
            print('=                      Dados para o DB                         =')
            print('================================================================')
            cont = 1
            for i in files:
                path_file_aln = f'{dirproject}/UserOutputs/OutPutProcessed/IMEx_OUTPUT/'+ i +'/TEXT_OUTPUT/'+ i + '_aln.txt'
                if os.path.exists(path_file_aln):
                    print(f'Lendo arquivo {cont} de {len(files)}')
                    # path_file_out = 'UserOutputs/OutPutProcessed/'
                    # os.system('python3 microssatelites/Scripts/newRead.py ' + path_file_aln + ' ' + str(project.pk))
                    doc2db(path_file_aln, project)
                else:
                    print('Arquivo de Entrada não encontrado!')
                cont+=1
            return render(request,'result.html', {'user': user, 'project': project})
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

# FUNÇÕES ACESSÓRIAS
def handle_uploaded_file(f, directory):
    destination = open(f'{directory}/{f}', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def doc2db(path, project):
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
            iterations = line.split()[-1].replace("\n","")

            # print(line.split()[-1])
        if(line.startswith('Total Imperfections:')):
            tractLength = line.split()[-1].replace("\n","")
            # print(line.split()[-1])
        if(line.startswith('Left Flanking Sequence:')):
            lflanking = linhas[cont+1].replace("\n","")
            # print('Left Flanking Sequence: ',linhas[cont+1])
            consensus = linhas[cont+3].replace("\n","")
            # print('Consensus: ',linhas[cont+3])
            rflanking = linhas[cont+8].replace("\n","")
            # print('Right Flanking Sequence: ',linhas[cont+8])
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
            projectdata = ProjectData.objects.create(cepa = cepa, motif = repeatMotif, lflanking = lflanking ,  rflanking = rflanking , iterations = iterations, tractlength = tractLength,  consensus = consensus, project = project)
            projectdata.save()
            # cursor.execute(f"INSERT INTO DATA (MOTIF, LFLANK, RFLANK, ITERATIONS, TRACKLENGTH, CONSENSUS, CONSULTA, CEPA) VALUES ('{repeatMotif}', ' {lflanking} ', ' {rflanking} ', {iterations}, {tractLength}, '{ consensus}', {1}, '{cepa}');")
        # objetos.append(File(cepa, repeatMotifList))
        cont += 1
    arquivo.close()

    # Cleanup Database
    # conn.commit()
    # cursor.close()
    # conn.close()
    print("Done.")

def result(request):
    return render(request,'result.html')
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#             username = cd['username'],
#             password = cd['password'])
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Authenticated '\
#                 'sucessfully')
#             else:
#                 return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#             else:
#                 form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})

# def upload_file(request):
    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES['file'])
    #         return HttpResponseRedirect('/success/url/')
    # else:
    #     form = UploadFileForm()
    # return render(request, 'index.html', {'form': form})
