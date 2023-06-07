import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Fishku - Weather",
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

with st.container():
    st.markdown("# Weather and Marine Condition")
    with open('styles/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("Kecepatan Angin", "9 m/s", "-8%")
        col2.metric("Curah Hujan", "1 mm", "0.8 mm") #TODO

        tab1, tab2, tab3 = st.tabs(
            ["🌊Gelombang", "💨Kecepatan Angin", "〰️Pasang Surut"])

        with tab1:
            st.subheader("Gelombang")

            col1, col2 = st.columns(2)
            with col1:
                col1.metric("Gelombang", "5.2 ft", "0.3 ft")

            with col2:
                st.markdown('⏱️ Periode **6s**.')
                st.markdown("🧭 Direction **187° S**")

            chart_data = pd.DataFrame(
                np.random.randn(24, 1),
                columns=["Tinggi Gelombang"])

            st.line_chart(chart_data)

        with tab2:
            st.subheader("Kecepatan Angin")
            col1, col2 = st.columns(2)
            with col1:
                col1.metric("Kecepatan Angin", "9 m/s", "-0.9 m/s")

            with col2:
                st.markdown('⏱️ Periode **3s**.')
                st.markdown("🧭 Direction **124° SE**")

            chart_data = pd.DataFrame(
                np.random.randn(24, 1),
                columns=["Kecepatan Angin"])

            st.line_chart(chart_data)

        with tab3:
            st.header("Pasang Surut")
            chart_data = pd.DataFrame(
                np.random.randn(24, 1),
                columns=["Tinggi Gelombang"])

            st.line_chart(chart_data)

            col1, col2, col3 = st.columns(3)
            col1.metric('**Pasang Berikutnya**', "Besok",)
            col2.metric('**Pasang Sekarang**', "1.5 ft", "-0.1 ft")
            col3.metric('**Arus Pasang Surut**', "-7 in/h")

            col1, col2 = st.columns(2)
            col1.metric('**Air Surut**', "12.32 1.17 ft",)
            col2.metric('**Air Pasang**', "06.16 4.83 ft",)
