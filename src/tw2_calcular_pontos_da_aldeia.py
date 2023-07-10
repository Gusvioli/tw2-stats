import json

data_dict = json.loads(open('data/soma_tabela_de_pontos.json').read())

print(data_dict['Edifício Principal'])