import streamlit as st
import requests

api_key = "mloverfishntcc"  # secret API KEY
url = "http://34.142.135.168:8000/" + api_key
st.set_page_config(
    page_title="Fishku - Contributor",
    page_icon="🐟",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# Made By Overfishn't Team.",
    },
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
    responden, identitas_kapal, pendaratan = st.columns(3)
    # Responden Column
    with responden:
        st.markdown("#### Form Responden Data")
        nama = st.text_input("Nama Responden")
        handphone = st.text_input("HP Responden")
        responsible_admin = st.text_input("Nama Data Admin")
        responsible_handphone = st.text_input("Hp Data Admin")
        data_id = st.text_input("ID Pengolah Data")
        responden_date = st.date_input("Tanggal Pencacatan")
        responden_position = st.selectbox(
            "Posisi Responden",
            options=[
                "Koperasi",
                "UMKM",
                "Pemilik Kapal",
                "Nahkoda",
                "Anak Buah Kapal",
                "Nelayan",
            ],
        )
    # Kapal Column
    with identitas_kapal:
        st.markdown("#### Form Identitas Kapal")
        no_kusuka = st.text_input("Nomor KUSUKA")
        id_sarana = st.text_input("ID Sarana")
        jenis_usaha = st.text_input("Jenis Usaha")
        no_SIPI = st.text_input("Nomor SIPI/SIKPI/BPKP")
        nama_kapal = st.text_input("Nama Kapal")
        jenis_kapal = st.text_input("Jenis Kapal")
        wilayah_ikan = st.text_input("Wilayah Penangkapan Ikan")

    # Pelabuhan Column
    with pendaratan:
        st.markdown("#### Form Data Pelabuhan")
        pelabuhan = st.text_input("Nama Pelabuhan")
        provinsi = st.text_input("Provinsi")
        kabupaten_kota = st.text_input("Kabupaten/Kota")
        kecamatan = st.text_input("Kecamatan")
        desa_kelurahan = st.text_input("Desa/Kelurahan")

    data_responden = {
        "nama_respon": nama,
        "hp_respon": handphone,
        "nama_admin": responsible_admin,
        "hp_admin": responsible_handphone,
        "data_id": data_id,
        "tanggal": str(responden_date),
        "posisi": responden_position,
    }
    data_pelabuhan = {
        "pelabuhan": pelabuhan,
        "provinsi": provinsi,
        "kota": kabupaten_kota,
        "kecamatan": kecamatan,
        "kelurahan": desa_kelurahan,
    }
    data_kapal = {
        "kusuka": no_kusuka,
        "id_sarana": id_sarana,
        "jenis_usaha": jenis_usaha,
        "SIPI": no_SIPI,
        "nama_kapal": nama_kapal,
        "jenis_kapal": jenis_kapal,
        "wilayah": wilayah_ikan,
    }

    # Check all field is filled
    if (
        pelabuhan
        and provinsi
        and kabupaten_kota
        and kecamatan
        and desa_kelurahan
        and nama
        and handphone
        and responsible_admin
        and responsible_handphone
        and data_id
        and responden_date
        and responden_position
        and no_kusuka
        and id_sarana
        and jenis_usaha
        and no_SIPI
        and nama_kapal
        and jenis_kapal
        and wilayah_ikan
    ):
        submit = st.button("Submit", type="primary", disabled=False)
    else:
        submit = st.button("Submit", type="primary", disabled=True)

    # Submit to firestore databases
    try:
        if submit:
            doc_name = "{0}_{1}_{2}".format(nama, kabupaten_kota, no_SIPI)
            requests.post(
                url + "/add",
                json={
                    "collec": "responden",
                    "doc": doc_name,
                    "data": data_responden,
                },
            )
            requests.post(
                url + "/add",
                json={
                    "collec": "pelabuhan",
                    "doc": doc_name,
                    "data": data_pelabuhan,
                },
            )
            requests.post(
                url + "/add",
                json={
                    "collec": "kapal",
                    "doc": doc_name,
                    "data": data_kapal,
                },
            )
            st.success("Data berhasil Disimpan")

    except Exception as e:
        st.error("Data tidak berhasil disimpan")


contributor_UI()
