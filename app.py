import streamlit as st

# =========================================================
# KONFIGURASI
# =========================================================

st.set_page_config(
    page_title="AI Tutor Adaptif",
    page_icon="🧠",
    layout="centered"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "name" not in st.session_state:
    st.session_state.name = ""

if "score" not in st.session_state:
    st.session_state.score = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .card {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }

    .result {
        padding: 20px;
        border-radius: 15px;
        background-color: #f5f5f5;
        margin: 15px 0;
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "home":

    st.markdown(
        '<div class="main-title">🧠 Adaptive Learning AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Belajar sesuai kemampuanmu</div>',
        unsafe_allow_html=True
    )

    st.markdown("### 👤 Mulai Belajar")

    name = st.text_input(
        "Nama Siswa",
        placeholder="Masukkan nama Anda"
    )

    material = st.selectbox(
        "Pilih Materi",
        [
            "Ekosistem",
            "Sistem Pernapasan",
            "Pencemaran Lingkungan"
        ]
    )

    if st.button(
        "🚀 Mulai Belajar",
        use_container_width=True
    ):

        if name.strip() == "":
            st.warning("Silakan masukkan nama terlebih dahulu.")

        else:
            st.session_state.name = name
            st.session_state.material = material
            st.session_state.page = "diagnostic"
            st.rerun()


# =========================================================
# DIAGNOSTIC TEST
# =========================================================

elif st.session_state.page == "diagnostic":

    st.title("📝 Tes Diagnostik")

    st.write(
        f"Halo, **{st.session_state.name}**! "
        "Jawab 3 pertanyaan berikut untuk mengetahui "
        "tingkat pemahaman awalmu."
    )

    st.divider()

    # SOAL 1
    st.subheader("Pertanyaan 1 dari 3")

    q1 = st.radio(
        "Organisme yang mampu membuat makanan sendiri disebut...",
        [
            "Konsumen",
            "Produsen",
            "Pengurai",
            "Predator"
        ],
        key="q1"
    )

    st.divider()

    # SOAL 2
    st.subheader("Pertanyaan 2 dari 3")

    q2 = st.radio(
        "Dalam rantai makanan, organisme yang mendapatkan energi langsung dari produsen disebut...",
        [
            "Konsumen tingkat I",
            "Konsumen tingkat II",
            "Pengurai",
            "Predator puncak"
        ],
        key="q2"
    )

    st.divider()

    # SOAL 3
    st.subheader("Pertanyaan 3 dari 3")

    q3 = st.radio(
        "Apa peran utama organisme pengurai dalam ekosistem?",
        [
            "Menghasilkan makanan",
            "Memakan semua konsumen",
            "Menguraikan sisa makhluk hidup",
            "Menghasilkan oksigen"
        ],
        key="q3"
    )

    st.divider()

    if st.button(
        "📊 Analisis Jawaban",
        use_container_width=True
    ):

        score = 0

        if q1 == "Produsen":
            score += 1

        if q2 == "Konsumen tingkat I":
            score += 1

        if q3 == "Menguraikan sisa makhluk hidup":
            score += 1

        st.session_state.score = score

        if score <= 1:
            st.session_state.level = "Dasar"
            st.session_state.focus = "Konsep dasar ekosistem"

        elif score == 2:
            st.session_state.level = "Menengah"
            st.session_state.focus = "Hubungan antarorganisme"

        else:
            st.session_state.level = "Lanjutan"
            st.session_state.focus = "Penerapan konsep ekosistem"

        st.session_state.page = "analysis"
        st.rerun()


# =========================================================
# ANALYSIS
# =========================================================

elif st.session_state.page == "analysis":

    st.title("📊 Analisis Kemampuan")

    st.write(
        f"**Siswa:** {st.session_state.name}"
    )

    score = st.session_state.score

    percentage = int((score / 3) * 100)

    st.metric(
        "Skor Diagnostik",
        f"{percentage}%"
    )

    st.divider()

    st.subheader("🧠 Analisis AI")

    if st.session_state.level == "Dasar":

        st.warning(
            "Pemahaman dasar masih perlu diperkuat."
        )

        st.write(
            "🎯 Fokus pembelajaran:"
        )

        st.info(
            st.session_state.focus
        )

    elif st.session_state.level == "Menengah":

        st.info(
            "Sebagian besar konsep dasar sudah dikuasai."
        )

        st.write("🎯 Fokus pembelajaran:")

        st.info(
            st.session_state.focus
        )

    else:

        st.success(
            "Pemahaman dasar sudah baik."
        )

        st.write("🎯 Fokus pembelajaran:")

        st.info(
            st.session_state.focus
        )

    st.divider()

    st.write(
        "🤖 Sistem akan menyesuaikan pembelajaran "
        "berdasarkan hasil diagnostik."
    )

    if st.button(
        "🤖 Mulai Pembelajaran Adaptif",
        use_container_width=True
    ):

        st.session_state.page = "tutor"
        st.rerun()


# =========================================================
# AI TUTOR
# =========================================================

elif st.session_state.page == "tutor":

    st.title("🤖 AI Tutor")

    st.caption(
        f"Materi: {st.session_state.material}"
    )

    st.divider()

    st.success(
        f"Halo {st.session_state.name}! "
        "Saya akan menyesuaikan pembelajaran "
        "berdasarkan hasil tesmu."
    )

    st.markdown(
        f"""
### 🎯 Fokus pembelajaran

**{st.session_state.focus}**

Mari kita mulai dari pertanyaan berikut.

**Menurutmu, mengapa produsen sangat penting "
"bagi keberlangsungan suatu ekosistem?**
"""
    )

    answer = st.text_area(
        "Tulis jawabanmu:",
        placeholder="Tuliskan jawaban dengan bahasamu sendiri..."
    )

    if st.button(
        "💬 Kirim Jawaban",
        use_container_width=True
    ):

        if answer.strip() == "":
            st.warning("Silakan tuliskan jawaban terlebih dahulu.")

        else:

            st.success(
                "Jawaban diterima! 🤖"
            )

            st.write(
                "AI Tutor:"
            )

            st.info(
                "Jawabanmu sudah menunjukkan pemahaman awal. "
                "Sekarang mari kita hubungkan konsep produsen "
                "dengan aliran energi dalam ekosistem."
            )

            st.write(
                "💡 **Pertanyaan berikutnya:**"
            )

            st.write(
                "Apa yang akan terjadi pada konsumen "
                "jika jumlah produsen dalam suatu ekosistem "
                "menurun secara drastis?"
            )

    st.divider()

    if st.button(
        "🎯 Selesaikan Pembelajaran",
        use_container_width=True
    ):

        st.session_state.page = "result"
        st.rerun()


# =========================================================
# RESULT
# =========================================================

elif st.session_state.page == "result":

    st.title("🎉 Pembelajaran Selesai")

    st.write(
        f"### {st.session_state.name}"
    )

    st.divider()

    st.subheader("📈 Hasil Pembelajaran")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Pre-test",
            f"{int((st.session_state.score / 3) * 100)}%"
        )

    with col2:
        st.metric(
            "Post-test",
            "100%"
        )

    st.divider()

    st.subheader("🎯 Profil Belajar")

    st.write(
        f"**Level awal:** {st.session_state.level}"
    )

    st.write(
        f"**Materi diperkuat:** {st.session_state.focus}"
    )

    st.success(
        "🟢 Sistem merekomendasikan siswa "
        "melanjutkan ke materi berikutnya."
    )

    st.divider()

    st.info(
        "Prototype ini mensimulasikan pembelajaran "
        "adaptif. Pada versi berikutnya, bagian AI "
        "akan menggunakan model AI sungguhan."
    )

    if st.button(
        "🔄 Mulai Lagi",
        use_container_width=True
    ):

        for key in [
            "score",
            "answers",
            "level",
            "focus"
        ]:
            if key in st.session_state:
                del st.session_state[key]

        st.session_state.page = "home"
        st.rerun()
