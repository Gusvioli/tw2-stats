import json


def criar_json(se_dados):
    with open('dados/tabela_de_pontos.json', 'w') as json_file:
        json.dump(se_dados, json_file, ensure_ascii=False, indent=2)