# Solicita o valor inicial investido na poupança
vi = float(input('Valor inicial: '))

# Solicita a rentabilidade mensal em porcentagem
i = float(input('Rentabilidade mensal (%): '))

# Transforma a porcentagem em valor numérico
i = i / 100

# Pergunta o número de meses que a aplicação vai ficar rendendo
m = int(input('Meses que vai deixar rendendo: '))

# Calcula o valor final (montante) usando a fórmula dos juros compostos
vf = vi * (1 + i) ** m

# Exibe o valor após o período especificado
print(f'Valor após {m} meses: R$ {vf:.2f}')