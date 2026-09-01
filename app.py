import streamlit as st
from supabase import create_client

# =========================
# KONFIGURASI
# =========================

st.set_page_config(
    page_title="AI Tutor Adaptif",
    page_icon="🤖"
)

# Mengambil Secrets dari Streamlit
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Membuat koneksi ke Supabase
supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
import base64
import json

token_parts = SUPABASE_KEY.split(".")

if len(token_parts) == 3:
    payload = token_parts[1]
    payload += "=" * (-len(payload) % 4)

    claims = json.loads(
        base64.urlsafe_b64decode(payload)
    )

    st.write("JWT role:", claims.get("role"))
    st.write("JWT ref:", claims.get("ref"))
else:
    st.write("Key bukan JWT")


# =========================
# TAMPILAN
# =========================

st.title("🤖 AI Tutor Adaptif")

st.write(
    "Prototype pembelajaran adaptif berbasis kecerdasan buatan."
)

st.divider()

st.subheader("👤 Data Siswa")

nama = st.text_input("Nama siswa")

student_code = st.text_input(
    "Kode siswa",
    placeholder="Contoh: S001"
)

if st.button("💾 Simpan Data Siswa"):

    if not nama or not student_code:
        st.warning("Nama dan kode siswa harus diisi.")

    else:
        try:
            data = {
                "name": nama,
                "student_code": student_code
            }

            response = supabase.table(
                "students"
            ).insert(data).execute()

            st.success(
                f"✅ Data {nama} berhasil disimpan!"
            )

        except Exception as e:
            st.error(
                f"Terjadi kesalahan: {e}"
            )
