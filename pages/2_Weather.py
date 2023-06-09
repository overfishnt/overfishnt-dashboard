import streamlit as st
from models.model import (
    get_angin_model,
    get_swh_model,
    get_presipitasi_model,
    predict_model,
)

angin_input = {
    "wpp571": [
        1.252122248,
        1.533762655,
        1.728628427,
        2.165838134,
        2.376633439,
        2.876918597,
        2.539736619,
        2.353342495,
        2.119526956,
    ],
    "wpp572": [
        1.898247316,
        2.006160848,
        2.246089955,
        2.409408858,
        2.640704658,
        2.750457805,
        2.479840855,
        2.186342618,
        2.059027315,
    ],
    "wpp573": [
        7.996236389,
        8.097581983,
        8.144385069,
        8.206755769,
        8.151435994,
        7.953666709,
        7.780313443,
        7.574298704,
        7.385406416,
    ],
    "wpp711": [
        1.817128874,
        1.703042417,
        1.618366002,
        1.695586124,
        1.734313,
        1.987243439,
        2.108600191,
        2.294410161,
        2.358525007,
    ],
    "wpp712": [
        2.44585924,
        2.580304115,
        2.659401801,
        2.66340666,
        2.759816778,
        2.910675667,
        3.187155997,
        3.357350709,
        3.562723301,
    ],
    "wpp713": [
        4.399634647,
        4.0204497,
        3.870679654,
        3.585224108,
        3.319408211,
        3.190506124,
        3.219755464,
        3.083246019,
        3.181885986,
    ],
    "wpp714": [
        5.46694973,
        5.530772724,
        5.619892838,
        5.895354706,
        5.619145192,
        5.524359144,
        5.330568725,
        5.107821952,
        5.096779418,
    ],
    "wpp715": [
        2.156355016,
        2.334448014,
        2.50422316,
        2.653991387,
        2.528009333,
        2.767778187,
        2.920888645,
        3.140673045,
        3.233527635,
    ],
    "wpp716": [
        1.90711266,
        1.863839111,
        1.821472815,
        1.778729129,
        1.617106252,
        1.586047094,
        1.830957914,
        1.677833737,
        1.835075004,
    ],
    "wpp717": [
        3.234311652,
        3.044164318,
        3.197954033,
        3.230503928,
        3.374084444,
        3.262495127,
        3.084428572,
        2.893695254,
        2.76536192,
    ],
    "wpp718": [
        7.997886685,
        7.455730522,
        7.881255425,
        7.594336312,
        7.410320682,
        7.100237158,
        6.857953406,
        6.419343983,
        6.102493607,
    ],
}
presipitasi_input = {
    "wpp571": [
        0.000006,
        0.000021,
        0.000013,
        0.000004,
        0.000073,
        0.000002,
        0.000005,
        0.000007,
        0.000031,
    ],
    "wpp572": [
        0.000004,
        0.000007,
        0.000004,
        0.000005,
        0.000015,
        0.000002,
        0.000008,
        0.000011,
        0.000019,
    ],
    "wpp573": [
        0.000081,
        0.000077,
        0.000086,
        0.000092,
        0.000088,
        0.000101,
        0.000079,
        0.000085,
        0.000091,
    ],
    "wpp711": [
        0.001467,
        0.00148,
        0.00163,
        0.000091,
        0.000087,
        0.000056,
        0.000081,
        0.000066,
        0.000071,
    ],
    "wpp712": [
        0.000137,
        0.000098,
        0.000072,
        0.000089,
        0.000107,
        0.000129,
        0.000168,
        0.000096,
        0.000078,
    ],
    "wpp713": [
        0.000013,
        0.000012,
        0.000017,
        0.000021,
        0.000024,
        0.000019,
        0.000016,
        0.000021,
        0.000019,
    ],
    "wpp714": [
        0.000019,
        0.000031,
        0.000027,
        0.000018,
        0.000023,
        0.000054,
        0.000047,
        0.000033,
        0.000039,
    ],
    "wpp715": [
        0.000552,
        0.000411,
        0.000091,
        0.000081,
        0.000073,
        0.000067,
        0.000063,
        0.000078,
        0.000103,
    ],
    "wpp716": [
        0.000124,
        0.000131,
        0.000097,
        0.000087,
        0.000147,
        0.00021,
        0.00019,
        0.000091,
        0.000082,
    ],
    "wpp717": [
        0.000139,
        0.000121,
        0.000108,
        0.000098,
        0.000089,
        0.000086,
        0.000077,
        0.000074,
        0.000079,
    ],
    "wpp718": [
        0.000037,
        0.000061,
        0.000076,
        0.000089,
        0.000093,
        0.000084,
        0.000072,
        0.000068,
        0.000056,
    ],
}
swh_input = {
    "wpp571": [
        0.091431,
        0.092415,
        0.092599,
        0.092683,
        0.092867,
        0.093151,
        0.093235,
        0.093349,
        0.093003,
    ],
    "wpp572": [
        1.649723,
        1.650548,
        1.650873,
        1.651531333,
        1.652106333,
        1.652681333,
        1.653256333,
        1.653831333,
        1.654406333,
    ],
    "wpp573": [
        1.816186,
        1.823449,
        1.827731,
        1.8343123,
        1.8400848,
        1.84595089,
        1.85181698,
        1.85768307,
        1.8554916,
    ],
    "wpp711": [
        0.232578,
        0.2513734,
        0.259739,
        0.260381,
        0.264583,
        0.270437,
        0.273856,
        0.278948,
        0.283138,
    ],
    "wpp712": [
        0.325817,
        0.329494,
        0.3301974,
        0.3320591,
        0.3356978,
        0.3419572,
        0.3430494,
        0.3592373,
        0.3582373,
    ],
    "wpp713": [
        0.459474,
        0.460283,
        0.462139,
        0.4640582,
        0.4682013,
        0.4693124,
        0.470323102,
        0.471446,
        0.47156898,
    ],
    "wpp714": [
        0.802435,
        0.805812,
        0.807488,
        0.8105838,
        0.8130282,
        0.817679,
        0.820952,
        0.826594,
        0.8294965,
    ],
    "wpp715": [
        0.3667223,
        0.375937,
        0.386261,
        0.392138,
        0.40190735,
        0.4056446,
        0.41222157,
        0.41787868,
        0.41853579,
    ],
    "wpp716": [
        0.257894,
        0.265316,
        0.269457,
        0.275463967,
        0.280845467,
        0.286420557,
        0.291795647,
        0.297200737,
        0.294088267,
    ],
    "wpp717": [
        1.262414412,
        1.2618733,
        1.261253874,
        1.260284717,
        1.258858453,
        1.25332349,
        1.25129384,
        1.25023837,
        1.249238757,
    ],
    "wpp718": [
        2.0312383,
        2.0184573,
        2.0075431,
        1.994742,
        1.9574873,
        1.929423,
        1.90284374,
        1.895847,
        1.865748,
    ],
}

# Page Config
st.set_page_config(
    page_title="Fishku - Weather",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Function to get the column for prediction
def hasilkan(res, x, p=False, a=False, s=False):
    col1, col2, col3 = st.columns(3)
    with col1:
        col1.metric("Hari Ini", "{0} {1}".format(round(float(res[0]), 4), x), "0%")
        if p:
            col1.subheader(presipitasi(res[0]))
        if a:
            col1.subheader(angin(res[0]))
        if s:
            col1.subheader(swh(res[0]))
    with col2:
        col2.metric(
            "Besok",
            "{0} {1}".format(round(float(res[1]), 4), x),
            "{0}%".format(round((float(res[1]) / float(res[0]) - 1) * 100, 2)),
        )
        if p:
            col2.subheader(presipitasi(res[1]))
        if a:
            col2.subheader(angin(res[1]))
        if s:
            col2.subheader(swh(res[1]))
    with col3:
        col3.metric(
            "Lusa",
            "{0} {1}".format(round(float(res[2]), 4), x),
            "{0}%".format(round((float(res[2]) / float(res[1]) - 1) * 100, 2)),
        )
        if p:
            col3.subheader(presipitasi(res[2]))
        if a:
            col3.subheader(angin(res[2]))
        if s:
            col3.subheader(swh(res[2]))

def angin(x):
    x = x * 3.6
    if x < 1:
        return "Tenang"
    if 1 <= x <= 5:
        return "Sedikit tenang"
    if 5 < x <= 11:
        return "Sedikit hembusan angin"
    if 11 < x <= 19:
        return "Hembusan angin pelan"
    if 19 < x <= 29:
        return "Hembusan angin sedang"
    if 29 < x <= 39:
        return "Hembusan angin sejuk"
    if 39 < x <= 50:
        return "Hembusan angin kuat"
    if 50 < x <= 61:
        return "Mendekati kencang"
    if 61 < x <= 74:
        return "Kencang"
    if 74 < x <= 87:
        return "Kencang sekali"
    if 87 < x <= 101:
        return "Badai"
    if 101 < x <= 117:
        return "Badai dahsyat"
    if x > 117:
        return "Badai topan"

def presipitasi(x):
    if x < 0.02:
        return "Hujan sangat lemah"
    if 0.02 <= x < 0.05:
        return "Hujan lemah"
    if 0.05 <= x < 0.25:
        return "Hujan normal"
    if 0.25 <= x < 1.0:
        return "Hujan deras"
    if x > 1.0:
        return "Hujan sangat deras"

def swh(x):
    if x <= 1.25:
        return "Gelombang Tenang"
    if 1.25 < x <= 2.5:
        return "Gelombang Sedang"
    if 2.5 < x <= 4:
        return "Gelombang Berombak"
    if x > 4:
        return "Gelombang Tinggi"

with st.container():
    st.markdown("# Weather and Marine Condition")
    st.write("Mari lihat **kondisi cuaca dan laut** berdasarkan prediksi dari model kami.")
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
    }

    # Load the style
    with open("styles/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        tab1, tab2, tab3 = st.tabs(
            ["🌧️Presipitasi", "🌪️Kecepatan Angin", "🌊Tinggi Gelombang"]
        )

        with tab1:
            st.subheader("Presipitasi")
            # get model path
            model = get_presipitasi_model(choose[sbox])
            # predict with model
            res = predict_model(presipitasi_input[choose[sbox].lower()], model)
            # load the column by calling the function above
            hasilkan(res, "mm", p=True)

        with tab2:
            st.subheader("Kecepatan Angin")
            # get model path
            model = get_angin_model(choose[sbox])
            # predict with model
            res = predict_model(angin_input[choose[sbox].lower()], model)
            # load the column by calling the function above
            hasilkan(res, "m/s", a=True)

        with tab3:
            st.subheader("Tinggi Gelombang")
            # get model path
            model = get_swh_model(choose[sbox])
            # predict with model
            res = predict_model(swh_input[choose[sbox].lower()], model)
            # load the column by calling the function above
            hasilkan(res, "m", s=True)
