import json
import os
import numpy as np
from itertools import groupby



files = os.listdir('../UserOutputs/OutPutProcessed/json/')

# print(files + )
for i in files:
    with open('../UserOutputs/OutPutProcessed/json/' + i, encoding='utf-8') as file_json:
        dados = json.load(file_json)
        print('Cepa: ' + dados['name'])
        # motif = dict(dados['repeatMotif'])
        print(type(dados['repeatMotif']))
        # print('Motivos: ' + dados['moti'])
        # cont = 0
        # for i in dados['repeatMotif']:
        #     # Agrupamento dos Motivos
        #     for f in groupby(dict(dados['repeatMotif']), key=lambda x: x.repeatMotif):
        #         if f[0] != '':
        #             # print('O Motivo ', f[0], 'se repete ', repeatMotifList.count(f[0]), ' vezes.')
        #             motif.append(f[0])
        #             numRepeats.append(repeatMotifList.count(f[0]))
        #
        #     dictMotif = dict(zip(motif, numRepeats))
        #     print(dictMotif)
        #
        #     print(str(cont))
        #     cont += 1
# for i in dados:
#     print(i[0][0])
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
