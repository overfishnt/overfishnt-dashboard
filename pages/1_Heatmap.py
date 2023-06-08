import os
import streamlit as st
import pandas as pd
import pydeck as pdk
from models.model import get_heatmap_model, predict_model

# Page Config
st.set_page_config(
    page_title="Fishku Prediction",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to get fish recommendation
def ikan(x):
    ikan = []
    if 0.16<= x <=0.25 :
        ikan.append("Ekor Kuning")
    if 0.2<= x <= 0.6 :
        ikan.append("Tongkol")
    if 0.09<= x <= 1.2 :
        ikan.append("Tuna")
    if 0.5<= x <= 2.5 :
        ikan.append("Tenggiri")
        ikan.append("Selar")
    if 1.5<= x <= 2.5 :
        ikan.append("Teri")
        ikan.append("Bandeng")
    if 0.67<= x <= 7.11 :
        ikan.append("Gabus")
    if 0.22<= x <= 1.12 :
        ikan.append("Baronang")
    return ikan

# Longitude and Latitude for every WPP
long_lat = {
    "WPP571": [5.0, 99.25],
    "WPP572": [-4.25, 100.0],
    "WPP573": [-9.5, 112.5],
    "WPP711": [-0.25, 108.5],
    "WPP712": [-6.0, 113.0],
    "WPP713": [-7.75, 119.0],
    "WPP714": [-7.25, 127.5],
    "WPP715": [-1.5, 127.0],
    "WPP716": [1.75, 125.0],
    "WPP717": [0.0, 137.25],
    "WPP718": [-7.5, 136.5],
}

# CONTENT
with st.container():
    styles: str = os.path.join("machine-learning", "style.css")
    st.markdown("# FISHKU")

    # Load the style
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        # Create column
        col1, col2 = st.columns([6, 2])
        with col1:
            st.write("### Heatmap Prediction")
            st.write("Cari tahu lokasi berkumpulnya ikan")

            # Select Area Box
            choose = st.selectbox(
                "Select Area",
                options=[
                    "WPP571",
                    "WPP572",
                    "WPP573",
                    "WPP711",
                    "WPP712",
                    "WPP713",
                    "WPP714",
                    "WPP715",
                    "WPP716",
                    "WPP717",
                    "WPP718",
                ],
            )

            # Data Frame
            map_data = pd.DataFrame(list(long_lat.values()), columns=["lat", "lon"])

            # Map Visualization with Pydeck
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state=pdk.ViewState(
                        latitude=long_lat[choose][0],
                        longitude=long_lat[choose][1],
                        zoom=6,
                        pitch=0,
                    ),
                    layers=[
                        pdk.Layer(
                            "ScatterplotLayer",
                            data=map_data,
                            get_position="[lon, lat]",
                            get_color="[200, 0, 0, 160]",
                            get_radius=11.5**4.5,
                        ),
                    ],
                )
            )
            st.caption("Prakiraan lokasi ikan muncul di perairan")



        with col2:
            st.write("### Rekomendasi")

            # get model path 
            model = get_heatmap_model(choose)
            # dummy data
            dummy = [1,2,3,4,5,6,7,8,9]
            # predict with model
            res = predict_model(dummy, model)

            # result
            st.write("Ikan yang banyak muncul")
            df_today = pd.DataFrame(
                {
                    "Rekomendasi Hari Ini": ikan(res[0]),
                }
            )
            df_besok = pd.DataFrame(
                {
                    "Rekomendasi Besok": ikan(res[1]),
                }
            )
            df_lusa = pd.DataFrame(
                {
                    "Rekomendasi Lusa": ikan(res[2]),
                }
            )

            # styleing to make the table cleaner
            hide_first = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
            st.markdown(hide_first, unsafe_allow_html=True)

            # visualize the data
            st.table(df_today)
            st.table(df_besok)
            st.table(df_lusa)
