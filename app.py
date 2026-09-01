import streamlit as st

st.set_page_config(
    page_title="AI Tutor Adaptif",
    page_icon="🤖"
)

st.title("🤖 AI Tutor Adaptif")

st.write("Selamat datang di prototype AI Tutor Adaptif.")

nama = st.text_input("Masukkan nama Anda:")

if nama:
    st.success(f"Halo, {nama}! 👋")
    st.write("Sistem siap membantu proses belajar Anda.")
