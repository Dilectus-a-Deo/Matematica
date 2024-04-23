#Dados das alturas das mulhres

import statistics

#Dados em sala de aula

dados = [77, 88, 49, 65, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 67,80,90,75,78,77,76,79,81,73,71,66,67,68,69,70]

#média

media = statistics.mean(dados)

#mediana

mediana = statistics.mean(dados)

#desvio medio

desvio_medio = statistics.mean(dados)

#desvio padrao

desvio_padrao = statistics.mean(dados)

#imprimindo resultados

print(f" Desvio Médio: {desvio_medio} ")
print(f" Mediana: {mediana} ")
print(f" Média: {media} ")
print(f" Desvio Padrão : {desvio_padrao} ")