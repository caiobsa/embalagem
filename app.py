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
## Guia de Tamanhos de Embalagens para E-commerce

Confira nosso guia de dimensões de embalagens especialmente projetado para negócios de e-commerce. Escolher o tamanho certo melhora a experiência do cliente e otimiza os custos de envio.

| Tamanho | Comprimento (cm) | Largura (cm) | Altura (cm) |
|---------|------------------|--------------|-------------|
| P       | 16               | 11           | 6           |
| M       | 18               | 13           | 9           |
| G       | 44               | 31           | 11          |
""", unsafe_allow_html=True)

# Seção de instruções e exemplos de utilização de embalagens
st.markdown("""
## Melhores Práticas de Embalagem para E-commerce

No mundo do e-commerce, a apresentação e segurança do produto são vitais. Além das dimensões, considere o impacto ambiental e a primeira impressão do cliente ao receber o pacote.

### Embalagem Pequena (P)

Perfeita para e-commerces especializados em:

- **Joias e Acessórios**: Use pequenas bolsas protetoras antes de embalar. Ideal para lojas online de joias. ![Imagem](LINK_DA_IMAGEM_DE_JOIAS)
- **Cosméticos**: Proteja produtos frágeis com plástico bolha. Essencial para boutiques de beleza online. ![Imagem](LINK_DA_IMAGEM_DE_COSMETICOS)
- **Brinquedos Pequenos**: Embalagens seguras garantem a satisfação do cliente em lojas de brinquedos online. ![Imagem](LINK_DA_IMAGEM_DE_BRINQUEDOS)

### Embalagem Média (M)

Recomendada para e-commerces de:

- **Livros**: Lojas online de livros podem usar envelopes acolchoados para uma proteção extra. ![Imagem](LINK_DA_IMAGEM_DE_LIVROS)
- **Eletrônicos**: Garanta a segurança de gadgets em sua loja virtual com materiais de preenchimento. ![Imagem](LINK_DA_IMAGEM_DE_ELETRONICOS)
- **Vestuário**: Lojas de moda online devem optar por sacolas plásticas ou envelopes flexíveis. ![Imagem](LINK_DA_IMAGEM_DE_VESTUARIO)

### Embalagem Grande (G)

Ideal para e-commerces de:

- **Equipamento Esportivo**: Mantenha os equipamentos intactos com plástico bolha. Ótimo para lojas de esportes online. ![Imagem](LINK_DA_IMAGEM_DE_EQUIPAMENTO)
- **Eletrodomésticos**: Para lojas de eletrodomésticos, use caixas resistentes e preencha espaços vazios. ![Imagem](LINK_DA_IMAGEM_DE_ELETRODOMESTICOS)
- **Móveis Desmontados**: Lojas de móveis online devem garantir a proteção de todas as peças. ![Imagem](LINK_DA_IMAGEM_DE_MOVEIS)

Para negócios de e-commerce, é vital verificar a política de embalagens do serviço de envio escolhido e adaptar as embalagens de acordo.
""", unsafe_allow_html=True)

# ... [Restante do código anterior permanece o mesmo]

