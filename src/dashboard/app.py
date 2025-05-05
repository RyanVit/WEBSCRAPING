# import
import streamlit as st
import pandas as pd
import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))  # Caminho do app.py
db_path = os.path.join(base_dir, '..', '..', 'data', 'mercadolivre.db')  # Caminho absoluto para o banco
db_path = os.path.normpath(db_path)  # Normaliza o caminho para Windows

# Cria conexão
conn = sqlite3.connect(db_path)

# Carregar os dados da tabela 'notebooks' em um DataFrame pandas
df = pd.read_sql_query("SELECT * FROM notebook", conn)

# Fechar a conexão com o banco de dados
conn.close()

# Título da aplicação
st.title('📊 Pesquisa de Mercado - Notebooks no Mercado Livre')

# Melhorar o layout com colunas para KPIs
st.subheader('💡 KPIs principais')
col1, col2, col3 = st.columns(3)

# KPI 1: Número total de itens
total_itens = df.shape[0]
col1.metric(label="🖥️ Total de Notebooks", value=total_itens)

# KPI 2: Número de marcas únicas
unique_brands = df['brand'].nunique()
col2.metric(label="🏷️ Marcas Únicas", value=unique_brands)

# KPI 3: Preço médio novo (em reais)
average_new_price = df['new_money'].mean()
col3.metric(label="💰 Preço Médio (R$)", value=f"{average_new_price:.2f}")

# Marcas mais frequentes
st.subheader('🏆 Marcas mais encontradas até a 10ª página')
col1, col2 = st.columns([4, 2])
top_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
st.write(top_brands)  # Tabela movida para baixo

# Preço médio por marca
st.subheader('💵 Preço médio por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_money'] > 0]
average_price_by_brand = df_non_zero_prices.groupby('brand')['new_money'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
st.write(average_price_by_brand)  # Tabela movida para baixo

# Satisfação média por marca
st.subheader('⭐ Satisfação média por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
st.write(satisfaction_by_brand)  # Tabela movida para baixo

# Marca que mais venceu em todas as categorias de gráficos
st.subheader('🏅 Marca Destaque em Todas as Categorias')

# Contagem de vitórias por marca
victories = pd.DataFrame(index=df['brand'].unique())
victories['top_frequency'] = (top_brands.index[0] == victories.index).astype(int)
victories['top_average_price'] = (average_price_by_brand.index[0] == victories.index).astype(int)
victories['top_satisfaction'] = (satisfaction_by_brand.index[0] == victories.index).astype(int)

# Soma total de vitórias
victories['total_victories'] = victories.sum(axis=1)

# Marca com mais vitórias
highlight_brand = victories['total_victories'].idxmax()

# Exibir a marca vencedora
st.write(f"A marca que mais se destacou: **{highlight_brand}**")