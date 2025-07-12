import streamlit as st
import matplotlib.pyplot as plt

# Data makanan dan kandungan gula (gram)
daftar_makanan = {
    "Teh Manis (250 mL)": 25,
    "Susu Kental Manis (50 g)": 20,
    "Roti Tawar (2 lembar)": 5,
    "Sereal Manis (50 g)": 12,
    "Minuman Soda (330 mL)": 35,
    "Kue Basah (1 buah)": 8,
    "Permen (1 buah)": 4,
    "Es Krim (1 scoop)": 14,
    "Cokelat Batang (30 g)": 18,
    "Saus Botolan (1 sdm)": 3
}

# Fungsi kebutuhan gula (WHO guidelines)
def kebutuhan_gula(gender, aktivitas):
    if aktivitas == "Tidak aktif":
        return 25 if gender == "Perempuan" else 30
    elif aktivitas == "Sedang":
        return 35 if gender == "Perempuan" else 40
    else:  # Aktif
        return 45 if gender == "Perempuan" else 50

# UI
st.set_page_config(page_title="Kebutuhan Gula Harian", page_icon="🍭")
st.title("🍬 Aplikasi Kebutuhan Gula Harian")
st.caption("Pantau konsumsi gula kamu, yuk!")

# User profile
st.header("1. Data Diri")
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
with col2:
    aktivitas = st.selectbox("Tingkat Aktivitas", ["Tidak aktif", "Sedang", "Aktif"])

# Perhitungan kebutuhan
batas_gula = kebutuhan_gula(gender, aktivitas)
st.success(f"Batas maksimal konsumsi gula harian kamu adalah **{batas_gula} gram**")

# Input konsumsi makanan
st.header("2. Pilih Makanan/Minuman")
selected = st.multiselect("Pilih makanan/minuman yang kamu konsumsi hari ini:", list(daftar_makanan.keys()))
jumlah_gula = sum([daftar_makanan[x] for x in selected])
st.write(f"🍭 **Total gula dari makanan/minuman terpilih: {jumlah_gula} gram**")

# Perbandingan
st.header("3. Status Konsumsi")
if jumlah_gula < batas_gula:
    st.success("✅ Asupan gula kamu masih dalam batas aman.")
elif jumlah_gula == batas_gula:
    st.warning("⚠️ Asupan gula kamu pas di batas maksimal.")
else:
    st.error("🚨 Kamu melebihi batas aman! Kurangi konsumsi gula.")

# Visualisasi
st.header("4. Visualisasi Konsumsi Gula")
fig, ax = plt.subplots()
ax.bar(["Batas Maks", "Konsumsi Kamu"], [batas_gula, jumlah_gula], color=["green", "red"])
ax.set_ylabel("Gram Gula")
ax.set_ylim(0, max(batas_gula, jumlah_gula) + 20)
st.pyplot(fig)

# Edukasi
st.header("5. Edukasi Singkat 🍽️")
with st.expander("Kenapa penting membatasi gula?"):
    st.write("""
    - Konsumsi gula berlebih meningkatkan risiko **diabetes tipe 2**, **obesitas**, dan **kerusakan gigi**.
    - WHO menyarankan maksimal 10% dari total kalori harian berasal dari gula (sekitar 50g).
    - Gula tersembunyi banyak terdapat pada: minuman kemasan, saus, roti, dan sereal.
    """)
with st.expander("Tips mengurangi konsumsi gula"):
    st.write("""
    - Ganti minuman manis dengan air putih atau infused water.
    - Hindari menambahkan gula ke makanan/minuman.
    - Baca label nutrisi sebelum beli produk kemasan.
    """)

