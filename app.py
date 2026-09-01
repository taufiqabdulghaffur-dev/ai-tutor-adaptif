import streamlit as st
from supabase import create_client

# =========================================================
# KONFIGURASI
# =========================================================

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# =========================================================
# HALAMAN
# =========================================================

st.set_page_config(
    page_title="AI Tutor Adaptif",
    page_icon="🤖",
    layout="centered"
)

# =========================================================
# HEADER
# =========================================================

st.title("🤖 AI Tutor Adaptif")

st.write(
    "Platform pembelajaran personal berbasis kecerdasan buatan."
)

st.divider()

# =========================================================
# DATA SISWA
# =========================================================

st.header("👤 Identitas Siswa")

student_code = st.text_input(
    "Kode Siswa",
    placeholder="Contoh: S001"
)

student_name = st.text_input(
    "Nama Siswa",
    placeholder="Masukkan nama lengkap"
)

# =========================================================
# TOMBOL MULAI
# =========================================================

if st.button("🚀 Mulai Belajar", use_container_width=True):

    # Validasi
    if not student_code or not student_name:
        st.warning(
            "Silakan masukkan kode siswa dan nama terlebih dahulu."
        )

    else:

        # Bersihkan input
        student_code = student_code.strip().upper()
        student_name = student_name.strip()

        try:

            # -------------------------------------------------
            # CEK APAKAH SISWA SUDAH TERDAFTAR
            # -------------------------------------------------

            existing = (
                supabase
                .table("students")
                .select("*")
                .eq("student_code", student_code)
                .execute()
            )

            # -------------------------------------------------
            # SISWA SUDAH ADA
            # -------------------------------------------------

            if existing.data:

                student = existing.data[0]

                # Pastikan nama sesuai database
                if student["name"].lower() != student_name.lower():

                    st.error(
                        "Kode siswa sudah terdaftar dengan nama yang berbeda."
                    )

                else:

                    st.success(
                        f"👋 Selamat datang kembali, {student['name']}!"
                    )

                    st.session_state["student_id"] = student["id"]
                    st.session_state["student_code"] = student["student_code"]
                    st.session_state["student_name"] = student["name"]

            # -------------------------------------------------
            # SISWA BARU
            # -------------------------------------------------

            else:

                new_student = {
                    "student_code": student_code,
                    "name": student_name
                }

                response = (
                    supabase
                    .table("students")
                    .insert(new_student)
                    .execute()
                )

                if response.data:

                    student = response.data[0]

                    st.success(
                        f"✅ Data {student['name']} berhasil didaftarkan!"
                    )

                    st.session_state["student_id"] = student["id"]
                    st.session_state["student_code"] = student["student_code"]
                    st.session_state["student_name"] = student["name"]

        except Exception as e:

            st.error(
                f"Terjadi kesalahan: {e}"
            )

# =========================================================
# STATUS SISWA
# =========================================================

if "student_id" in st.session_state:

    st.divider()

    st.subheader("📚 Siap Belajar")

    st.write(
        f"**Siswa:** {st.session_state['student_name']}"
    )

    st.write(
        f"**Kode:** {st.session_state['student_code']}"
    )

    st.info(
        "Tahap pembelajaran akan tersedia setelah identitas siswa berhasil."
    )
