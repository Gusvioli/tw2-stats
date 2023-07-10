from tw2_somar_pontos_da_tabela import somar_pontos_da_tabela
from tw2_conversor_srt_para_numero_e_limpando import conversor_srt_para_numero_e_limpando
from tw2_criar_json import criar_json
import tw2_tabela_de_pontos as tw2_tabela_de_pontos

selec = tw2_tabela_de_pontos.pegar_dados()[0]
selec_Title = tw2_tabela_de_pontos.pegar_dados()[1]

se_dados = tw2_tabela_de_pontos.separar_dados(selec, selec_Title)
criar_json(se_dados, 'data/str_tabela_de_pontos.json')

se_dados = conversor_srt_para_numero_e_limpando('data/str_tabela_de_pontos.json')
criar_json(se_dados, 'data/tabela_de_pontos.json')

somar_pontos = somar_pontos_da_tabela(se_dados)
criar_json(se_dados, 'data/soma_tabela_de_pontos.json')