import streamlit as st

# =========================================================
# SALiM
# Sains Adaptive Learning Machine
# =========================================================

st.set_page_config(
    page_title="SALiM | IPA Kelas X",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="collapsed"
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

if "material" not in st.session_state:
    st.session_state.material = "Ekosistem"

if "level" not in st.session_state:
    st.session_state.level = ""

if "focus" not in st.session_state:
    st.session_state.focus = ""


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ================================
       GLOBAL
       ================================ */

    .stApp {
        background-color: #F4F7FB;
        color: #172033;
    }

    .block-container {
        max-width: 950px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Semua teks utama */
    p, label, span {
        color: #172033;
    }

    /* ================================
       HERO
       ================================ */

    .hero {
        background: linear-gradient(
            135deg,
            #111827 0%,
            #1E293B 45%,
            #3730A3 100%
        );

        padding: 42px 38px;
        border-radius: 26px;
        margin-bottom: 30px;

        box-shadow:
            0 18px 45px rgba(30, 41, 59, 0.18);
    }

    .hero-label {
        color: #A5B4FC !important;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 1.8px;
        margin-bottom: 8px;
    }

    .hero-title {
        color: #FFFFFF !important;
        font-size: 48px;
        font-weight: 800;
        line-height: 1.1;
        margin-bottom: 6px;
    }

    .hero-subtitle {
        color: #E0E7FF !important;
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 14px;
    }

    .hero-description {
        color: #CBD5E1 !important;
        font-size: 15px;
        line-height: 1.7;
        max-width: 720px;
    }

    /* ================================
       SECTION
       ================================ */

    .section-title {
        color: #172033 !important;
        font-size: 25px;
        font-weight: 800;
        margin-top: 25px;
        margin-bottom: 8px;
    }

    .section-description {
        color: #64748B !important;
        font-size: 15px;
        margin-bottom: 20px;
    }

    /* ================================
       CARD
       ================================ */

    .card {
        background-color: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.05);
        margin-bottom: 20px;
    }

    .card-title {
        color: #172033 !important;
        font-size: 19px;
        font-weight: 750;
        margin-bottom: 7px;
    }

    .card-description {
        color: #64748B !important;
        font-size: 14px;
        line-height: 1.6;
    }

    /* ================================
       MATERIAL CARD
       ================================ */

    .material-card {
        background-color: #FFFFFF;
        padding: 23px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        min-height: 170px;
        box-shadow: 0 7px 22px rgba(15, 23, 42, 0.045);
    }

    .material-icon {
        font-size: 30px;
        margin-bottom: 8px;
    }

    .material-title {
        color: #172033 !important;
        font-size: 18px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    .material-description {
        color: #64748B !important;
        font-size: 14px;
        line-height: 1.55;
    }

    /* ================================
       QUESTION
       ================================ */

    .question-card {
        background-color: #FFFFFF;
        padding: 26px;
        border-radius: 20px;
        border: 1px solid #E2E8F0;
        margin-top: 22px;
        margin-bottom: 8px;

        box-shadow:
            0 8px 25px rgba(15, 23, 42, 0.05);
    }

    .question-number {
        color: #4F46E5 !important;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .question-text {
        color: #172033 !important;
        font-size: 18px;
        font-weight: 700;
        line-height: 1.65;
    }

    /* ================================
       AI CARD
       ================================ */

    .ai-card {
        background: linear-gradient(
            135deg,
            #EEF2FF,
            #F8FAFC
        );

        padding: 27px;
        border-radius: 22px;
        border: 1px solid #C7D2FE;
        margin: 20px 0;
    }

    .ai-label {
        color: #4338CA !important;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .ai-title {
        color: #1E1B4B !important;
        font-size: 20px;
        font-weight: 750;
        line-height: 1.5;
    }

    .ai-text {
        color: #475569 !important;
        font-size: 15px;
        line-height: 1.7;
    }

    /* ================================
       RESULT
       ================================ */

    .result-card {
        background-color: #FFFFFF;
        padding: 35px;
        border-radius: 24px;
        border: 1px solid #E2E8F0;
        text-align: center;

        box-shadow:
            0 10px 30px rgba(15, 23, 42, 0.07);

        margin: 25px 0;
    }

    .score {
        color: #4F46E5 !important;
        font-size: 60px;
        font-weight: 850;
        line-height: 1;
    }

    .score-label {
        color: #64748B !important;
        font-size: 14px;
        margin-top: 8px;
    }

    /* ================================
       METRIC
       ================================ */

    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        padding: 18px;
        border-radius: 16px;
    }

    [data-testid="stMetricLabel"] {
        color: #64748B !important;
    }

    [data-testid="stMetricValue"] {
        color: #172033 !important;
    }

    /* ================================
       INPUT
       ================================ */

    div[data-baseweb="input"] {
        background-color: #FFFFFF;
        border-radius: 12px;
    }

    div[data-baseweb="select"] {
        background-color: #FFFFFF;
        border-radius: 12px;
    }

    textarea {
        background-color: #FFFFFF !important;
        color: #172033 !important;
        border-radius: 12px !important;
    }

    /* ================================
       BUTTON
       ================================ */

    .stButton > button {
        border-radius: 12px;
        min-height: 45px;
        font-weight: 700;
        border: 1px solid #CBD5E1;
        background-color: #FFFFFF;
        color: #172033;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #4F46E5;
        color: #4338CA;
        box-shadow: 0 5px 15px rgba(79, 70, 229, 0.12);
    }

    /* ================================
       RADIO
       ================================ */

    div[role="radiogroup"] label {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 10px 14px;
        margin-bottom: 7px;
    }

    /* ================================
       FOOTER
       ================================ */

    .footer {
        text-align: center;
        color: #64748B !important;
        font-size: 13px;
        line-height: 1.6;
        margin-top: 45px;
        padding-top: 20px;
        border-top: 1px solid #E2E8F0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

def show_footer():
    st.markdown(
        """
        <div class="footer">
            🧬 <b>SALiM</b> • Sains Adaptive Learning Machine<br>
            Developed by Tabdulghaffur © 2026
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "home":

    # HERO
    st.markdown(
        """
        <div class="hero">

            <div class="hero-label">
                IPA KELAS X • KURIKULUM MERDEKA
            </div>

            <div class="hero-title">
                🧬 SALiM
            </div>

            <div class="hero-subtitle">
                Sains Adaptive Learning Machine
            </div>

            <div class="hero-description">
                Sistem pembelajaran adaptif yang membantu
                siswa belajar IPA berdasarkan kemampuan awal,
                kebutuhan belajar, dan perkembangan pemahamannya.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">🚀 Mulai Pembelajaran</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Masukkan identitas dan pilih materi yang ingin dipelajari.'
        '</div>',
        unsafe_allow_html=True
    )

    # IDENTITAS
    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    👤 Identitas Siswa
                </div>

                <div class="card-description">
                    Data ini digunakan untuk mengenali
                    peserta pembelajaran.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        name = st.text_input(
            "Nama Siswa",
            placeholder="Contoh: Ahmad"
        )

    with col2:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    📚 Materi Pembelajaran
                </div>

                <div class="card-description">
                    Pilih materi IPA Kelas X yang
                    ingin dipelajari.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        material = st.selectbox(
            "Pilih Materi",
            [
                "Ekosistem",
                "Sistem Pernapasan",
                "Pencemaran Lingkungan"
            ]
        )

    st.write("")

    if st.button(
        "🚀 Mulai Belajar",
        type="primary",
        use_container_width=True
    ):

        if name.strip() == "":

            st.warning(
                "Silakan masukkan nama terlebih dahulu."
            )

        else:

            st.session_state.name = name.strip()
            st.session_state.material = material
            st.session_state.page = "diagnostic"

            st.rerun()

    # MATERI
    st.markdown(
        '<div class="section-title">🔬 Materi IPA Kelas X</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Tiga materi prototype yang tersedia pada SALiM.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="material-card">

                <div class="material-icon">
                    🌱
                </div>

                <div class="material-title">
                    Ekosistem
                </div>

                <div class="material-description">
                    Hubungan antara makhluk hidup
                    dan lingkungan dalam suatu ekosistem.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="material-card">

                <div class="material-icon">
                    🫁
                </div>

                <div class="material-title">
                    Sistem Pernapasan
                </div>

                <div class="material-description">
                    Mengenal organ, mekanisme,
                    dan proses pernapasan manusia.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="material-card">

                <div class="material-icon">
                    🌍
                </div>

                <div class="material-title">
                    Pencemaran Lingkungan
                </div>

                <div class="material-description">
                    Mengenal penyebab, dampak,
                    dan upaya mengatasi pencemaran.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    show_footer()


# =========================================================
# DIAGNOSTIC TEST
# =========================================================

elif st.session_state.page == "diagnostic":

    st.title("📝 Tes Diagnostik")

    st.caption(
        f"👤 {st.session_state.name}  •  "
        f"📚 {st.session_state.material}"
    )

    st.progress(
        0.25,
        text="Tahap 1 dari 4 • Tes Diagnostik"
    )

    st.markdown(
        """
        <div class="ai-card">

            <div class="ai-label">
                🧠 SALiM Diagnostic
            </div>

            <div class="ai-title">
                Mari mengetahui kemampuan awalmu.
            </div>

            <div class="ai-text">
                Jawablah tiga pertanyaan berikut dengan
                sebaik mungkin. Tidak perlu khawatir jika
                ada jawaban yang belum kamu ketahui.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # SOAL 1
    st.markdown(
        """
        <div class="question-card">

            <div class="question-number">
                Pertanyaan 1 dari 3
            </div>

            <div class="question-text">
                Organisme yang mampu membuat makanan
                sendiri disebut...
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    q1 = st.radio(
        "Pilih jawaban:",
        [
            "Konsumen",
            "Produsen",
            "Pengurai",
            "Predator"
        ],
        key="q1"
    )

    # SOAL 2
    st.markdown(
        """
        <div class="question-card">

            <div class="question-number">
                Pertanyaan 2 dari 3
            </div>

            <div class="question-text">
                Dalam rantai makanan, organisme yang
                mendapatkan energi langsung dari produsen
                disebut...
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    q2 = st.radio(
        "Pilih jawaban:",
        [
            "Konsumen tingkat I",
            "Konsumen tingkat II",
            "Pengurai",
            "Predator puncak"
        ],
        key="q2"
    )

    # SOAL 3
    st.markdown(
        """
        <div class="question-card">

            <div class="question-number">
                Pertanyaan 3 dari 3
            </div>

            <div class="question-text">
                Apa peran utama organisme pengurai
                dalam ekosistem?
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    q3 = st.radio(
        "Pilih jawaban:",
        [
            "Menghasilkan makanan",
            "Memakan semua konsumen",
            "Menguraikan sisa makhluk hidup",
            "Menghasilkan oksigen"
        ],
        key="q3"
    )

    st.write("")

    if st.button(
        "📊 Analisis Jawaban",
        type="primary",
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

            st.session_state.focus = (
                "Konsep dasar ekosistem"
            )

        elif score == 2:

            st.session_state.level = "Menengah"

            st.session_state.focus = (
                "Hubungan antarorganisme"
            )

        else:

            st.session_state.level = "Lanjutan"

            st.session_state.focus = (
                "Penerapan konsep ekosistem"
            )

        st.session_state.answers = {
            "q1": q1,
            "q2": q2,
            "q3": q3
        }

        st.session_state.page = "analysis"

        st.rerun()

    show_footer()


# =========================================================
# ANALYSIS
# =========================================================

elif st.session_state.page == "analysis":

    st.title("📊 Analisis Kemampuan")

    st.caption(
        f"👤 Siswa: {st.session_state.name}"
    )

    st.progress(
        0.50,
        text="Tahap 2 dari 4 • Analisis Kemampuan"
    )

    score = st.session_state.score

    percentage = int(
        (score / 3) * 100
    )

    # SCORE
    st.markdown(
        f"""
        <div class="result-card">

            <div class="score">
                {percentage}%
            </div>

            <div class="score-label">
                Skor Diagnostik
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Jawaban Benar",
            f"{score} / 3"
        )

    with col2:

        st.metric(
            "Level Awal",
            st.session_state.level
        )

    st.divider()

    st.subheader("🧠 Analisis SALiM")

    if st.session_state.level == "Dasar":

        st.warning(
            "Pemahaman dasar masih perlu diperkuat."
        )

        st.write(
            "SALiM akan mengarahkan pembelajaran "
            "pada penguatan konsep dasar."
        )

    elif st.session_state.level == "Menengah":

        st.info(
            "Sebagian besar konsep dasar sudah dikuasai."
        )

        st.write(
            "SALiM akan mengarahkan pembelajaran "
            "pada hubungan antar konsep."
        )

    else:

        st.success(
            "Pemahaman dasar sudah baik."
        )

        st.write(
            "SALiM akan mengarahkan pembelajaran "
            "pada penerapan dan pendalaman konsep."
        )

    st.subheader("🎯 Fokus Pembelajaran")

    st.info(
        st.session_state.focus
    )

    st.divider()

    st.markdown(
        """
        <div class="ai-card">

            <div class="ai-label">
                🤖 Adaptive Learning
            </div>

            <div class="ai-title">
                Pembelajaran akan disesuaikan
                dengan kemampuanmu.
            </div>

            <div class="ai-text">
                SALiM menggunakan hasil tes diagnostik
                sebagai dasar untuk menentukan arah
                pembelajaran berikutnya.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "🤖 Mulai Pembelajaran Adaptif",
        type="primary",
        use_container_width=True
    ):

        st.session_state.page = "tutor"

        st.rerun()

    show_footer()


# =========================================================
# AI TUTOR
# =========================================================

elif st.session_state.page == "tutor":

    st.title("🤖 SALiM AI Tutor")

    st.caption(
        f"📚 {st.session_state.material}  •  "
        f"🎯 Level: {st.session_state.level}"
    )

    st.progress(
        0.75,
        text="Tahap 3 dari 4 • Pembelajaran Adaptif"
    )

    st.markdown(
        f"""
        <div class="ai-card">

            <div class="ai-label">
                SALiM AI Tutor
            </div>

            <div class="ai-title">
                Halo, {st.session_state.name}! 👋
            </div>

            <div class="ai-text">
                Saya akan membantu kamu memahami materi
                berdasarkan hasil tes diagnostik yang telah
                kamu kerjakan.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🎯 Fokus Pembelajaran")

    st.info(
        st.session_state.focus
    )

    st.divider()

    st.subheader("💬 Pertanyaan dari SALiM")

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🤖 Mari berpikir lebih dalam
            </div>

            <div class="card-description">
                Menurutmu, mengapa produsen sangat penting
                bagi keberlangsungan suatu ekosistem?
                Jelaskan dengan bahasamu sendiri.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.text_area(
        "Tulis jawabanmu:",
        placeholder=(
            "Tuliskan jawaban dengan bahasamu sendiri..."
        ),
        height=150
    )

    if st.button(
        "💬 Kirim Jawaban",
        type="primary",
        use_container_width=True
    ):

        if answer.strip() == "":

            st.warning(
                "Silakan tuliskan jawaban terlebih dahulu."
            )

        else:

            st.success(
                "Jawaban diterima! 🤖"
            )

            st.markdown(
                """
                <div class="ai-card">

                    <div class="ai-label">
                        🤖 Umpan Balik SALiM
                    </div>

                    <div class="ai-title">
                        Bagus! Kamu sudah mulai
                        memahami konsep ekosistem.
                    </div>

                    <div class="ai-text">
                        Produsen merupakan sumber energi
                        awal dalam banyak rantai makanan.
                        Tumbuhan, misalnya, mengubah energi
                        cahaya menjadi energi kimia melalui
                        fotosintesis.
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.subheader(
                "💡 Pertanyaan berikutnya"
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

    show_footer()


# =========================================================
# RESULT
# =========================================================

elif st.session_state.page == "result":

    st.progress(
        1.0,
        text="Tahap 4 dari 4 • Pembelajaran Selesai"
    )

    st.markdown(
        """
        <div class="hero">

            <div class="hero-label">
                LEARNING JOURNEY COMPLETED
            </div>

            <div class="hero-title">
                🎉 Selesai!
            </div>

            <div class="hero-subtitle">
                Pembelajaran bersama SALiM telah selesai.
            </div>

            <div class="hero-description">
                Kamu telah menyelesaikan tes diagnostik
                dan sesi pembelajaran adaptif.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader(
        f"👋 {st.session_state.name}"
    )

    st.write(
        f"Materi: **{st.session_state.material}**"
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

    st.info(
        f"**Level awal:** "
        f"{st.session_state.level}"
    )

    st.info(
        f"**Materi diperkuat:** "
        f"{st.session_state.focus}"
    )

    st.success(
        "🟢 Sistem merekomendasikan siswa "
        "melanjutkan ke materi berikutnya."
    )

    st.divider()

    st.markdown(
        """
        <div class="ai-card">

            <div class="ai-label">
                🧬 SALiM
            </div>

            <div class="ai-title">
                Setiap siswa memiliki perjalanan belajar
                yang berbeda.
            </div>

            <div class="ai-text">
                Prototype ini menunjukkan konsep dasar
                pembelajaran adaptif: melakukan diagnosis,
                menganalisis kemampuan, memberikan
                pembelajaran, kemudian memberikan
                rekomendasi.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button(
        "🔄 Mulai Pembelajaran Lagi",
        type="primary",
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

    show_footer()
