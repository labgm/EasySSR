import os
import time

inicio = time.time()

os.system('mkdir GBKs')
os.system('cp -r data/GBKs gbk2ptt-2')

os.system("ls gbk2ptt-2/GBKs/ > gbk2ptt-2/meusarquivos.txt")
# print(os.system("ls gbk2ptt-2/GBKs/"))

meusarquivos = open("gbk2ptt-2/meusarquivos.txt", "r")

for i in meusarquivos:
    var =  i.replace("\n","")
    inicio_p = time.time()
    ptt = var[:-4]
    os.system("perl gbk2ptt-2/GBKtoPTT.pl <gbk2ptt-2/GBKs/"+ str(var) + " > " + str(ptt) + "ptt" + " -o gbk2ptt-2/ptt-files/")
    print ("Convertendo o arquivo "+ str(var) + " para o formato .ptt ")
    print ("Conversão concluida! Arquivo gerado: " + str(ptt) + "ptt ")
    #print ("mv " + str(ptt) + "ptt ptt-files/")
    os.system("mv " + str(ptt) + "ptt gbk2ptt-2/ptt-files/")
    #print ("perl GBKtoPTT.pl <GBKs/"+ str(var) + " > " + str(ptt) + "ptt" + " -o ptt-files/")
    fim_p = time.time()
    print("Tempo: "+str(fim_p - inicio_p)+"\n")
    #time.sleep(6)
# os.system('rm -r ')
fim = time.time()
print("\nTempo Total: "+str(fim - inicio)+"\n")

os.system("touch gbk2ptt-2/time_output.txt")
time_output = open("gbk2ptt-2/time_output.txt","w")

time_output.write("Tempo Total: "+str(fim - inicio))
time_output.close()
