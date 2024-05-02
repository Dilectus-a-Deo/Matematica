import math

#Definindo a função 
def calcular_angulo(a, b, c):

#Calculando utilizando lei dos cossenos 
    coseno_angulo = (b**2 + c**2 - a**2) / (2 * b * c)

    
#Calculando o ângulo em radianos
    angulo_radianos = math.acos(coseno_angulo)

    
#Convertendo o ângulo para graus
    angulo_graus = math.degrees(angulo_radianos)
    return angulo_graus


#Lados do triângulo
lado_a = float(input('Digite o comprimento do lado a: '))
lado_b = float(input('Digite o comprimento do lado b: '))
lado_c = float(input('Digite o comprimento do lado c: '))

#Calculando os ângulos
angulo_A = calcular_angulo(lado_a, lado_b, lado_c)
angulo_B = calcular_angulo(lado_b, lado_a, lado_c)
angulo_C = calcular_angulo(lado_c, lado_a, lado_b)

#Imprimindo
print(f"Ângulo A: {angulo_A} graus")
print(f"Ângulo B: {angulo_B} graus")
print(f"Ângulo C: {angulo_C} graus")
