#Definindo varáveis

def converte_hora(hora, minuto):
    """
    Converte a hora de 24 horas para 12 horas com A.M./P.M.

    Parâmetros:
    hora (int): Hora no formato de 24 horas.
    minuto (int): Minuto.

    Retorna:
    tuple: Hora no formato de 12 horas e indicador A.M./P.M.
    """
    if hora == 0:
        return 12, minuto, 'A'
    elif hora < 12:
        return hora, minuto, 'A'
    elif hora == 12:
        return 12, minuto, 'P'
    else:
        return hora - 12, minuto, 'P'

#Definindo variáveis 

def exibe_hora(hora, minuto, periodo):
    """
    Exibe a hora no formato de 12 horas com A.M./P.M.

    Parâmetros:
    hora (int): Hora no formato de 12 horas.
    minuto (int): Minuto.
    periodo (str): 'A' para A.M. e 'P' para P.M.
    """
    periodo_str = 'A.M.' if periodo == 'A' else 'P.M.'
    print(f"{hora}:{minuto:02d} {periodo_str}")

#Definindo Variáveis 

def main():
    while True:
        try:
            hora_24 = int(input("Digite a hora (0-23): "))
            minuto = int(input("Digite o minuto (0-59): "))
            if 0 <= hora_24 < 24 and 0 <= minuto < 60:
                hora_12, minuto, periodo = converte_hora(hora_24, minuto)
                exibe_hora(hora_12, minuto, periodo)
            else:
                print("Hora ou minuto inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
        
        repetir = input("Deseja converter outra hora? (s/n): ").strip().lower()
        if repetir != 's':
            break

if __name__ == "__main__":
    main()
