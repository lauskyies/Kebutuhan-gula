import streamlit as st

# Data makanan dan gula (gram)
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

# Fungsi kebutuhan gula
def kebutuhan_gula(gender, aktivitas):
    if aktivitas == "Tidak aktif":
        return 25 if gender == "Perempuan" else 30
    elif aktivitas == "Sedang":
        return 35 if gender == "Perempuan" else 40
    else:
        return 45 if gender == "Perempuan" else 50

# Streamlit App
st.set_page_config(page_title="Kebutuhan Gula Harian", page_icon="🍬")
st.title("🍬 Aplikasi Kebutuhan Gula Harian")
st.write("Pantau konsumsi gula kamu berdasarkan aktivitas dan makanan sehari-hari.")

# 1. Profil
st.header("1. Data Diri")
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
with col2:
    aktivitas = st.selectbox("Aktivitas Harian", ["Tidak aktif", "Sedang", "Aktif"])

batas_gula = kebutuhan_gula(gender, aktivitas)
st.success(f"Batas maksimal gula harian kamu adalah **{batas_gula} gram**")

# 2. Pilih makanan
st.header("2. Makanan/Minuman yang Dikonsumsi")
pilihan = st.multiselect("Pilih yang kamu konsumsi hari ini:", daftar_makanan.keys())
total_gula = sum([daftar_makanan[x] for x in pilihan])
st.info(f"🍭 Total gula dari pilihanmu: **{total_gula} gram**")

# 3. Status Konsumsi
st.header("3. Status Konsumsi Gula")
status = ""
if total_gula < batas_gula:
    status = "✅ Aman"
    st.success("Asupan gula kamu masih dalam batas aman.")
elif total_gula == batas_gula:
    status = "⚠️ Batas Maksimal"
    st.warning("Asupan gula kamu tepat di batas maksimal.")
else:
    status = "🚨 Melebihi Batas"
    st.error("Kamu melebihi batas aman! Kurangi konsumsi gula.")

# 4. Visualisasi Sederhana
st.header("4. Visualisasi Gula Harian")
gula_data = {
    "Batas Maksimum": batas_gula,
    "Konsumsi Kamu": total_gula
}
st.bar_chart(data=gula_data)

# 5. Edukasi
st.header("5. Edukasi Singkat")
with st.expander("📘 Kenapa kita harus membatasi gula?"):
    st.markdown("""
    - Gula berlebih bisa memicu **obesitas, diabetes tipe 2, dan gangguan metabolik lainnya**.
    - Banyak makanan olahan dan minuman mengandung gula tersembunyi.
    - WHO menyarankan konsumsi gula harian maksimal 10% dari total kalori (sekitar 50g).
    """)

with st.expander("💡 Tips mengurangi konsumsi gula"):
    st.markdown("""
    - Minum air putih dibandingkan minuman manis.
    - Hindari menambahkan gula ke teh/kopi.
    - Baca label gizi sebelum membeli makanan/minuman kemasan.
    """)

