#Estátistica com strings 

import statistics

# Solicitando ao usuário o número de entradas 

dados = int(input("Quantos números você gostaria de inserir ? : " ))

# Criando uma lista de números

lista_numeros = []

# Loop para inserir os números

for i in range(dados):
    numero = float(input("Insira o número: "))
    lista_numeros.append(numero)

#Cálculando a média

media = statistics.mean(lista_numeros)

#Cálculando a mediana

mediana = statistics.median(lista_numeros)

#Cáculando o desvio padrão

desvio_padrao = statistics.stdev(lista_numeros)

 
# Imprimindo a média , mediana e o desvio padrão

print(f"A média dos números inseridos é {media}")
print(f"A mediana dos números inseridos é {mediana}")
print(f"O desvio padrão dos números inseridos é {desvio_padrao}")