import pandas as pd
import os
import argparse
from plot import pyplot

#Variáveis dos Valores
header = []
cepas = []

totalSSR = []
totalCodificantes = []
totalNCodificantes = []
totalMono = []
totalDi = []
totalTri = []
totalTetra = []
totalPenta = []
totalHexa = []
totalPerfeitos = []
totalPerfCoding = []
totalPerfNonCoding = []
totalPerfMono = []
totalPerfDi = []
totalPerfTri = []
totalPerfTetra = []
totalPerfPenta = []
totalPerfHexa = []
totalImperfeitos = []
totalImpCoding = []
totalImpNonCoding = []
totalImpMono = []
totalImpDi = []
totalImpTri = []
totalImpTetra = []
totalImpPenta = []
totalImpHexa = []

#Pega a pasta que contém os arquivos TXT como argumento
parser = argparse.ArgumentParser(description='')
parser.add_argument('--input', type=str, default='UserOutputs/OutPutProcessed/', help='Input folder containing the txt files')
parser.add_argument('--output_file', type=str, default='UserOutputs/Microsat', help='Output file containing the data in xlsx format')
parser.add_argument('--config_file', type=str, default='config.yaml', help='File to write config file [default: config.yaml]')
args = parser.parse_args()

#Cria uma lista com as subpastas das CEPAS
folders = os.listdir(args.input)

#Para cada pasta da Lista:
for f in folders:
    #Verifica se não é pasta oculta
    if not f.startswith('.') and os.path.isfile(args.input+f):
        # print(f)
        cepas.append(f.replace(".txt", ""))
        # Abre o arquivo .txt da Cepa
        # with open(args.input + f, 'r') as arquivo:
        # with open(args.input + f, 'r') as arquivo:
        with open(args.input + "/" + f, 'r') as arquivo:
            linhas = arquivo.readlines()
        #Count do total de SSR (-2 para desconsiderar as duas primeiras linhas, cabeçalho e divisor)
        # totalSSR = len(linhas)-2
        # cepas.append(f)
        # Percorre as linhas do arquivo
        # print(linhas)
        for linha in linhas:
            # Separa as colunas baseado no espaço em branco entre elas
            linhaIndex = linha.split('|')
            # print(linha)
            if (linha == linhas[0]):
                header = linhaIndex
            else:
                totalSSR.append(int(linhaIndex[0]))
                totalCodificantes.append(int(linhaIndex[1]))
                totalNCodificantes.append(int(linhaIndex[2]))
                totalMono.append(int(linhaIndex[3]))
                totalDi.append(int(linhaIndex[4]))
                totalTri.append(int(linhaIndex[5]))
                totalTetra.append(int(linhaIndex[6]))
                totalPenta.append(int(linhaIndex[7]))
                totalHexa.append(int(linhaIndex[8]))
                totalPerfeitos.append(int(linhaIndex[9]))
                totalPerfCoding.append(int(linhaIndex[10]))
                totalPerfNonCoding.append(int(linhaIndex[11]))
                totalPerfMono.append(int(linhaIndex[12]))
                totalPerfDi.append(int(linhaIndex[13]))
                totalPerfTri.append(int(linhaIndex[14]))
                totalPerfTetra.append(int(linhaIndex[15]))
                totalPerfPenta.append(int(linhaIndex[16]))
                totalPerfHexa.append(int(linhaIndex[17]))
                totalImperfeitos.append(int(linhaIndex[18]))
                totalImpCoding.append(int(linhaIndex[19]))
                totalImpNonCoding.append(int(linhaIndex[20]))
                totalImpMono.append(int(linhaIndex[21]))
                totalImpDi.append(int(linhaIndex[22]))
                totalImpTri.append(int(linhaIndex[23]))
                totalImpTetra.append(int(linhaIndex[24]))
                totalImpPenta.append(int(linhaIndex[25]))
                totalImpHexa.append(int(linhaIndex[26]))
#==============================================================================================================================
data = {'Cepa': cepas,
        'Total SSR': totalSSR,
        'Total Codificante': totalCodificantes,
        'Total não Codificante': totalNCodificantes,
        'Mono': totalMono,
        'Di': totalDi,
        'Tri': totalTri,
        'Tetra': totalTetra,
        'Penta': totalPenta,
        'Hexa': totalHexa,
        'Total Perfeitos': totalPerfeitos,
        'Total Perfeitos Codificantes': totalPerfCoding,
        'Total Perfeitos não Codificantes': totalPerfNonCoding,
        'Perfeito Mono': totalPerfMono,
        'Perfeito Di': totalPerfDi,
        'Perfeito Tri': totalPerfTri,
        'Perfeito Tetra': totalPerfTetra,
        'Perfeito Penta': totalPerfPenta,
        'Perfeito Hexa': totalPerfHexa,
        'Total Imperfeitos': totalImperfeitos,
        'Total imperfeitos Codificantes': totalImpCoding,
        'Total imperfeitos não Codificantes': totalImpNonCoding,
        'Imperfeito Mono': totalImpMono,
        'Imperfeito Di': totalImpDi,
        'Imperfeito Tri': totalImpTri,
        'Imperfeito Tetra': totalImpTetra,
        'Imperfeito Penta': totalImpPenta,
        'Imperfeito Hexa': totalImpHexa}
# print (data)
padroes = [sum(totalMono), sum(totalDi), sum(totalTri), sum(totalTetra), sum(totalPenta), sum(totalHexa)]
labels = ['Mono', 'Di', 'Tri', 'Tetra', 'Penta', 'Hexa']


pyplot(args.input,'Totais de Padrões', padroes, 'Padrões de Repetição', labels)
pyplot(args.input,'Perfeitos x Imperfeitos', [sum(totalPerfeitos), sum(totalImperfeitos)], 'Totais', ['Perfeitos', 'Imperfeitos'])
pyplot(args.input,'Totais Perfeitos', [sum(totalPerfMono), sum(totalPerfDi), sum(totalPerfTri), sum(totalPerfTetra), sum(totalPerfPenta), sum(totalPerfHexa)], 'Totais', ['Mono', 'Di', 'Tri', 'Tetra', 'Penta', 'Hexa'])
pyplot(args.input,'Totais Imperfeitos', [sum(totalImpMono), sum(totalImpDi), sum(totalImpTri), sum(totalImpTetra), sum(totalImpPenta), sum(totalImpHexa)], 'Totais', ['Mono', 'Di', 'Tri', 'Tetra', 'Penta', 'Hexa'])
pyplot(args.input,'Perfeitos Codificantes x Perfeitos Não-Codificantes', [sum(totalPerfCoding), sum(totalPerfNonCoding)], 'Totais', ['Perfeitos Codificantes', 'Perfeitos Não-Codificantes'])
pyplot(args.input,'Imperfeitos Codificantes x Imperfeitos Não-Codificantes', [sum(totalImpCoding), sum(totalImpNonCoding)], 'Totais', ['Imperfeitos Codificantes', 'Imperfeitos Não-Codificantes'])
pyplot(args.input,'Codificantes x Não-Codificantes', [sum(totalCodificantes), sum(totalNCodificantes)], 'Totais', ['Codificantes', 'Não-Codificantes'])

df = pd.DataFrame(data)
df.to_excel(args.output_file + '.xlsx')
df.to_csv(args.output_file + '.txt')
