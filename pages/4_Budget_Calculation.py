import streamlit as st
import pandas as pd
import numpy as np
import datetime

st.set_page_config(
    page_title="Fishku - Budget Calculation",
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

st.markdown("# Budget Calculation")
st.write("Estimasi pengeluaranmu ketika melaut")
with st.container():
    col1, col2 = st.columns([2, 1])
    with open('styles/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        with col1:
            st.time_input('Berangkat Melaut', datetime.time(17, 00))
            st.time_input('Pulang Melaut', datetime.time(20, 00))
            distance = st.number_input('Jarak Tempuh (km)')
            machine_type = st.selectbox(
                'Tipe Mesin Kapal',
                ('TDR-3000', 'JKT48', 'AK47'))

    with col2:
        with open('styles/style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
            st.write("#### Biaya")
            st.write("Berikut merupakan estimasi biaya melaut")
            st.markdown('⏱️ Waktu Melaut : **3 Jam**.')
            st.write("📏 Jarak Tempuh :", distance)
            st.write("⚙️ Tipe Mesin :", machine_type)
            st.write("⛽ Harga 1 liter solar : 20k", )

            st.write("##### Estimasi Biaya :", 20 * distance, "k")
