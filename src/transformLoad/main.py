# Importações necessárias
import pandas as pd
import sqlite3
from datetime import datetime

# Caminho para o arquivo JSONL
df = pd.read_json('data/data.jsonl', lines=True)

# Configuração do pandas para exibir todas as colunas
pd.options.display.max_columns = None

# Adicionar colunas fixas
df['_source'] = "https://lista.mercadolivre.com.br/notebook"
df['_datetime'] = datetime.now()

# Tratamento de valores nulos
df['old_money'] = df['old_money'].fillna('0')
df['new_money'] = df['new_money'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['reviews_amount'] = df['reviews_amount'].fillna('(0)')

# Conversão para strings e limpeza de caracteres indesejados
df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(str).str.replace('[\(\)]', '', regex=True)

# Conversão para tipos numéricos
df['old_money'] = df['old_money'].astype(float)
df['new_money'] = df['new_money'].astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)

# Filtragem de produtos com preços dentro do intervalo desejado
df = df[
    (df['old_money'] >= 1000) & (df['old_money'] <= 10000) &
    (df['new_money'] >= 1000) & (df['new_money'] <= 10000)
]

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('data/mercadolivre.db')

# Salvando o DataFrame no banco de dados
df.to_sql('notebook', conn, if_exists='replace', index=False)

# Fechando a conexão com o banco de dados
conn.close()
