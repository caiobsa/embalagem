import streamlit as st
import pandas as pd
from io import BytesIO

# Função para gerar o arquivo Excel
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    processed_data = output.getvalue()
    return processed_data

# Inicializa o histórico no estado da sessão se ainda não estiver lá
if 'historico' not in st.session_state:
    st.session_state.historico = []

# Lista de embalagens padrão disponíveis no Brasil (exemplos)
embalagens_padrao = [
    (16, 11, 6),
    (18, 13, 9),
    (22, 16, 10),
    # ... continue adicionando embalagens
]

# Função para encontrar a embalagem adequada (substitua esta função pela sua função correta)
def encontrar_embalagem(comprimento, largura, altura, peso):
    for embalagem in embalagens_padrao:
        if embalagem[0] >= comprimento and embalagem[1] >= largura and embalagem[2] >= altura:
            return embalagem
    return None

# Estilos personalizados para campos de input quadrados
st.markdown("""
<style>
input[type="number"] {
    -webkit-appearance: none;
    margin: 0;
    width: 120px !important;
    height: 120px !important;
    font-size: 22px !important;
    text-align: center;
}
div.row-widget.stNumberInput > div {flex-direction: column;}
</style>
""", unsafe_allow_html=True)

# Layout principal
st.title('Calculadora de Embalagens para E-commerce')

with st.form(key='my_form'):
    comprimento = st.number_input('Comprimento (cm)', min_value=0, format='%d', key='comprimento')
    largura = st.number_input('Largura (cm)', min_value=0, format='%d', key='largura')
    altura = st.number_input('Altura (cm)', min_value=0, format='%d', key='altura')
    peso = st.number_input('Peso (g)', min_value=0, format='%d', key='peso')
    submit_button = st.form_submit_button(label='Calcular embalagem ideal')

if submit_button:
    embalagem = encontrar_embalagem(comprimento, largura, altura, peso)
    if embalagem:
        resultado = f'Use a embalagem: {embalagem[0]}x{embalagem[1]}x{embalagem[2]} cm'
        # Adiciona ao histórico no estado da sessão
        st.session_state.historico.append({
            "Comprimento": comprimento,
            "Largura": largura,
            "Altura": altura,
            "Peso": peso,
            "Embalagem Sugerida": f'{embalagem[0]}x{embalagem[1]}x{embalagem[2]} cm'
        })
        st.success(resultado)
    else:
        st.error('Não foi possível encontrar uma embalagem padrão adequada.')

# Barra lateral para histórico
st.sidebar.title("Histórico de Cálculos")
if st.session_state.historico:
    historico_df = pd.DataFrame(st.session_state.historico)
    st.sidebar.table(historico_df)

    # Botão para baixar o histórico em Excel
    if st.sidebar.button("Baixar histórico em Excel"):
        df_excel = pd.DataFrame(st.session_state.historico)
        excel_file = to_excel(df_excel)
        st.sidebar.download_button(label="📥 Baixar Excel",
                                   data=excel_file,
                                   file_name='historico_embalagens.xlsx')
