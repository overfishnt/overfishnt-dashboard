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

# Heatmap input data
heatmap_input = {
    "wpp571": [
        0.474631,
        0.480707,
        0.486783,
        0.492859,
        0.498935,
        0.505011,
        0.511087,
        0.517163,
        0.523239,
    ],
    "wpp572": [
        0.09901,
        0.0977,
        0.09639,
        0.09508,
        0.09377,
        0.097118,
        0.09115,
        0.08984,
        0.08853,
    ],
    "wpp573": [
        0.156401,
        0.154167,
        0.151837,
        0.151006,
        0.148724,
        0.1468725,
        0.145021,
        0.1431695,
        0.141318,
    ],
    "wpp711": [
        0.326078,
        0.371255,
        0.411674,
        0.455265,
        0.498063,
        0.540861,
        0.583659,
        0.626457,
        0.669255,
    ],
    "wpp712": [
        0.124991,
        0.124494,
        0.131946,
        0.134098667,
        0.137576167,
        0.141053667,
        0.144531167,
        0.148008667,
        0.151486167,
    ],
    "wpp713": [
        0.119972,
        0.119811,
        0.11782,
        0.117049,
        0.115973,
        0.114897,
        0.113821,
        0.112745,
        0.111669,
    ],
    "wpp714": [
        0.10168,
        0.100565,
        0.099821,
        0.098829667,
        0.097900167,
        0.096970667,
        0.096041167,
        0.095111667,
        0.094182167,
    ],
    "wpp715": [
        0.13706,
        0.147282,
        0.146687,
        0.153303333,
        0.158116833,
        0.162930333,
        0.167743833,
        0.172557333,
        0.177370833,
    ],
    "wpp716": [
        0.128567,
        0.129666,
        0.130852,
        0.13198,
        0.1331225,
        0.134265,
        0.1354075,
        0.13655,
        0.1376925,
    ],
    "wpp717": [
        0.242139,
        0.239811,
        0.236801,
        0.234245667,
        0.231576667,
        0.228907667,
        0.226238667,
        0.223569667,
        0.220900667,
    ],
    "wpp718": [
        0.84029,
        1.188471,
        1.292007,
        1.558639667,
        1.784498167,
        2.010356667,
        2.236215167,
        2.462073667,
        2.687932167,
    ],
}


# Function to get fish recommendation
def ikan(x):
    ikan = []
    if 0.16 <= x <= 0.25:
        ikan.append("Ekor Kuning")
    if 0.2 <= x <= 0.6:
        ikan.append("Tongkol")
    if 0.09 <= x <= 1.2:
        ikan.append("Tuna")
    if 0.5 <= x <= 2.5:
        ikan.append("Tenggiri")
        ikan.append("Selar")
    if 1.5 <= x <= 2.5:
        ikan.append("Teri")
        ikan.append("Bandeng")
    if 0.67 <= x <= 7.11:
        ikan.append("Gabus")
    if 0.22 <= x <= 1.12:
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
    st.markdown("# Heatmap Prediction")
    st.write("**Perkiraan ikan** yang akan kamu dapatkan berdasarkan lokasi dan waktu.")

    # Load the style
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        # Create column
        col1, col2 = st.columns([6, 2])
        with col1:
            st.write("### Heatmap")

            # Select Area Box
            sbox = st.selectbox(
                "Pilih Area",
                options=[
                    "Selat Malaka dan Laut Andaman (WPP571)",
                    "Samudra Hindia sebelah Barat Sumatera dan Selat Sunda (WPP572)",
                    "Samudra Hindia Selatan Jawa hingga Laut Timor bagian Barat (WPP573)",
                    "Selat Karimata, Laut Natuna dan Laut Cina Selatan (WPP711)",
                    "Laut Jawa (WPP712)",
                    "Selat Makassar, Teluk Bone, Laut Flores dan Laut Bali (WPP713)",
                    "Teluk Tolo dan Laut Banda (WPP714)",
                    "Teluk Tomini, Laut Maluku hingga Teluk Berau (WPP715)",
                    "Laut Sulawesi sebelah Utara Pulau Halmahera (WPP716)",
                    "Teluk Cendrawasih dan Samudra Pasifik (WPP717)",
                    "Laut Aru, Laut Arafuru dan Laut Timur bagian Timur (WPP718)",
                ],
            )

            choose = {
                "Selat Malaka dan Laut Andaman (WPP571)": "WPP571",
                "Samudra Hindia sebelah Barat Sumatera dan Selat Sunda (WPP572)": "WPP572",
                "Samudra Hindia Selatan Jawa hingga Laut Timor bagian Barat (WPP573)": "WPP573",
                "Selat Karimata, Laut Natuna dan Laut Cina Selatan (WPP711)": "WPP711",
                "Laut Jawa (WPP712)": "WPP712",
                "Selat Makassar, Teluk Bone, Laut Flores dan Laut Bali (WPP713)": "WPP713",
                "Teluk Tolo dan Laut Banda (WPP714)": "WPP714",
                "Teluk Tomini, Laut Maluku hingga Teluk Berau (WPP715)": "WPP715",
                "Laut Sulawesi sebelah Utara Pulau Halmahera (WPP716)": "WPP716",
                "Teluk Cendrawasih dan Samudra Pasifik (WPP717)": "WPP717",
                "Laut Aru, Laut Arafuru dan Laut Timur bagian Timur (WPP718)": "WPP718",
            }

            # Data Frame
            map_data = pd.DataFrame(list(long_lat.values()), columns=["lat", "lon"])

            # Map Visualization with Pydeck
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state=pdk.ViewState(
                        latitude=long_lat[choose[sbox]][0],
                        longitude=long_lat[choose[sbox]][1],
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
            model = get_heatmap_model(choose[sbox])

            # predict with model
            res = predict_model(heatmap_input[choose[sbox].lower()], model)

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
