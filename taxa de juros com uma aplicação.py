#Inserindo variaveis

montante = float(input('Digite o valor do montante: '))
capital = float(input('Digite o valor do capital: '))
capital_2 = float(input('Digite o valor do capital_2: '))
tempo = float(input('Digite o valor do tempo: '))

#Inserindo formula

taxa_de_juros = (montante - capital) / (capital_2 * tempo)

#imprimindo valores

print(f'o valor da taxa de juros é: {taxa_de_juros} %' )