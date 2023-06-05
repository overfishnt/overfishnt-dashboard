import streamlit as st
import datetime


st.set_page_config(
    page_title="Fishku - Contributor",
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

st.markdown("# Jadilah Kontributor")
st.write("Mari bantu Fishku dengan menjadi kontributor. Cukup isi form dibawah ini.")

# """
# # 1. It will be input one-by-one
# # 2. Import the CSV, Excel -> Preprocessing and Save it Google Cloud
# """

@st.cache_data
def responder_responses() -> str:
    ...

@st.cache_data
def pendaratan_responses() -> str:
    ...

@st.cache_data
def identitas_kapal_responses() -> str:
    ...

def contributor_UI() -> str:
    responden, pendaratan, identitas_kapal = st.columns(3)
    try:
        with responden:
            st.markdown("#### Form Responden Data")
            with st.form("Form 1 - Responden"):
                nama = st.text_input("Nama Responden")
                handphone = st.text_input("HP Responden")
                responsible_admin = st.text_input("Nama Data Admin")
                responsible_handphone = st.text_input("Hp Data Admin")
                data_id = st.text_input("ID Pengolah Data")
                responden_date = st.text_input("Tanggal Pencacatan")
                responden_position = st.selectbox(
                    "Posisi Responden", 
                    options = ["Koperasi", "UMKM", "Pemilik Kapal", "Nahkoda", "Anak Buah Kapal", "Nelayan"]
                )
                submitted = st.form_submit_button("Submit", type = "primary")
                if submitted:
                    st.success(body = "Data berhasil disimpan", icon = "😇")
        
        with pendaratan:
            st.markdown("#### Form Data Pelabuhan/Pendaratan")
            with st.form("Form 2 - Pendaratan"):
                pelabuhan = st.text_input("Nama Pelabuhan")
                provinsi = st.text_input("Provinsi")
                kabupaten_kota = st.text_input("Kabupaten/Kota")
                kecamatan = st.text_input("Kecamatan")
                desa_kelurahan = st.text_input("Desa/Kelurahan")

                submitted = st.form_submit_button("Submit", type = "primary")
                if submitted:
                    st.success(body = "Data berhasil disimpan", icon = "😇")

        with identitas_kapal:
            st.markdown("#### Form Identitas Kapal")
            with st.form("Form 2 - Identitas Kapal"):
                nama = st.text_input("Nama Responden")
                handphone = st.text_input("HP Responden")
                responsible_admin = st.text_input("Nama Data Admin")
                responsible_handphone = st.text_input("Hp Data Admin")
                data_id = st.text_input("ID Pengolah Data")
                responden_date = st.text_input("Tanggal Pencacatan")
                responden_position = st.selectbox(
                    "Posisi Responden", 
                    options = ["Koperasi", "UMKM", "Pemilik Kapal", "Nahkoda", "Anak Buah Kapal", "Nelayan"]
                )
                submitted = st.form_submit_button("Submit", type = "primary")
                if submitted:
                    st.success(body = "Data berhasil disimpan", icon = "😇")

    except Exception as e:
        st.error("Data tidak berhasil disimpan")

    name = st.text_input('Nama', 'Jevin Arda')
    st.text_input('Domisili', 'Trenggalek')
    st.time_input('Berangkat Melaut', datetime.time(17, 00))
    st.time_input('Pulang Melaut', datetime.time(20, 00))
    st.number_input('Hasil Tangkapan Tertinggi (kg)')
    st.number_input('Hasil Tangkapan Terendah (kg)')
    st.text_area('Apa masalah yang sering anda hadapi',
                'Terlalu banyak membuang sumber daya saat proses pencarian lokasi ikan berkumpul')
    
    submitted = st.button("Submit", type = "primary")
    if submitted:
        st.success(body = "Data berhasil disimpan", icon = "😇")

    
contributor_UI()