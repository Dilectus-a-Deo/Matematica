import math

# inserindo variaveis

capital = float(input('digite o valor do capital: '))
taxa = float(input('digite o valor da taxa : '))
tempo = float(input('digite o valor o tempo: '))

# inserindo formula

juros = capital * taxa * tempo

# inserindo condicao

if juros >=2:
    print('o juros se manteve constante')
elif juros <=2:
    print('o juros diminuiu')
else:
    print('o juros aumentou ')

# imprimindo resutado

print(f'o valor do juros foi: {juros:.2f} R$')