import streamlit as st
import pandas as pd

# Configurações de estilo
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
label {font-size: 18px !important;}
</style>
""", unsafe_allow_html=True)

# Função para encontrar a embalagem adequada
def encontrar_embalagem(comprimento, largura, altura, peso):
    for embalagem in embalagens:
        if embalagem[0] >= comprimento and embalagem[1] >= largura and embalagem[2] >= altura:
            return embalagem
    return None

# Lista de embalagens padrão
embalagens = [
    (16, 11, 6),
    (18, 13, 9),
    (44, 31, 11),
    # ... Adicione mais tamanhos conforme necessário
]

if 'historico' not in st.session_state:
    st.session_state['historico'] = []

st.title('Calculadora de Embalagens para E-commerce')

with st.form(key='dimensoes_form'):
    comprimento = st.number_input('Comprimento (cm)', min_value=0, format='%d')
    largura = st.number_input('Largura (cm)', min_value=0, format='%d')
    altura = st.number_input('Altura (cm)', min_value=0, format='%d')
    peso = st.number_input('Peso (Gramas)', min_value=0, format='%d')
    submit_button = st.form_submit_button(label='Calcular embalagem ideal')

if submit_button:
    embalagem = encontrar_embalagem(comprimento, largura, altura, peso)
    if embalagem:
        resultado = f'Use a embalagem: {embalagem[0]}x{embalagem[1]}x{embalagem[2]} cm'
        st.markdown(f'<p class="big-font">{resultado}</p>', unsafe_allow_html=True)
        st.session_state['historico'].append({
            "Comprimento": comprimento,
            "Largura": largura,
            "Altura": altura,
            "Peso": peso,
            "Embalagem Sugerida": resultado
        })
    else:
        st.error('Não foi possível encontrar uma embalagem padrão adequada.')

# Histórico na barra lateral
st.sidebar.title("Histórico de Cálculos")
if st.session_state['historico']:
    historico_df = pd.DataFrame(st.session_state['historico'])
    st.sidebar.table(historico_df)
    if st.sidebar.button("Baixar histórico em CSV"):
        csv = historico_df.to_csv(index=False)
        st.sidebar.download_button(label="📥 Baixar CSV",
                                   data=csv,
                                   file_name='historico_embalagens.csv',
                                   mime='text/csv')

# ... [Parte inicial do código anterior permanece a mesma]

# Seção de definição de tamanhos de embalagem
st.markdown("""
## Definições de Tamanhos de Embalagens

| Tamanho | Comprimento (cm) | Largura (cm) | Altura (cm) |
|---------|------------------|--------------|-------------|
| P       | 16               | 11           | 6           |
| M       | 18               | 13           | 9           |
| G       | 44               | 31           | 11          |
""", unsafe_allow_html=True)

# Seção de instruções e exemplos de utilização de embalagens
st.markdown("""
## Instruções e Exemplos de Utilização de Embalagens

Ao escolher uma embalagem para o seu produto, considere não apenas as dimensões, mas também a segurança, apresentação e o impacto ambiental. 

### Embalagem Pequena (P)

Ideal para:

- **Joias e Acessórios**: Coloque-os em pequenas bolsas protetoras e depois na embalagem. ![Imagem](LINK_DA_IMAGEM_DE_JOIAS)
- **Cosméticos**: Embale produtos frágeis ou líquidos em plástico bolha. ![Imagem](LINK_DA_IMAGEM_DE_COSMETICOS)
- **Brinquedos Pequenos**: Garanta que estão bem acondicionados para evitar danos. ![Imagem](LINK_DA_IMAGEM_DE_BRINQUEDOS)

### Embalagem Média (M)

Ideal para:

- **Livros**: Envelopes acolchoados ou caixas para proteção extra. ![Imagem](LINK_DA_IMAGEM_DE_LIVROS)
- **Eletrônicos**: Caixas com materiais de preenchimento para evitar movimentos. ![Imagem](LINK_DA_IMAGEM_DE_ELETRONICOS)
- **Vestuário**: Sacolas plásticas ou envelopes flexíveis para roupas dobradas. ![Imagem](LINK_DA_IMAGEM_DE_VESTUARIO)

### Embalagem Grande (G)

Ideal para:

- **Equipamento Esportivo**: Proteja com plástico bolha ou isopor. ![Imagem](LINK_DA_IMAGEM_DE_EQUIPAMENTO)
- **Eletrodomésticos**: Use caixas resistentes e preencha espaços vazios. ![Imagem](LINK_DA_IMAGEM_DE_ELETRODOMESTICOS)
- **Móveis Desmontados**: Certifique-se de que todas as peças estejam bem acondicionadas e protegidas. ![Imagem](LINK_DA_IMAGEM_DE_MOVEIS)

Lembre-se de verificar a política de embalagens do serviço de envio escolhido e adaptar suas embalagens de acordo.
""", unsafe_allow_html=True)

# ... [Restante do código anterior permanece o mesmo]
