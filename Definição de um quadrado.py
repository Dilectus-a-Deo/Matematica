#Inserindo variáveis 

def calcular_quadrado(lado):
    perimetro = lado * 4 
    area = lado * lado
    return perimetro , area

#Pedindo para o usuário inserir o valor do lado 

lado = float(input('digite o valor do lado: '))

#Calculando Perímetro e a área

perimetro, area = calcular_quadrado(lado)

#Imprimindo o valor do lado e o perímetro

print(f'perimetro: {perimetro} - area: {area}')