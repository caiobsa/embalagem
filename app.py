import streamlit as st
import pandas as pd

# Configuração de estilo para aumentar a fonte
st.markdown("""
<style>
.big-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

# Título do app
st.title('Calculadora de Embalagens para E-commerce')

# Sidebar para histórico de cálculos
st.sidebar.header("Histórico de Cálculos")
historico = st.sidebar.empty()  # Placeholder para o histórico

# Dicionário para armazenar o histórico
historico_dict = {"Comprimento": [], "Largura": [], "Altura": [], "Peso": [], "Embalagem Sugerida": []}

# Lista de embalagens padrão disponíveis no Brasil (exemplos)
embalagens = [
    (16, 11, 6),
    (18, 13, 9),
    (44, 31, 11),
    (20, 14, 10),
    (20, 14, 14),
    (30, 20, 20),
    (30, 22, 22),
    # Adicione aqui mais tamanhos de embalagens conforme necessário
]

# Campos para inserção das dimensões e peso do produto
comprimento = st.number_input('Comprimento do produto (cm):', min_value=0, format='%d', key="comprimento")
largura = st.number_input('Largura do produto (cm):', min_value=0, format='%d', key="largura")
altura = st.number_input('Altura do produto (cm):', min_value=0, format='%d', key="altura")
peso = st.number_input('Peso do produto (g):', min_value=0, format='%d', key="peso")

# Função para encontrar a embalagem ideal
def encontrar_embalagem(comprimento, largura, altura, peso):
    # Aqui você pode implementar uma lógica mais complexa para escolher a embalagem com base nas dimensões e peso
    # Vamos apenas selecionar a primeira embalagem que seja maior que o produto em todas as dimensões
    for emb in embalagens:
        if emb[0] >= comprimento and emb[1] >= largura and emb[2] >= altura:
            return emb
    return None  # Caso nenhuma embalagem seja adequada

# Botão para calcular a embalagem
if st.button('Calcular embalagem ideal', key="calcular"):
    embalagem = encontrar_embalagem(comprimento, largura, altura, peso)
    if embalagem:
        resultado = f'Use a embalagem: {embalagem[0]}x{embalagem[1]}x{embalagem[2]} cm'
        st.markdown(f'<p class="big-font">{resultado}</p>', unsafe_allow_html=True)
        
        # Adicionar ao histórico
        historico_dict["Comprimento"].append(comprimento)
        historico_dict["Largura"].append(largura)
        historico_dict["Altura"].append(altura)
        historico_dict["Peso"].append(peso)
        historico_dict["Embalagem Sugerida"].append(f'{embalagem[0]}x{embalagem[1]}x{embalagem[2]} cm')
        
        # Atualiza a tabela no sidebar
        historico_df = pd.DataFrame(historico_dict)
        historico.dataframe(historico_df)
    else:
        st.markdown('<p class="big-font">Produto muito pesado ou grande, consulte nossa equipe para uma solução personalizada.</p>', unsafe_allow_html=True)

# Botão para baixar o histórico em Excel
if st.sidebar.button("Baixar histórico em Excel"):
    historico_df = pd.DataFrame(historico_dict)
    towrite = pd.ExcelWriter("historico_embalagens.xlsx")
    historico_df.to_excel(towrite, index=False)
    towrite.save()
    towrite.close()
    st.sidebar.download_button(
         label="Baixar Excel",
         data=open("historico_embalagens.xlsx", "rb"),
         file_name="historico_embalagens.xlsx",
         mime="application/vnd.ms-excel"
    )

# Este comando garante que o app não rode novamente automaticamente a cada interação
st.session_state.run_once = True
