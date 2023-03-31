import os
import time
import sys
# import utils

def renameFiles(files, path):
    for i in files:
        r = i.replace(' ', '_').replace('-', '')
        if(r != i):
            os.rename(path + i, path + r)
            print(f'Renomeando {i} por {r}')


inicio = time.time()

path = f'{sys.argv[1]}/UserData/GBKs/'
path2 = f'{sys.argv[1]}/UserData/'
files = os.listdir(path)

renameFiles(files, path)

files = os.listdir(path)
if '.DS_Store' in files:
    files.remove('.DS_Store')
print('Iniciando Conversão...')
print('Arquivos a serem convertidos: ' + str(files))

for i in files:
    inicio_p = time.time()
    ptt = i.split('.g')
    os.system('perl microssatelites/Scripts/gbk2ptt-2/GBKtoPTT.pl < '+ path + i + ' > ' + ptt[0] + '.ptt')
    print ("Conversão concluida! Arquivo gerado: " + ptt[0] + ".ptt ")
    fim_p = time.time()
    print("Tempo: "+str(fim_p - inicio_p)+"\n")

if os.path.exists(f'{path2}PTTs/'):
    os.system(f'rm -r {path2}PTTs/')

os.system('mkdir PTTs')
os.system('mv *.ptt PTTs/')
os.system('mv PTTs/ '+ path2)
fim = time.time()

print('Tempo Total: '+ str(fim - inicio))
