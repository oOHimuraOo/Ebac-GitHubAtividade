import os
import json
import random
from datetime import datetime

import requests
import seaborn as sns

def _gerar_data():
    date = datetime.now()
    data = datetime.strftime(date, '%Y/%m/%d')
    hora = datetime.strftime(date, '%H:%M:%S')
    timestamp = str(datetime.timestamp(date)).split('.')[0]
    info = [data,hora,timestamp]
    return info

def _retorna_dado_cdi(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as exc:
        print('Dado não encontrado, Continuando.')
        cdi = None
        return cdi
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        dado = json.loads(response.text)
        cdi = float(dado['taxa'].replace(',', '.'))
        return cdi

def criar_arquivo_csv(nome_do_arquivo:str = 'taxa-cdi.csv'):
    if os.path.exists('./' + nome_do_arquivo) == False:
        with open(file='./' + nome_do_arquivo, mode='w', encoding='utf-8') as fp:
            fp.write('data,hora,taxa\n')

def atualizar_arquivo_csv( url, nome_do_arquivo:str = 'taxa-cdi.csv'):
    mutacao = random.randrange(-3,3)
    if os.path.exists('./' + nome_do_arquivo):
        with open(file='./' + nome_do_arquivo, mode='a', encoding='utf-8') as fp:
            fp.write(f'{_gerar_data()[0]},{_gerar_data()[1]},{_retorna_dado_cdi(url) + mutacao}\n')

def gerar_grafico(nome_csv:str = 'taxa-cdi.csv', nome_imagem:str = _gerar_data()[2]):
    horas = []
    taxas = []
    with open(file='./' + nome_csv, mode='r', encoding='utf-8') as fp:
        linha = fp.readline()
        linha = fp.readline()
        while linha:
            linha_separada = linha.split(sep=',')
            hora = linha_separada[1]
            horas.append(hora)
            taxa = float(linha_separada[2])
            taxas.append(taxa)
            linha = fp.readline()
    
    grafico = sns.lineplot(x=horas, y=taxas)
    grafico.get_figure().savefig(f'{nome_imagem}.png')



