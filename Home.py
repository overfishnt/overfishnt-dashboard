import os
from dataclasses import dataclass
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf

st.set_page_config(
    page_title="Fishku Prediction",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

MODEL_DIR = t

with st.container():

    styles: str = os.path.join('machine-learning', 'style.css')
    st.markdown("# FISHKU")
    with open('styles/style.css') as f: 
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("### Heatmap Prediction")
            st.write("Cari tahu lokasi berkumpulnya ikan")
            map_data = pd.DataFrame(
                np.random.randn(20, 2) / [50, 50] + [-8.3, 111.71],
                columns=['lat', 'lon'])

            st.map(map_data)
            st.caption("Prakiraan lokasi ikan muncul di perairan")

        with col2:
            st.write("### Rekomendasi")
            # st.subheader("Cari tahu lokasi berkumpulnya ikan")
            st.write("Ikan yang banyak muncul")
            df = pd.DataFrame({
                'Rekomendasi Tangkapan Laut': ["Tongkol", "Tengiri", "Cakalang", "Cumi", "Mujair", "Patin", "Gurame", "Nila", "Kakap", "Salmon", "Tuna"],
            })

            df

