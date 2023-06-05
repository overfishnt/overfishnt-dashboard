import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Fishku - Market Demand",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# Made By Overfishn't Team."
    }
)
# hide = """<style>
#             header {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """

# st.markdown(hide, unsafe_allow_html=True)

st.markdown("# Permintaan Pasar")
with st.container():
    st.subheader("Permintaan Pasar Per Bulan Mei 2023")
    with open('styles/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        chart_data = pd.DataFrame(
            np.random.randn(30, 3),
            columns=["Gurame", "Tuna", "Cakalang"])

        st.bar_chart(chart_data)

        col1, col2 = st.columns(2)
        col1.metric('**Permintan Tertinggi**', "Tuna : 30%", "+10%")
        col2.metric('**Permintaan Terendah**', "Cakalang", "-20%")
