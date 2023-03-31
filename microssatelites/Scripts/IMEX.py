import os
import time
from utils import *
import sys
import argparse

inicio = time.time()

path_fasta = f'{sys.argv[1]}/UserData/FASTA/'
path_ptt = f'{sys.argv[1]}/UserData/PTTs/'
path_imex = 'microssatelites/Scripts/IMEX2.1/imex_batch'
path_output = f'{sys.argv[1]}/UserOutputs/OutPutProcessed/'

files = os.listdir(path_fasta)
renameFiles(files, path_fasta)

# FUNÇÕES ===================================================================================
def get_parameters():
	all_parameters = []

	with open(f"microssatelites/Scripts/UserParameters.txt", "r") as parameters_file:
		for line in parameters_file:
			parameters = line.replace('\n',' ').split(':')
			all_parameters.append(parameters[1])
	return ' '.join(all_parameters).replace('  ',' ')
# ===========================================================================================

# ENTRADA DOS PARÂMETROS ==========================================================================================================================

# parameters = get_parameters()
parameters = ' '.join(sys.argv[2:])
print (f'Parameters: {parameters}')

# ==========================================================================================================================

# EXECUÇÃO DO IMEx ==========================================================================================================================
time.sleep(0.5)
print (" ###########Carregando###############"  )
time.sleep(0.5)
print ("Executando análises... ################")

# os.system("ls /UserData/Fasta/ > meusarquivos.txt")
files_fasta = os.listdir(path_fasta)

if('.DS_Store' in files_fasta):
	files_fasta.remove('.DS_Store')
for i in files_fasta:
	inicio_p = time.time()
	ptt = i.split('.f')
	os.system('chmod +x ' + path_imex)
	os.system(path_imex +" "+ path_fasta + i +" "+ parameters + " " + path_ptt + ptt[0] + ".ptt")
	print ("##Arquivo em analise##  Genoma Fasta: "+ i +" ptt file: " + ptt[0] + ".ptt")
	print(path_imex +" "+ path_fasta + i +" "+ parameters + " " + path_ptt + ptt[0] + ".ptt")
	fim_p = time.time()
if not os.path.exists(path_output):
	print('Pasta IMEx_OUTPUT não existe. Criando...')
	os.system('mkdir '+ path_output)
os.system('mv IMEx_OUTPUT/ '+ path_output)
print("Tempo: "+str(fim_p - inicio_p)+" ######################## ")


fim = time.time()
print("Tempo Total: "+str(fim - inicio)+"")
