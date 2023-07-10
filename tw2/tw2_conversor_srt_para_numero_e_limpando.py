import json

def conversor_srt_para_numero_e_limpando(json_in):
    with open(json_in, 'r') as json_file:
        data_dict = json.load(json_file)

    data_dict['Edifício Principal'] = [
        int(i) for i in data_dict['Edifício Principal']
        if i != '' and i != '0']
    data_dict['Quartel'] = [
        int(i) for i in data_dict['Quartel']
        if i != '' and i != '0']
    data_dict['Estábulo'] = [
        int(i) for i in data_dict['Estábulo']
        if i != '' and i != '0']
    data_dict['Oficina'] = [
        int(i) for i in data_dict['Oficina']
        if i != '' and i != '0']
    data_dict['Igreja'] = [
        int(i) for i in data_dict['Igreja']
        if i != '' and i != '0']
    data_dict['Primeira Igreja'] = [
        int(i) for i in data_dict['Primeira Igreja']
        if i != '' and i != '0']
    data_dict['Torre de Vigia'] = [
        int(i) for i in data_dict['Torre de Vigia']
        if i != '' and i != '0']
    data_dict['Academia'] = [
        int(i) for i in data_dict['Academia']
        if i != '' and i != '0']
    data_dict['Ferreiro'] = [
        int(i) for i in data_dict['Esconderijo']
        if i != '' and i != '0']
    data_dict['Praça de Reunião'] = [
        int(i) for i in data_dict['Praça de Reunião']
        if i != '' and i != '0']
    data_dict['Estátua'] = [
        int(i) for i in data_dict['Estátua']
        if i != '' and i != '0']
    data_dict['Mercado'] = [
        int(i) for i in data_dict['Mercado']
        if i != '' and i != '0']
    data_dict['Bosque'] = [
        int(i) for i in data_dict['Bosque']
        if i != '' and i != '0']
    data_dict['Poço de Argila'] = [
        int(i) for i in data_dict['Poço de Argila']
        if i != '' and i != '0']
    data_dict['Mina de Ferro'] = [
        int(i) for i in data_dict['Mina de Ferro']
        if i != '' and i != '0']
    data_dict['Fazenda'] = [
        int(i) for i in data_dict['Fazenda']
        if i != '' and i != '0']
    data_dict['Armazém'] = [
        int(i) for i in data_dict['Armazém']
        if i != '' and i != '0']
    data_dict['Esconderijo'] = [
        int(i) for i in data_dict['Esconderijo']
        if i != '' and i != '0']
    data_dict['Muralha'] = [
        int(i) for i in data_dict['Muralha']
        if i != '' and i != '0']

    return data_dict
