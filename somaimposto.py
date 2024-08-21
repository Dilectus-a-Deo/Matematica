#Definindo variáveis 

def somaImposto(taxaImposto, custo):
    """
    Calcula o custo de um item incluindo o imposto sobre vendas.

    Parâmetros:
    taxaImposto (float): A taxa de imposto sobre vendas em porcentagem.
    custo (float): O custo do item antes do imposto.

    Retorna:
    float: O custo do item incluindo o imposto.
    """
    return custo + (custo * taxaImposto / 100)

# Exemplo de uso

taxa = 10  # 10%
custo_item = 100  # R$100,00
custo_com_imposto = somaImposto(taxa, custo_item)
print(f"O custo do item com imposto é: R${custo_com_imposto:.2f}")
