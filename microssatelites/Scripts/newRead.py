import pandas as pd
import json
from itertools import groupby
from file import File
import sys
import os

# adding Folder_2/subfolder to the system path

# import mysql.connector
# from mysql.connector import errorcode
# from connect import connect

# def busca(lista, element):
#     for i in range(len(lista)):
#         if lista[i] == element:
#             return i
#     return None

# CONEXAO COM O Database
config = {
  'host':'localhost',
  'user':'root',
  'password':'',
  'database':'FASTSSR'
}

# try:
#    conn = mysql.connector.connect(**config)
#    print("Connection established")
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with the user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   cursor = conn.cursor()




# files = os.listdir('UserOutputs/OutPutProcessed/IMEx_OUTPUT')
arquivo = open(sys.argv[1], 'r')
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
cepa = sys.argv[1].split("/")[-1].replace('_aln.txt',"")

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
        projectdata = ProjectData.objects.create(cepa = cepa, motif = repeatMotif, lflanking = lflanking ,  rflanking = rflanking , iterations = iterations, tractlength = tractLength,  consensus = consensus, project = sys.argv[1])
        projectdata.save()
        # cursor.execute(f"INSERT INTO DATA (MOTIF, LFLANK, RFLANK, ITERATIONS, TRACKLENGTH, CONSENSUS, CONSULTA, CEPA) VALUES ('{repeatMotif}', ' {lflanking} ', ' {rflanking} ', {iterations}, {tractLength}, '{ consensus}', {1}, '{cepa}');")
    objetos.append(File(cepa, repeatMotifList))
    cont += 1
arquivo.close()

# Cleanup Database
# conn.commit()
# cursor.close()
# conn.close()
print("Done.")
# print(objetos)
# print('Cepa:' + objetos[-1].cepa)
# print('Motivos:')
#
# for i in repeatMotifList:
#     print('Motivos: ' + i)


motif = []
numRepeats = []

# Criar o JSON
# if not os.path.exists('UserOutputs/OutPutProcessed/json/'):
#     os.system('mkdir UserOutputs/OutPutProcessed/json/')
#
# out_file = open('UserOutputs/OutPutProcessed/json/'+ cepa + '.json', "w")
#
# json.dump(objetos[-1].__dict__, out_file, indent = 6)
#
# out_file.close()


# Corynebacterium_diphtheriae_NCTC11397.fna


# Agrupamento dos Motivos
# for f in groupby(objetos, key=lambda x: x.repeatMotif):
#     if f[0] != '':
#         # print('O Motivo ', f[0], 'se repete ', repeatMotifList.count(f[0]), ' vezes.')
#         motif.append(f[0])
#         numRepeats.append(repeatMotifList.count(f[0]))
#
# dictMotif = dict(zip(motif, numRepeats))
# # print(dictMotif)
# df = pd.DataFrame(dictMotif, index=[0])
# df.to_csv('out.csv', index=False)
