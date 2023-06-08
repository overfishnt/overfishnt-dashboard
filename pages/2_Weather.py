import streamlit as st
import pandas as pd
from models.model import (
    get_angin_model,
    get_swh_model,
    get_presipitasi_model,
    predict_model,
)

# Page Config
st.set_page_config(
    page_title="Fishku - Weather",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to get the column for prediction
def hasilkan(res, x):
    col1, col2, col3 = st.columns(3)
    with col1:
        col1.metric(
            "Hari Ini", "{0} {1}".format(round(float(res[0]), 2), x), "0 {0}".format(x)
        )
    with col2:
        col2.metric(
            "Besok",
            "{0} {1}".format(round(float(res[1]), 2), x),
            "{0} {1}".format(round((float(res[1]) / float(res[0]) - 1) * 100, 2), x),
        )
    with col3:
        col3.metric(
            "Lusa",
            "{0} {1}".format(round(float(res[2]), 2), x),
            "{0} {1}".format(round((float(res[2]) / float(res[1]) - 1) * 100, 2), x),
        )


with st.container():
    st.markdown("# Weather and Marine Condition")
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
        ],
    )

    # Load the style
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(
            ["🌊Tinggi Gelombang", "💨Kecepatan Angin", "🌧️Presipitasi"]
        )

        with tab1:
            st.subheader("Tinggi Gelombang")

            # get model path
            model = get_swh_model(choose)
            # dummy data
            dummy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # predict with model
            res = predict_model(dummy, model)
            # load the column by calling the function above
            hasilkan(res, "ft")

            # visualize data
            chart_data = pd.DataFrame(res, columns=["Tinggi Gelombang"])
            st.line_chart(chart_data)

        with tab2:
            st.subheader("Kecepatan Angin")

            # get model path
            model = get_angin_model(choose)
            # dummy data
            dummy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # predict with model
            res = predict_model(dummy, model)
            # load the column by calling the function above
            hasilkan(res, "m/s")

            # visualize data
            chart_data = pd.DataFrame(res, columns=["Kecepatan Angin"])
            st.line_chart(chart_data)

        with tab3:
            st.header("Presipitasi")

            # get model path
            model = get_presipitasi_model(choose)
            # dummy data
            dummy = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # predict with model
            res = predict_model(dummy, model)
            # load the column by calling the function above
            hasilkan(res, "mm")

            # visualize data
            chart_data = pd.DataFrame(res, columns=["Presipitasi"])
            st.line_chart(chart_data)
