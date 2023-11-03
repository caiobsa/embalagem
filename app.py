import streamlit as st
import pandas as pd

# Configurações de estilo - mantidas conforme seu código original
st.markdown("""
<style>
.big-font {
    font-size:22px !important;
}
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

# Função para encontrar a embalagem adequada
def encontrar_embalagem(comprimento, largura, altura, peso):
    # Substitua por sua lógica de encontro de embalagens
    for embalagem in embalagens:
        if embalagem[0] >= comprimento and embalagem[1] >= largura and embalagem[2] >= altura:
            return embalagem
    return None

# Lista de embalagens padrão disponíveis no Brasil (exemplos)
embalagens = [
    (16, 11, 6),
    (18, 13, 9),
    (44, 31, 11),
    # ... Adicione mais tamanhos conforme necessário
]

# Inicializa o histórico no estado da sessão se ainda não estiver lá
if 'historico' not in st.session_state:
    st.session_state['historico'] = []

st.title('Calculadora de Embalagens para E-commerce')

# Campos para inserção das dimensões e peso do produto
with st.form(key='dimensoes_form'):
    comprimento = st.number_input('Comprimento (cm)', min_value=0, format='%d')
    largura = st.number_input('Largura (cm)', min_value=0, format='%d')
    altura = st.number_input('Altura (cm)', min_value=0, format='%d')
    peso = st.number_input('Peso (g)', min_value=0, format='%d')
    submit_button = st.form_submit_button(label='Calcular embalagem ideal')

if submit_button:
    embalagem = encontrar_embalagem(comprimento, largura, altura, peso)
    if embalagem:
        resultado = f'Use a embalagem: {embalagem[0]}x{embalagem[1]}x{embalagem[2]} cm'
        st.markdown(f'<p class="big-font">{resultado}</p>', unsafe_allow_html=True)
        # Adiciona ao histórico no estado da sessão
        st.session_state['historico'].append({
            "Comprimento": comprimento,
            "Largura": largura,
            "Altura": altura,
            "Peso": peso,
            "Embalagem Sugerida": resultado
        })
    else:
        st.error('Não foi possível encontrar uma embalagem padrão adequada.')

# Mostra o histórico na barra lateral
st.sidebar.title("Histórico de Cálculos")
if st.session_state['historico']:
    historico_df = pd.DataFrame(st.session_state['historico'])
    st.sidebar.table(historico_df)

    # Botão para baixar o histórico em CSV
    if st.sidebar.button("Baixar histórico em CSV"):
        csv = historico_df.to_csv(index=False)
        st.sidebar.download_button(label="📥 Baixar CSV",
                                   data=csv,
                                   file_name='historico_embalagens.csv',
                                   mime='text/csv')
