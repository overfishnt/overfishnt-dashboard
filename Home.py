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
st.title("FISHKU")