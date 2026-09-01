import streamlit as st

# =========================================================
# KONFIGURASI SALiM
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

defaults = {
    "page": "home",
    "name": "",
    "material": "Ekosistem",
    "score": 0,
    "answers": {},
    "level": "",
    "focus": "",
    "tutor_answer": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   BACKGROUND
   ===================================================== */

.stApp {
    background: #F3F6FA;
}

.main .block-container {
    max-width: 920px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* =====================================================
   TYPOGRAPHY
   ===================================================== */

h1, h2, h3 {
    color: #172033 !important;
}

p, label {
    color: #334155;
}

.small-text {
    color: #64748B;
    font-size: 14px;
}


/* =====================================================
   HERO
   ===================================================== */

.hero-box {
    background: linear-gradient(
        135deg,
        #111827,
        #1E293B 55%,
        #3730A3
    );

    border-radius: 24px;
    padding: 40px 35px;
    margin-bottom: 30px;

    box-shadow:
        0 15px 35px rgba(15, 23, 42, 0.15);
}

.hero-small {
    color: #A5B4FC;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.hero-title {
    color: #FFFFFF;
    font-size: 48px;
    font-weight: 800;
    margin-top: 8px;
    margin-bottom: 3px;
}

.hero-name {
    color: #E0E7FF;
    font-size: 19px;
    font-weight: 650;
}

.hero-description {
    color: #CBD5E1;
    font-size: 15px;
    line-height: 1.7;
    margin-top: 15px;
}


/* =====================================================
   SECTION
   ===================================================== */

.section-title {
    font-size: 25px;
    font-weight: 800;
    color: #172033;
    margin-top: 25px;
}

.section-subtitle {
    color: #64748B;
    font-size: 14px;
    margin-bottom: 20px;
}


/* =====================================================
   CARD
   ===================================================== */

.card-box {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 23px;
    margin-bottom: 18px;

    box-shadow:
        0 6px 18px rgba(15, 23, 42, 0.05);
}

.card-title {
    color: #172033;
    font-size: 18px;
    font-weight: 750;
    margin-bottom: 7px;
}

.card-text {
    color: #64748B;
    font-size: 14px;
    line-height: 1.6;
}


/* =====================================================
   MATERIAL
   ===================================================== */

.material-box {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 18px;
    padding: 20px;
    min-height: 165px;

    box-shadow:
        0 6px 18px rgba(15, 23, 42, 0.04);
}

.material-icon {
    font-size: 30px;
}

.material-name {
    color: #172033;
    font-size: 17px;
    font-weight: 750;
    margin-top: 8px;
}

.material-text {
    color: #64748B;
    font-size: 13px;
    line-height: 1.55;
    margin-top: 6px;
}


/* =====================================================
   AI BOX
   ===================================================== */

.ai-box {
    background: #EEF2FF;
    border: 1px solid #C7D2FE;
    border-radius: 18px;
    padding: 23px;
    margin: 20px 0;
}

.ai-label {
    color: #4338CA;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
}

.ai-title {
    color: #1E1B4B;
    font-size: 19px;
    font-weight: 750;
    margin-top: 6px;
}

.ai-text {
    color: #475569;
    font-size: 14px;
    line-height: 1.65;
    margin-top: 8px;
}


/* =====================================================
   QUESTION
   ===================================================== */

.question-box {
    background: #FFFFFF;
    border-left: 5px solid #4F46E5;
    border-radius: 15px;
    padding: 20px;
    margin-top: 22px;
    margin-bottom: 10px;

    box-shadow:
        0 5px 15px rgba(15, 23, 42, 0.04);
}

.question-label {
    color: #4F46E5;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
}

.question-text {
    color: #172033;
    font-size: 17px;
    font-weight: 700;
    line-height: 1.6;
    margin-top: 7px;
}


/* =====================================================
   RESULT
   ===================================================== */

.result-box {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 22px;
    padding: 32px;
    text-align: center;
    margin: 25px 0;

    box-shadow:
        0 8px 25px rgba(15, 23, 42, 0.06);
}

.result-score {
    color: #4F46E5;
    font-size: 58px;
    font-weight: 850;
}

.result-label {
    color: #64748B;
    font-size: 14px;
}


/* =====================================================
   INPUT
   ===================================================== */

div[data-baseweb="input"] {
    background: #FFFFFF;
    border-radius: 10px;
}

div[data-baseweb="select"] {
    background: #FFFFFF;
    border-radius: 10px;
}

textarea {
    background: #FFFFFF !important;
    color: #172033 !important;
}


/* =====================================================
   BUTTON
   ===================================================== */

.stButton > button {
    border-radius: 11px;
    min-height: 45px;
    font-weight: 700;
}

.stButton > button[kind="primary"] {
    background: #4F46E5;
    border-color: #4F46E5;
    color: #FFFFFF;
}

.stButton > button[kind="primary"]:hover {
    background: #4338CA;
    border-color: #4338CA;
}


/* =====================================================
   RADIO
   ===================================================== */

div[role="radiogroup"] label {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 9px 12px;
    margin-bottom: 6px;
}


/* =====================================================
   METRIC
   ===================================================== */

[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 15px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #64748B !important;
}

[data-testid="stMetricValue"] {
    color: #172033 !important;
}


/* =====================================================
   FOOTER
   ===================================================== */

.footer {
    text-align: center;
    color: #64748B;
    font-size: 12px;
    line-height: 1.7;
    margin-top: 45px;
    padding-top: 20px;
    border-top: 1px solid #E2E8F0;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

def footer():
    st.markdown(
        """
        <div class="footer">
            🧬 SALiM — Sains Adaptive Learning Machine<br>
            IPA Kelas X • Kurikulum Merdeka<br>
            Developed by Tabdulghaffur © 2026
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "home":

    st.markdown(
        """
        <div class="hero-box">
            <div class="hero-small">
                IPA KELAS X • KURIKULUM MERDEKA
            </div>
            <div class="hero-title">
                🧬 SALiM
            </div>
            <div class="hero-name">
                Sains Adaptive Learning Machine
            </div>
            <div class="hero-description">
                Platform pembelajaran adaptif yang membantu
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
        '<div class="section-subtitle">'
        'Masukkan identitas dan pilih materi pembelajaran.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card-box">
                <div class="card-title">
                    👤 Identitas Siswa
                </div>
                <div class="card-text">
                    Masukkan nama siswa sebelum memulai
                    pembelajaran.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        name = st.text_input(
            "Nama siswa",
            placeholder="Contoh: Ahmad"
        )

    with col2:

        st.markdown(
            """
            <div class="card-box">
                <div class="card-title">
                    📚 Pilih Materi
                </div>
                <div class="card-text">
                    Pilih materi IPA Kelas X yang
                    ingin dipelajari.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        material = st.selectbox(
            "Materi",
            [
                "Ekosistem",
                "Sistem Pernapasan",
                "Pencemaran Lingkungan"
            ],
            label_visibility="collapsed"
        )

    st.write("")

    if st.button(
        "🚀 Mulai Pembelajaran",
        type="primary",
        use_container_width=True
    ):

        if not name.strip():

            st.warning(
                "Silakan masukkan nama siswa terlebih dahulu."
            )

        else:

            st.session_state.name = name.strip()
            st.session_state.material = material
            st.session_state.page = "diagnostic"

            st.rerun()

    st.markdown(
        '<div class="section-title">🔬 Materi IPA Kelas X</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Materi yang tersedia dalam prototype SALiM.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            """
            <div class="material-box">
                <div class="material-icon">🌱</div>
                <div class="material-name">Ekosistem</div>
                <div class="material-text">
                    Hubungan antara makhluk hidup
                    dan lingkungan.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            """
            <div class="material-box">
                <div class="material-icon">🫁</div>
                <div class="material-name">
                    Sistem Pernapasan
                </div>
                <div class="material-text">
                    Organ dan mekanisme
                    pernapasan manusia.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        st.markdown(
            """
            <div class="material-box">
                <div class="material-icon">🌍</div>
                <div class="material-name">
                    Pencemaran
                </div>
                <div class="material-text">
                    Penyebab, dampak, dan
                    penanggulangan pencemaran.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    footer()


# =========================================================
# DIAGNOSTIC
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
        <div class="ai-box">
            <div class="ai-label">
                SALiM DIAGNOSTIC
            </div>
            <div class="ai-title">
                Mari mengetahui kemampuan awalmu.
            </div>
            <div class="ai-text">
                Jawablah tiga pertanyaan berikut dengan
                sebaik mungkin. Hasilnya akan digunakan
                untuk menentukan pembelajaran yang sesuai.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SOAL 1
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="question-box">
            <div class="question-label">
                PERTANYAAN 1 DARI 3
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
        "Jawaban pertanyaan 1",
        [
            "Konsumen",
            "Produsen",
            "Pengurai",
            "Predator"
        ],
        key="q1",
        label_visibility="collapsed"
    )

    # -----------------------------------------------------
    # SOAL 2
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="question-box">
            <div class="question-label">
                PERTANYAAN 2 DARI 3
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
        "Jawaban pertanyaan 2",
        [
            "Konsumen tingkat I",
            "Konsumen tingkat II",
            "Pengurai",
            "Predator puncak"
        ],
        key="q2",
        label_visibility="collapsed"
    )

    # -----------------------------------------------------
    # SOAL 3
    # -----------------------------------------------------

    st.markdown(
        """
        <div class="question-box">
            <div class="question-label">
                PERTANYAAN 3 DARI 3
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
        "Jawaban pertanyaan 3",
        [
            "Menghasilkan makanan",
            "Memakan semua konsumen",
            "Menguraikan sisa makhluk hidup",
            "Menghasilkan oksigen"
        ],
        key="q3",
        label_visibility="collapsed"
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

        st.session_state.answers = {
            "q1": q1,
            "q2": q2,
            "q3": q3
        }

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

        st.session_state.page = "analysis"

        st.rerun()

    footer()


# =========================================================
# ANALYSIS
# =========================================================

elif st.session_state.page == "analysis":

    st.title("📊 Analisis Kemampuan")

    st.caption(
        f"👤 {st.session_state.name}"
    )

    st.progress(
        0.50,
        text="Tahap 2 dari 4 • Analisis Kemampuan"
    )

    percentage = int(
        (st.session_state.score / 3) * 100
    )

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-score">
                {percentage}%
            </div>
            <div class="result-label">
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
            f"{st.session_state.score} / 3"
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
            "SALiM akan memprioritaskan penguatan "
            "konsep dasar sebelum masuk ke konsep "
            "yang lebih kompleks."
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

    st.markdown(
        """
        <div class="ai-box">
            <div class="ai-label">
                ADAPTIVE LEARNING
            </div>
            <div class="ai-title">
                Pembelajaran akan disesuaikan
                dengan kemampuanmu.
            </div>
            <div class="ai-text">
                Hasil tes diagnostik digunakan sebagai
                dasar untuk menentukan fokus pembelajaran.
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

    footer()


# =========================================================
# AI TUTOR
# =========================================================

elif st.session_state.page == "tutor":

    st.title("🤖 SALiM AI Tutor")

    st.caption(
        f"📚 {st.session_state.material}  •  "
        f"🎯 Level {st.session_state.level}"
    )

    st.progress(
        0.75,
        text="Tahap 3 dari 4 • Pembelajaran Adaptif"
    )

    st.markdown(
        f"""
        <div class="ai-box">
            <div class="ai-label">
                SALiM AI TUTOR
            </div>
            <div class="ai-title">
                Halo, {st.session_state.name}! 👋
            </div>
            <div class="ai-text">
                Saya akan membantu kamu memahami materi
                berdasarkan hasil tes diagnostikmu.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🎯 Fokus Pembelajaran")

    st.info(
        st.session_state.focus
    )

    st.markdown(
        """
        <div class="question-box">
            <div class="question-label">
                PERTANYAAN PEMBELAJARAN
            </div>
            <div class="question-text">
                Menurutmu, mengapa produsen sangat penting
                bagi keberlangsungan suatu ekosistem?
                Jelaskan dengan bahasamu sendiri.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    answer = st.text_area(
        "Jawabanmu",
        placeholder=(
            "Tuliskan jawaban dengan bahasamu sendiri..."
        ),
        height=150,
        label_visibility="collapsed"
    )

    if st.button(
        "💬 Kirim Jawaban",
        type="primary",
        use_container_width=True
    ):

        if not answer.strip():

            st.warning(
                "Silakan tuliskan jawaban terlebih dahulu."
            )

        else:

            st.session_state.tutor_answer = answer

            st.success(
                "Jawaban diterima!"
            )

            st.markdown(
                """
                <div class="ai-box">
                    <div class="ai-label">
                        🤖 UMPAN BALIK SALiM
                    </div>
                    <div class="ai-title">
                        Bagus! Kamu sudah mulai memahami
                        konsep ekosistem.
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

    footer()


# =========================================================
# RESULT
# =========================================================

elif st.session_state.page == "result":

    st.markdown(
        """
        <div class="hero-box">
            <div class="hero-small">
                LEARNING JOURNEY COMPLETED
            </div>
            <div class="hero-title">
                🎉 Selesai!
            </div>
            <div class="hero-name">
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

    st.progress(
        1.0,
        text="Tahap 4 dari 4 • Pembelajaran Selesai"
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

    st.markdown(
        """
        <div class="ai-box">
            <div class="ai-label">
                🧬 SALiM
            </div>
            <div class="ai-title">
                Setiap siswa memiliki perjalanan
                belajar yang berbeda.
            </div>
            <div class="ai-text">
                Prototype ini menerapkan alur dasar
                pembelajaran adaptif: diagnosis,
                analisis kemampuan, pembelajaran,
                dan rekomendasi.
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
            "focus",
            "tutor_answer"
        ]:

            if key in st.session_state:
                del st.session_state[key]

        st.session_state.page = "home"

        st.rerun()

    footer()
