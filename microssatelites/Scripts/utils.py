import os
from file import File

def renameFiles(files, path):
    for i in files:
        r = i.replace(' ', '_').replace('-', '')
        if(r != i):
            os.rename(path + i, path + r)
            print(f'Renomeando {i} por {r}')

def read_file(path):
    # Open the file report.txt
    tsv_file = open(path)
    read_tsv = csv.reader(tsv_file, delimiter="\t")

    # cont = 0 # Controle de linhas
    montadores = [] # Lista de Objetos (Montadores)
    for row in read_tsv:
        print (row)
        # if cont == 0:
        #     objects = len(row)-1
        #     for i in range(objects):
        #         montadores.append(File(row[i+1]))
        #
        # elif cont == 13:
        #     for i in range(objects):
        #         montadores[i].contigs = int(row[i+1].replace("\n",""))
        #
        # elif cont == 15:
        #     for i in range(objects):
        #         montadores[i].total_length = int(row[i+1].replace("\n",""))
        #
        # elif cont == 17:
        #     for i in range(objects):
        #         montadores[i].n50 = int(row[i+1].replace("\n",""))
        #
        # elif cont == 18:
        #     for i in range(objects):
        #         montadores[i].n75 = int(row[i+1].replace("\n",""))
        #
        # elif cont == 19:
        #     for i in range(objects):
        #         montadores[i].l50 = int(row[i+1].replace("\n",""))
        #
        # elif cont == 20:
        #     for i in range(objects):
        #         montadores[i].l75 = int(row[i+1].replace("\n",""))
        # cont += 1
    return montadores
