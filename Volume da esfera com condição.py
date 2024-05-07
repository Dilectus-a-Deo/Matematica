import math 

#Inserindo variáveis 

raio = float(input('Digite o valor do raio: '))

#Defindo fórmula 

volume = (4/3) * math.pi * (raio) ** 3

#Introduzindo condição 

if raio < 200 :
   print('O volume diminuiu')
elif raio >= 200 : 
   print('O volume sofreu um aumento moderado')  
else: 
   print('O volume sofreu um aumento alarmante')   

#Imprimindo o valor do volume 

   print(f'O volume da esfera é : {volume} litros ') 