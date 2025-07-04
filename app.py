import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# training a model
df = pd.read_csv('pizzas.csv')

model = LinearRegression()
x = df[['diametro']]
y = df[['preco']]
model.fit(x, y)


# home page
st.set_page_config(
    page_title="Pizza",
    page_icon="🍕",
    layout="centered"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .title {
        color: #d11141;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subheader {
        text-align: center;
        font-size: 18px;
        color: #fff;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="title">🍕 Previsão de Preço de Pizza</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Digite o diâmetro da pizza e descubra o preço estimado.</div>', unsafe_allow_html=True)


st.divider()
diametro = st.number_input("📏 Digite o diâmetro da pizza (em cm):")


if st.button("🔍 Prever Preço",):
    if diametro <= 0:
        st.warning("Digite um diâmetro válido maior que 0.")
    else:
        preco_previsto = model.predict(np.array([[diametro]]))[0][0]
        st.success(f"💰 O valor estimado da pizza com {diametro:.2f} cm é de **R${preco_previsto:.2f}**")
        st.balloons()


    
with st.expander("ℹ️ Como funciona essa previsão?"):
    st.markdown("""
    Este modelo usa **Regressão Linear** para prever o preço de uma pizza com base no seu diâmetro.
    A fórmula aprendida com os dados é da forma:
    ```
        preço = a * diâmetro + b
    ```

    Onde `a` e `b` são calculados automaticamente a partir do conjunto de dados `pizzas.csv`.
    """)

# --- Footer ---
st.markdown("---")

