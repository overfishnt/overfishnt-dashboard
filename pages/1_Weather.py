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
        col1.metric("Temperature", "32 °C", "0.2 °C")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")

        tab1, tab2, tab3 = st.tabs(
            ["🌊Gelombang", "💨Gelombang Angin", "〰️Pasang Surut"])

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
            st.subheader("Gelombang Angin")
            col1, col2 = st.columns(2)
            with col1:
                col1.metric("Gelombang Angin", "1.5 ft", "0.1 ft")

            with col2:
                st.markdown('⏱️ Periode **3s**.')
                st.markdown("🧭 Direction **124° SE**")

            chart_data = pd.DataFrame(
                np.random.randn(24, 1),
                columns=["Gelombang Angin"])

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
