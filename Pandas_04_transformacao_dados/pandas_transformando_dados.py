# -*- coding: utf-8 -*-
"""Pandas_04_transformando_dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B5SKs_Nj6YzJsyIDZXCjwtSS6sCGP6jj
"""

#Projeto de precificação inteligente para hospedagem

import pandas as pd

#conhecendo os dados
dados = pd.read_json('/content/dados_hospedagem.json')
dados.head()

#normalizando o df para melhorar a visualização

dados = pd.json_normalize(dados['info_moveis'])
dados

#retirando os dados das listas

#transformando o nome das colunas em uma lista
colunas = list(dados.columns)
colunas

#usando o explode para desagrupar os dados
dados = dados.explode(colunas[3:]) #excluindo as primeiras 3 colunas
dados

#resetando os índices para reordenar os dados

dados.reset_index(inplace = True, drop=True)
dados.head()

#verificando o tipo dos dados
dados.info()

#convertando os dados numéricos
import numpy as np

#convertendo os dados e atribuindo a col ao df
dados['max_hospedes']=dados['max_hospedes'].astype(np.int64)

dados.info()

#convertendo as outras colunas

col_numericas = ['quantidade_banheiros','quantidade_quartos','quantidade_camas']

#aplicando ao df

dados[col_numericas] = dados[col_numericas].astype(np.int64)

#convertendo as colunas do tipo float
dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)

#verificando os dados
dados.info()

"""tipos de inteiros:

"""

#tratamento de numeros com string

#observando os dados
dados['preco']

#usando o método apply com lamda
dados['preco'].apply(lambda x: x.replace('$', '').replace(',','').strip()) #substitui o $ e , por vazio, o strip apaga os espaços vazios

#atribuindo a uma nova coluna
dados['preco'] = dados['preco'].apply(lambda x: x.replace('$', '').replace(',','').strip())

#aplicando o astype
dados['preco'] = dados['preco'].astype(np.float64)

dados.info()

#convertendo duas colunas junto

#verificando o df
dados[['taxa_deposito','taxa_limpeza']]

#convertendo e atribuindo os dados de duas colunas juntas

dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].applymap(lambda x: x.replace('$', '').replace(',','').strip())

#transformando as colunas
dados[['taxa_deposito','taxa_limpeza']] = dados[['taxa_deposito','taxa_limpeza']].astype(np.float64)

dados.info()

#manipulando os textos

#transformando as strings em minuscula para manipular
dados['descricao_local'] = dados['descricao_local'].str.lower()

#removendo alguns caracteres

#observando o texto
dados['descricao_local'][3169]

#substituindo os caracteres
dados['descricao_local'] = dados['descricao_local'].str.replace('[^a-zA-Z0-9\-\']', ' ', regex=True) #ignora todas as letras, os numeros, apostrofos e traço

#removendo hífen fora de palavras compostas
dados['descricao_local'] = dados['descricao_local'].str.replace('(?<!\w)-(?!\w)', ' ', regex=True) #regex que verifica se existe algum caractere antes e depois do hífen

#fazendo a tokenização de strings, transformando o texto em elementos dentro de uma lista
dados['descricao_local'] = dados['descricao_local'].str.split()
dados.head()

#tokenizando a coluna de comodidades

dados['comodidades'] = dados['comodidades'].str.replace('\{|}|\"','',regex=True) #encontra as chaves, aspas duplas

#fazendo a tokenização
dados['comodidades'] = dados['comodidades'].str.split(',')
dados.head()

