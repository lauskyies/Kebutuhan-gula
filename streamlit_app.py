import streamlit as st

# Fungsi menghitung batas maksimal gula harian (WHO standard)
def kebutuhan_gula(gender, usia, aktivitas):
    # Rekomendasi WHO: max 10% dari total kalori → ± 50g (200 kkal)
    if aktivitas == "Tidak aktif":
        return 25
    elif aktivitas == "Sedang":
        return 35
    else:
        return 50

st.title("🍭 Aplikasi Pemantau Kebutuhan Gula Harian")

st.write("Aplikasi ini membantu kamu mengetahui batas aman konsumsi gula harian berdasarkan profil dan aktivitasmu.")

# Input pengguna
gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
usia = st.slider("Usia", 5, 80, 25)
aktivitas = st.selectbox("Tingkat Aktivitas", ["Tidak aktif", "Sedang", "Aktif"])
asupan_gula = st.number_input("Total Asupan Gula Hari Ini (gram)", min_value=0)

# Hitung kebutuhan
batas_gula = kebutuhan_gula(gender, usia, aktivitas)

st.subheader("📊 Hasil Perhitungan")

st.write(f"👉 Batas maksimal konsumsi gula harian kamu: **{batas_gula} gram**")

if asupan_gula < batas_gula:
    st.success("✅ Asupan gula kamu masih dalam batas aman!")
elif asupan_gula == batas_gula:
    st.warning("⚠️ Asupan gula kamu tepat di batas maksimal.")
else:
    st.error("🚨 Asupan gula kamu melebihi batas aman! Kurangi konsumsi gula.")

# Edukasi
st.markdown("---")
st.subheader("📚 Edukasi Singkat")
st.write("""
- WHO menyarankan konsumsi gula <10% dari total kalori harian (idealnya 5%).
- Konsumsi gula berlebih dapat menyebabkan obesitas, diabetes tipe 2, dan kerusakan gigi.
- Sumber gula tersembunyi: teh manis, roti, saus botolan, minuman kemasan.
""")
