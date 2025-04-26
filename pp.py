import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
data = pd.read_csv('sales_data.csv')

# Título e descrição
st.title('Análise de Vendas')
st.write("Este é um Data Storytelling sobre as vendas de produtos. Vamos explorar os dados para descobrir insights valiosos!")

# Filtro de categoria
categoria = st.selectbox('Escolha uma categoria:', data['Category'].unique())

# Filtro de data
inicio = st.date_input('Data de Início', min_value=data['Date_Sold'].min(), max_value=data['Date_Sold'].max())
fim = st.date_input('Data de Fim', min_value=data['Date_Sold'].min(), max_value=data['Date_Sold'].max())

# Filtrando os dados com base nos filtros de usuário
data_filtrada = data[(data['Category'] == categoria) & (data['Date_Sold'] >= str(inicio)) & (data['Date_Sold'] <= str(fim))]

# Exibindo as primeiras linhas dos dados filtrados
st.write(f"Dados filtrados para a categoria {categoria} entre {inicio} e {fim}:")
st.write(data_filtrada.head())

# Gráfico de Vendas por Categoria
st.subheader(f"Vendas totais por Categoria ({categoria})")
vendas_categoria = data_filtrada.groupby('Category')['Total_Sales'].sum()
fig, ax = plt.subplots()
vendas_categoria.plot(kind='bar', ax=ax)
plt.title(f'Vendas Totais por Categoria - {categoria}')
st.pyplot(fig)

# Exemplo de Gráfico de Tendência ao Longo do Tempo
st.subheader('Tendência de Vendas ao Longo do Tempo')
data_filtrada['Date_Sold'] = pd.to_datetime(data_filtrada['Date_Sold'])
vendas_por_data = data_filtrada.groupby('Date_Sold')['Total_Sales'].sum()

fig, ax = plt.subplots()
vendas_por_data.plot(kind='line', ax=ax)
plt.title('Vendas ao Longo do Tempo')
st.pyplot(fig)

# Conclusão
st.write("Com essas visualizações, podemos identificar padrões de vendas e ajustar nossa estratégia de marketing para maximizar os lucros!")




