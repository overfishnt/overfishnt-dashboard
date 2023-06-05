import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Fishku - Fish Activity",
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

st.markdown("# Aktivitas Ikan")

with st.container():
    with open('styles/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        chart_data = pd.DataFrame(
            np.random.randn(24, 1),
            columns=["Jumlah Ikan"])

        st.line_chart(chart_data)

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Waktu Terbaik**")
            st.markdown('07.49-10.19')
            st.markdown('19.12-22.42')

        with col2:
            st.write("**Waktu Terburuk**")
            st.markdown('01.49-03.19')
            st.markdown('14.12-15.42')
