#Definindo variáveis 

def valorPagamento(valor, dias_atraso):
    """
    Calcula o valor a ser pago por uma prestação, considerando multa e juros por atraso.

    Parâmetros:
    valor (float): Valor da prestação.
    dias_atraso (int): Número de dias em atraso.

    Retorna:
    float: Valor total a ser pago.
    """
    if dias_atraso == 0:
        return valor
    else:
        multa = valor * 0.03  # 3% de multa
        juros = valor * 0.001 * dias_atraso  # 0,1% de juros por dia de atraso
        return valor + multa + juros

#Definindo Variáveis 

def main():
    total_prestacoes = 0
    total_valor_pago = 0.0

    while True:
        valor = float(input("Digite o valor da prestação (ou 0 para sair): "))
        if valor == 0:
            break
        dias_atraso = int(input("Digite o número de dias em atraso: "))
        valor_a_pagar = valorPagamento(valor, dias_atraso)
        print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")

        total_prestacoes += 1
        total_valor_pago += valor_a_pagar

    print("\nRelatório do dia:")
    print(f"Quantidade de prestações pagas: {total_prestacoes}")
    print(f"Valor total pago: R$ {total_valor_pago:.2f}")

if __name__ == "__main__":
    main()
