import streamlit as st
from models.model import *

# Page Config
st.set_page_config(
    page_title="Fishku Prediction",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Styling the page
with open("styles/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.image("https://fishku.id/assets/img/logo-fishku.png")

st.title("")
st.subheader("**Fishku**")
st.write(
    "Fishku merupakan startup e-commerce di bidang perikanan yang bertujuan untuk mempermudah kegiatan jual beli ikan dan mendeteksi kesegaran ikan menggunakan machine learning."
)
st.subheader("**Overfishn't**")
st.write(
    "Overfishn't adalah tim yang terbentuk dari Company Capstone Bangkit 2023 bertujuan membuat dashboard untuk membantu para nelayan dalam berlabuh dengan memprediksi beberapa hal yang berkaitan dengan oceanografi."
)
st.title("")
st.title("")
st.title("WPP RI")
st.write(
    "**Indonesia memiliki 11 Wilayah Pengelolaan Perikanan (WPP) yang merupakan area kegiatan perikanan, seperti: penangkapan ikan, pembudidayaan ikan, konservasi, penelitian, dan pengembangan perikanan yang meliputi perairan pedalaman, perairan kepulauan, laut teritorial, zona tambahan, dan zona ekonomi eksklusif Indonesia (Peraturan Pemerintah No.18 Tahun 2014).**"
)

