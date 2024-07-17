#Definição de um variável

def calcular_um_trinagulo(lado):
    area = lado * lado / 2
    perimetro = lado + lado + lado 
    return perimetro , area 

#Inserindo valores do lado do triângulo 

lado = float(input('Digite o valor do lado do triângulo: '))

#Calculando perímetro e a área do triângulo 

perimetro , area = calcular_um_trinagulo(lado)

#Imprimindo o valor 

print(f'area: {area} - perimetro: {perimetro}')