import CDI
import os

NOME_CSV = 'meu_csv.csv'
NOME_IMAGEM = 'minha_imagem.png'
URL = 'https://cdi-generator.vercel.app/api'

CAMINHO_CSV = './' + NOME_CSV
EXECUCOES_MAXIMAS = 10

if os.path.exists(CAMINHO_CSV):
    for execucao in range(EXECUCOES_MAXIMAS):
        CDI.atualizar_arquivo_csv(URL, NOME_CSV)
else:
    CDI.criar_arquivo_csv(NOME_CSV)
    for execucao in range(EXECUCOES_MAXIMAS):
        CDI.atualizar_arquivo_csv(URL, NOME_CSV)

CDI.gerar_grafico(NOME_CSV, NOME_IMAGEM)
