import sys
import os

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

with open(sys.argv[1], 'r') as arquivo:
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

# Exibe os resultados
print("Total SSR\t|Total Codificante\t|Total não Codificante\t|Mono\t|Di\t|Tri\t|Tetra\t|Penta\t|Hexa\t|"+
      "Total Perfeitos\t|Total Perfeitos Codificantes\t|Total Perfeitos não Codificantes\t|Perfeito Mono\t|"+
      "Perfeito Di\t|Perfeito Tri\t|Perfeito Tetra\t|Perfeito Penta\t|Perfeito Hexa\t|Total Imperfeitos\t|"+
      "Total imperfeitos Codificantes\t|Total imperfeitos não Codificantes\t|Imperfeito Mono\t|Imperfeito Di\t|"+
      "Imperfeito Tri\t|Imperfeito Tetra\t|Imperfeito Penta\t|Imperfeito Hexa|\n" +
      str(totalSSR) + "\t\t|" + str(codificante) + "\t\t\t|" + str(naoCodificante) + "\t\t\t|" + str(perfMono + impMono) + "\t|" +
      str(perfDi + impDi) + "\t|" + str(perfTri + impTri) + "\t|" + str(perfTetra + impTetra) + "\t|" + str(perfPenta + impPenta) + "\t|" +
      str(perfHexa + impHexa) + "\t|" + str(perfeitos) + "\t\t\t|" + str(perfCoding) + "\t\t\t\t|" + str(perfNonCoding) + "\t\t\t\t\t|" +
      str(perfMono) + "\t\t|" + str(perfDi) + "\t\t|" + str(perfTri) + "\t\t|" + str(perfTetra) + "\t\t|" + str(perfPenta) + "\t\t|" +
      str(perfHexa) + "\t\t|" + str(imperfeitos) + "\t\t\t|" + str(impCoding) + "\t\t\t\t|" + str(impNonCoding) + "\t\t\t\t\t|" +
      str(impMono) + "\t\t\t|" + str(impDi) + "\t\t|" + str(impTri) + "\t\t|" + str(impTetra) + "\t\t\t|" + str(impPenta) + "\t\t\t|" +
      str(impHexa) + "\t\t|")
