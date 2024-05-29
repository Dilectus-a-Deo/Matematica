#Dados(Ele saiu de casa ás 6 horas : 52 minutos)
#Perguntas da questão (Que horas ele chegou ? e qual era a sua velocidade?)

#Inserindo variáveis 

distancia = 5
tempo = 0.37

#Calculando a velocidade  

velocidade = distancia / tempo

#Imprimindo velocidade 

print(f'o valor da velocidade foi: {velocidade} km/h')

#Somando as distâncias totais para obter o tempo

tempo_inicial = 6.52
um_kilometro = 0.324
dois_kilometros = 0.180 
tres_kilometros = 0.124

tempo_total = (um_kilometro + dois_kilometros + tres_kilometros)
tempo_de_chegada_para_o_cafe = (tempo_inicial + tempo_total)

#Imprimindo o tempo de chegada para o café

print(f'o tempo de chegada para o café foi: {tempo_de_chegada_para_o_cafe} horas')