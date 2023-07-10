import requests
from parsel import Selector
import numpy as np


def pegar_dados():
    req = requests.get('https://help.tribalwars.com.br/wiki/Tabela_de_pontos')
    selector = Selector(req.text)
    selector_Title = selector.css('table tr a::attr(title)').getall()
    selector = selector.css('table tr td::text').getall()

    return selector, selector_Title


def filtar_dados(selec):
    i = [i.replace('\n', '') for i in selec]
    i2 = [i.replace('\xa0', '0') for i in i]
    array = np.array(i2[20:619])
    matriz = np.array_split(array, 30)

    return matriz


def separar_dados(selec, selec_Title):
    matriz = filtar_dados(selec)

    result_final = {}
    i = 0
    while i < 19:
        result_final[selec_Title[i]] = [matriz[i] for matriz in matriz]
        i += 1

    return result_final
