import streamlit as st
from models.model import *

# Page Config
st.set_page_config(
    page_title="Fishku Prediction",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Styling pages
styles = """<style>
[data-testid="stSidebar"] {
    background-size: 200px;
    background-repeat: no-repeat;
    background-position: center 20px;
    background-color: #ffffff;
}
span.css-10trblm.e16nr0p30 {
    color: #043770;
}
</style>"""
# Implement the style
st.markdown(styles, unsafe_allow_html=True)

# FISHKU logo image
st.image("https://fishku.id/assets/img/logo-fishku.png")

st.title("")

# Brief explanation about Fishku
st.subheader("**Fishku**")
st.write(
    "Fishku merupakan startup e-commerce di bidang perikanan yang bertujuan untuk mempermudah kegiatan jual beli ikan dan mendeteksi kesegaran ikan yang berbasis machine learning. Fishku juga menyediakan fitur untuk mendeteksi kesegaran ikan dengan memasukkan gambar ikan yang akan dijual."
)
# Brief explanation about Overfisn't
st.subheader("**Overfishn't**")
st.write(
    "Overfishn't adalah tim yang terbentuk dari **Company Capstone Bangkit 2023** yang bertujuan membuat dashboard untuk membantu para nelayan dalam berlabuh dengan memprediksi beberapa hal yang berkaitan dengan oseanografi. Kami mengembangkan model berbasis machine learning untuk memprediksi beberapa hal seperti presipitasi, kecepatan angin, dan tinggi gelombang. Selain itu, kami juga mengembangkan model untuk memprediksi jenis ikan yang akan didapatkan oleh para nelayan."
)
st.title("")
st.title("")

# Brief explanation about WPP
st.title("WPP RI")
st.write(
    "**Indonesia memiliki 11 Wilayah Pengelolaan Perikanan (WPP) yang merupakan area kegiatan perikanan, seperti: penangkapan ikan, pembudidayaan ikan, konservasi, penelitian, dan pengembangan perikanan yang meliputi perairan pedalaman, perairan kepulauan, laut teritorial, zona tambahan, dan zona ekonomi eksklusif Indonesia (Peraturan Pemerintah No.18 Tahun 2014).**"
)

