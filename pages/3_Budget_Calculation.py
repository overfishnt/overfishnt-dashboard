import streamlit as st
import re

# Page config
st.set_page_config(
    page_title="Fishku - Budget Calculation",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("# Budget Calculation")
st.write("Estimasi pengeluaranmu ketika melaut")
with st.container():
    col1, col2 = st.columns(2)

    # Load style
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        with col1:
            # Select Jenis Kapal
            jenis_kapal = st.selectbox(
                "Jenis Kapal",
                options=[
                    "Jarak Dekat/Nearshore",
                    "Jarak Menengah/Mid-Range",
                    "Jarak Jauh/Offshore",
                ],
            )

            # Check the situation and get the distance and usage
            if jenis_kapal == "Jarak Dekat/Nearshore":
                distance = st.number_input(
                    "Jarak tempuh", step=1, min_value=0, max_value=37
                )
                penggunaan = [0.5, 2]
            if jenis_kapal == "Jarak Menengah/Mid-Range":
                distance = st.number_input(
                    "Jarak tempuh", step=1, min_value=37, max_value=370
                )
                penggunaan = [1, 4]
            if jenis_kapal == "Jarak Jauh/Offshore":
                distance = st.number_input("Jarak tempuh", step=1, min_value=370)
                penggunaan = [2, 6]

        with col2:
            solar = 6800
            st.write(
                "Harga 1 liter solar : **Rp {0}**".format(
                    re.sub(r"(?<!^)(?=(\d{3})+$)", r".", str(solar))
                ),
            )
            st.write("Jarak Tempuh : **{0} km**".format(distance))
            bensin = [distance * penggunaan[0], distance * penggunaan[1]]
            st.write(
                "Perkiraan Bensin : **{0} - {1} liter**".format(
                    float(bensin[0]), float(bensin[1])
                )
            )
            harga = [int(bensin[0] * solar), int(bensin[1] * solar)]
            st.write(
                "**Perkiraan Budget : Rp {0} - Rp {1}**".format(
                    re.sub(r"(?<!^)(?=(\d{3})+$)", r".", str(harga[0])),
                    re.sub(r"(?<!^)(?=(\d{3})+$)", r".", str(harga[1])),
                )
            )
