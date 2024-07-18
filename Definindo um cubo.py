#Definindo variáveis 

def calcular_um_cubo(lado):
    area = lado ** 3
    perimetro = 12 * lado
    return area , perimetro

#Pedindo para o usuário inserio o valor do lado 

lado = float(input('Digite o valor do lado: '))

#Calculando a área do cubo 

area , perimetro = calcular_um_cubo(lado)

#Imprimindo o valor 

print(f'area: {area} - perimetro: {perimetro}')