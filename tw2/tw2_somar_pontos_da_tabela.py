from tw2_criar_json import criar_json
from tw2_conversor_srt_para_numero_e_limpando import conversor_srt_para_numero_e_limpando


dados = conversor_srt_para_numero_e_limpando('dados/tabela_de_pontos.json')

criar_json(dados)

soma_list = []
soma_list.append(dados['Edifício Principal'][0])

for i in range(1, len(dados['Edifício Principal'])):
    soma = dados['Edifício Principal'][i] + dados['Edifício Principal'][i -1]
    soma_list.append(soma)

print(soma_list)

# print(dados)
