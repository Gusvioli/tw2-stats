from tw2_criar_json import criar_json
from tw2_conversor_srt_para_numero_e_limpando import conversor_srt_para_numero_e_limpando


def somar_pontos_da_tabela(dados):
    for key in dados:
        lista = dados[key]
        soma = 0
        for i in range(len(lista)):
            soma += lista[i]
            lista[i] = soma
    return dados
