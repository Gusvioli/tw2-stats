# Refatoração pelo ChatGpt-3
def somar_pontos_da_tabela(dados):
    for key in dados:
        lista = dados[key]
        soma = 0
        for i in range(len(lista)):
            soma += lista[i]
            lista[i] = soma
    return dados
