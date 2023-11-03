import streamlit as st

st.title('Calculadora de Embalagens para E-commerce')

# Campos para inserção das dimensões e peso do produto
comprimento = st.number_input('Comprimento do produto (cm):', min_value=0.0, format='%f')
largura = st.number_input('Largura do produto (cm):', min_value=0.0, format='%f')
altura = st.number_input('Altura do produto (cm):', min_value=0.0, format='%f')
peso = st.number_input('Peso do produto (g):', min_value=0.0, format='%f')

# Lógica simplificada para determinar o tamanho da caixa
# (Os valores aqui são exemplos, você precisará ajustar de acordo com sua lógica e estoque de caixas)
if st.button('Calcular embalagem ideal'):
    if peso <= 300:
        st.success('Use a embalagem: 16x11x6 cm ou 18x13x9 cm')
    elif peso <= 400:
        st.success('Use a embalagem: 44x31x11 cm ou envelope de segurança')
    elif peso <= 800:
        st.success('Use a embalagem: 20x14x10 cm ou 20x14x14 cm')
    elif peso <= 1000:
        st.success('Use a embalagem: 30x20x20 cm ou 30x22x22 cm')
    else:
        st.error('Produto muito pesado, consulte nossa equipe para uma solução personalizada.')

