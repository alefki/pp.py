import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
@st.cache
def load_data():
    data = pd.read_csv('sales_data.csv')
    data['Date_Sold'] = pd.to_datetime(data['Date_Sold'])  # Garantir que a data seja datetime
    return data

data = load_data()

# Título e descrição
st.title('Análise de Vendas')
st.write("Este é um Data Storytelling sobre as vendas de produtos. Vamos explorar os dados para descobrir insights valiosos!")

# Filtro de categoria
categoria = st.selectbox('Escolha uma categoria:', data['Category'].unique())

# Filtro de data
inicio = st.date_input('Data de Início', min_value=data['Date_Sold'].min().date(), max_value=data['Date_Sold'].max().date())
fim = st.date_input('Data de Fim', min_value=data['Date_Sold'].min().date(), max_value=data['Date_Sold'].max().date())

# Filtrando os dados com base nos filtros de usuário
data_filtrada = data[(data['Category'] == categoria) & (data['Date_Sold'].dt.date >= inicio) & (data['Date_Sold'].dt.date <= fim)]

# Exibindo as primeiras linhas dos dados filtrados
st.write(f"Dados filtrados para a categoria **{categoria}** entre {inicio} e {fim}:")
st.write(data_filtrada.head())

# Gráfico de Vendas por Categoria
st.subheader(f"Vendas totais por Categoria ({categoria})")
vendas_categoria = data_filtrada.groupby('Category')['Total_Sales'].sum()

fig, ax = plt.subplots(figsize=(10, 6))  # Ajuste do tamanho
vendas_categoria.plot(kind='bar', ax=ax, color='skyblue')

# Definindo título e rótulos
ax.set_title(f'Vendas Totais por Categoria - {categoria}', fontsize=16)
ax.set_xlabel('Categoria', fontsize=12)
ax.set_ylabel('Total de Vendas', fontsize=12)

# Ajuste das marcas no eixo X
plt.xticks(rotation=45, ha='right')  # Rotaciona as marcas do eixo X para evitar sobreposição
plt.tight_layout()  # Ajusta o layout do gráfico
st.pyplot(fig)

# Gráfico de Tendência ao Longo do Tempo
st.subheader('Tendência de Vendas ao Longo do Tempo')

# Agrupando as vendas por data
vendas_por_data = data_filtrada.groupby('Date_Sold')['Total_Sales'].sum()

fig, ax = plt.subplots(figsize=(10, 6))  # Ajuste do tamanho
vendas_por_data.plot(kind='line', ax=ax, color='green', marker='o')

# Definindo título e rótulos
ax.set_title('Vendas ao Longo do Tempo', fontsize=16)
ax.set_xlabel('Data de Venda', fontsize=12)
ax.set_ylabel('Total de Vendas', fontsize=12)

# Ajustando as marcas no eixo X
plt.xticks(rotation=45, ha='right')  # Rotaciona as marcas do eixo X
plt.tight_layout()  # Ajuste do layout do gráfico
st.pyplot(fig)

# Conclusão
st.write("""
Com essas visualizações, podemos identificar padrões de vendas, como picos e quedas, e ajustar nossas estratégias de marketing para maximizar os lucros. Por exemplo:
- Se identificarmos que um produto tem uma queda de vendas significativa em determinado período, podemos investir em promoções ou campanhas.
- Se notarmos que as vendas são consistentes durante um mês específico, podemos planejar melhor nosso estoque e melhorar a distribuição.
""")




