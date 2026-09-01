import streamlit as st

# =========================================================
# CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="SALiM • AI Learning",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "page": "home",
    "name": "",
    "student_code": "",
    "material": "Ekosistem",
    "score": 0,
    "level": "",
    "focus": "",
    "q1": None,
    "q2": None,
    "q3": None,
    "tutor_started": False,
    "post_test": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(99,102,241,0.10), transparent 30%),
        radial-gradient(circle at 90% 10%, rgba(16,185,129,0.10), transparent 30%),
        #f8fafc;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1180px;
}

/* Hero */
.hero {
    padding: 55px 50px;
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        #111827 0%,
        #1e293b 50%,
        #312e81 100%
    );
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 20px 50px rgba(15,23,42,0.15);
}

.hero-small {
    color: #cbd5e1;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.hero-title {
    font-size: 44px;
    font-weight: 800;
    line-height: 1.1;
    margin-top: 10px;
    margin-bottom: 15px;
}

.hero-desc {
    color: #cbd5e1;
    font-size: 17px;
    line-height: 1.7;
    max-width: 720px;
}

/* Cards */
.card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
    margin-bottom: 20px;
}

.card-title {
    font-size: 20px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 8px;
}

.card-desc {
    color: #64748b;
    line-height: 1.6;
}

/* Material cards */
.material-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    height: 190px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
}

.material-icon {
    font-size: 34px;
    margin-bottom: 10px;
}

.material-title {
    font-size: 19px;
    font-weight: 700;
    color: #0f172a;
}

.material-text {
    color: #64748b;
    font-size: 14px;
    line-height: 1.5;
}

/* Stats */
.stat {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 22px;
    text-align: center;
}

.stat-number {
    font-size: 30px;
    font-weight: 800;
    color: #111827;
}

.stat-label {
    color: #64748b;
    font-size: 13px;
}

/* Question */
.question-box {
    background: white;
    border-radius: 20px;
    padding: 30px;
    border: 1px solid #e2e8f0;
    margin-bottom: 20px;
}

.question-number {
    color: #6366f1;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.question-text {
    font-size: 21px;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.5;
    margin-top: 10px;
}

/* AI tutor */
.ai-box {
    background: linear-gradient(
        135deg,
        #eef2ff,
        #ecfeff
    );
    border: 1px solid #c7d2fe;
    border-radius: 22px;
    padding: 28px;
    margin-bottom: 20px;
}

.ai-label {
    color: #4f46e5;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.ai-question {
    font-size: 20px;
    font-weight: 700;
    color: #1e1b4b;
    line-height: 1.6;
    margin-top: 10px;
}

/* Result */
.result-box {
    background: white;
    border-radius: 25px;
    padding: 35px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 12px 40px rgba(15,23,42,0.07);
    text-align: center;
}

.big-score {
    font-size: 60px;
    font-weight: 800;
    color: #4f46e5;
}

.small-muted {
    color: #64748b;
}

/* Buttons */
.stButton > button {
    border-radius: 12px;
    min-height: 46px;
    font-weight: 700;
    border: none;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">Kurikulum Merdeka • IPA Kelas X</div>
        <div class="hero-title">
            🧬 SALiM<br>
            Science Adaptive Learning Machine
        </div>
        <div class="hero-desc">
            Temukan cara belajar yang sesuai dengan kemampuanmu.
            SALiM menganalisis pemahaman awal dan membantu kamu
            belajar secara bertahap melalui pengalaman belajar yang personal.
        </div>
        <div class="hero-desc">
            Developed by Tabdulghaffur
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Mulai Perjalanan Belajarmu")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.markdown("""
        <div class="card">
            <div class="card-title">👤 Identitas Siswa</div>
            <div class="card-desc">
                Masukkan identitas untuk memulai pembelajaran.
            </div>
        </div>
        """, unsafe_allow_html=True)

        name = st.text_input(
            "Nama siswa",
            placeholder="Contoh: Ahmad"
        )

        student_code = st.text_input(
            "Kode siswa",
            placeholder="Contoh: S001"
        )

    with col2:

        st.markdown("""
        <div class="card">
            <div class="card-title">📚 Pilih Materi IPA</div>
            <div class="card-desc">
                Pilih salah satu topik untuk memulai tes diagnostik.
            </div>
        </div>
        """, unsafe_allow_html=True)

        material = st.selectbox(
            "Materi",
            [
                "Ekosistem",
                "Keanekaragaman Hayati",
                "Perubahan Lingkungan",
                "Virus",
                "Bakteri"
            ]
        )

        st.write("")

        if st.button(
            "🚀 Mulai Pembelajaran",
            use_container_width=True
        ):

            if not name.strip():
                st.warning("Masukkan nama siswa terlebih dahulu.")

            elif not student_code.strip():
                st.warning("Masukkan kode siswa terlebih dahulu.")

            else:

                st.session_state.name = name.strip()
                st.session_state.student_code = student_code.strip().upper()
                st.session_state.material = material
                st.session_state.page = "diagnostic"

                st.rerun()

    st.markdown("---")

    st.markdown("## 🔬 Topik IPA Kelas X")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="material-card">
            <div class="material-icon">🌱</div>
            <div class="material-title">Ekosistem</div>
            <div class="material-text">
                Memahami hubungan antara makhluk hidup
                dan lingkungan dalam suatu ekosistem.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="material-card">
            <div class="material-icon">🧬</div>
            <div class="material-title">Keanekaragaman Hayati</div>
            <div class="material-text">
                Mengenal tingkat keanekaragaman dan
                pentingnya menjaga biodiversitas.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="material-card">
            <div class="material-icon">🌍</div>
            <div class="material-title">Perubahan Lingkungan</div>
            <div class="material-text">
                Menganalisis penyebab dan dampak perubahan
                lingkungan serta upaya penanggulangannya.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="stat">
            <div class="stat-number">5</div>
            <div class="stat-label">Topik Pembelajaran</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stat">
            <div class="stat-number">AI</div>
            <div class="stat-label">Pembelajaran Adaptif</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="stat">
            <div class="stat-number">∞</div>
            <div class="stat-label">Jalur Belajar Personal</div>
        </div>
        """, unsafe_allow_html=True)


# =========================================================
# DIAGNOSTIC TEST
# =========================================================

elif st.session_state.page == "diagnostic":

    st.title("🧠 Tes Diagnostik")

    st.caption(
        f"{st.session_state.name} • "
        f"{st.session_state.material}"
    )

    st.progress(0.33)

    st.markdown("""
    <div class="card">
        <div class="card-title">
            Mengapa ada tes diagnostik?
        </div>
        <div class="card-desc">
            Tes ini bukan untuk menentukan nilai rapor.
            Sistem menggunakannya untuk mengetahui konsep
            mana yang sudah kamu pahami dan mana yang perlu diperkuat.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # QUESTION 1

    st.markdown("""
    <div class="question-box">
        <div class="question-number">Pertanyaan 01 • Komponen Ekosistem</div>
        <div class="question-text">
            Organisme yang mampu membuat makanan sendiri
            melalui proses fotosintesis disebut...
        </div>
    </div>
    """, unsafe_allow_html=True)

    q1 = st.radio(
        "Pilih jawaban:",
        [
            "Konsumen",
            "Produsen",
            "Pengurai",
            "Detritivor"
        ],
        key="q1_radio"
    )

    # QUESTION 2

    st.markdown("""
    <div class="question-box">
        <div class="question-number">Pertanyaan 02 • Aliran Energi</div>
        <div class="question-text">
            Perhatikan rantai makanan berikut:
            Rumput → Belalang → Katak → Ular.
            Organisme yang memperoleh energi langsung
            dari rumput adalah...
        </div>
    </div>
    """, unsafe_allow_html=True)

    q2 = st.radio(
        "Pilih jawaban:",
        [
            "Belalang",
            "Katak",
            "Ular",
            "Pengurai"
        ],
        key="q2_radio"
    )

    # QUESTION 3

    st.markdown("""
    <div class="question-box">
        <div class="question-number">Pertanyaan 03 • Dekomposer</div>
        <div class="question-text">
            Apa fungsi utama bakteri dan jamur sebagai
            organisme pengurai dalam ekosistem?
        </div>
    </div>
    """, unsafe_allow_html=True)

    q3 = st.radio(
        "Pilih jawaban:",
        [
            "Menghasilkan energi matahari",
            "Menghasilkan makanan bagi produsen",
            "Menguraikan sisa organisme",
            "Menghentikan rantai makanan"
        ],
        key="q3_radio"
    )

    st.write("")

    if st.button(
        "📊 Analisis Pemahaman Saya",
        use_container_width=True
    ):

        score = 0

        if q1 == "Produsen":
            score += 1

        if q2 == "Belalang":
            score += 1

        if q3 == "Menguraikan sisa organisme":
            score += 1

        st.session_state.score = score

        if score == 0:
            st.session_state.level = "Pemula"
            st.session_state.focus = "Konsep dasar ekosistem"

        elif score == 1:
            st.session_state.level = "Dasar"
            st.session_state.focus = "Komponen dan hubungan dalam ekosistem"

        elif score == 2:
            st.session_state.level = "Menengah"
            st.session_state.focus = "Aliran energi dan hubungan antarorganisme"

        else:
            st.session_state.level = "Mahir"
            st.session_state.focus = "Penerapan konsep ekosistem"

        st.session_state.page = "analysis"

        st.rerun()


# =========================================================
# ANALYSIS
# =========================================================

elif st.session_state.page == "analysis":

    st.title("📊 Profil Pemahaman")

    percentage = int(
        (st.session_state.score / 3) * 100
    )

    st.markdown(
        f"""
        <div class="result-box">

            <div class="small-muted">
                HASIL TES DIAGNOSTIK
            </div>

            <div class="big-score">
                {percentage}%
            </div>

            <div>
                Tingkat pemahaman awal
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Skor",
            f"{st.session_state.score}/3"
        )

    with c2:
        st.metric(
            "Level",
            st.session_state.level
        )

    with c3:
        st.metric(
            "Materi",
            st.session_state.material
        )

    st.markdown("## 🔎 Analisis Sistem")

    if st.session_state.score <= 1:

        st.markdown("""
        <div class="ai-box">
            <div class="ai-label">🤖 AI Learning Analysis</div>
            <div class="ai-question">
                Pemahaman dasar masih perlu diperkuat.
            </div>
            <p>
                Sistem akan memberikan penjelasan secara bertahap
                dan menggunakan contoh sederhana sebelum menuju
                soal yang lebih kompleks.
            </p>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.score == 2:

        st.markdown("""
        <div class="ai-box">
            <div class="ai-label">🤖 AI Learning Analysis</div>
            <div class="ai-question">
                Kamu sudah memahami sebagian besar konsep dasar.
            </div>
            <p>
                Sistem akan melewati materi yang sudah dikuasai
                dan fokus pada konsep yang masih perlu diperkuat.
            </p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="ai-box">
            <div class="ai-label">🤖 AI Learning Analysis</div>
            <div class="ai-question">
                Pemahaman awalmu sudah sangat baik.
            </div>
            <p>
                Sistem akan memberikan tantangan yang lebih tinggi
                dan mengarahkanmu pada penerapan konsep.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🎯 Fokus Pembelajaran")

    st.info(
        st.session_state.focus
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
        f"{st.session_state.material} • "
        f"Level {st.session_state.level}"
    )

    st.markdown("""
    <div class="ai-box">

        <div class="ai-label">
            🧠 Adaptive AI Tutor
        </div>

        <div class="ai-question">
            Saya sudah melihat hasil tes diagnostikmu.
            Sekarang kita belajar sesuai dengan bagian
            yang masih perlu diperkuat.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Fokus Belajarmu")

    st.info(
        st.session_state.focus
    )

    st.markdown("### 💬 Mari Berdiskusi")

    st.markdown("""
    <div class="card">

        <div class="card-title">
            🤖 AI Tutor
        </div>

        <p>
        Menurutmu, apa yang akan terjadi pada sebuah ekosistem
        jika jumlah produsen tiba-tiba menurun drastis?
        </p>

        <p class="small-muted">
        Tidak perlu takut salah. Jelaskan dengan bahasamu sendiri.
        </p>

    </div>
    """, unsafe_allow_html=True)

    answer = st.text_area(
        "Jawabanmu",
        placeholder="Tuliskan pemikiranmu di sini...",
        height=140
    )

    if st.button(
        "💬 Kirim Jawaban",
        use_container_width=True
    ):

        if not answer.strip():

            st.warning(
                "Coba tuliskan jawabanmu terlebih dahulu."
            )

        else:

            st.success(
                "Jawaban diterima."
            )

            st.markdown("""
            <div class="ai-box">

                <div class="ai-label">
                    🤖 AI Tutor
                </div>

                <div class="ai-question">
                    Bagus. Kamu sudah mulai menghubungkan
                    produsen dengan keberlangsungan ekosistem.
                </div>

                <p>
                Sekarang kita naik satu tingkat.
                Jika produsen berkurang karena kekeringan,
                bagaimana kondisi konsumen tingkat pertama?
                Jelaskan alasannya.
                </p>

            </div>
            """, unsafe_allow_html=True)

    st.divider()

    if st.button(
        "🎯 Lanjut ke Evaluasi",
        use_container_width=True
    ):

        st.session_state.page = "result"

        st.rerun()


# =========================================================
# RESULT
# =========================================================

elif st.session_state.page == "result":

    st.markdown("""
    <div class="hero">
        <div class="hero-small">Learning Journey Completed</div>
        <div class="hero-title">
            🎉 Hebat! Pembelajaran selesai.
        </div>
        <div class="hero-desc">
            Berikut adalah ringkasan perjalanan belajar
            yang telah kamu lakukan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"## 👋 {st.session_state.name}"
    )

    st.write(
        f"Materi: **{st.session_state.material}**"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Pre-test",
            f"{int((st.session_state.score / 3) * 100)}%"
        )

    with c2:
        st.metric(
            "Post-test",
            "100%"
        )

    with c3:
        improvement = 100 - int(
            (st.session_state.score / 3) * 100
        )

        st.metric(
            "Peningkatan",
            f"+{improvement}%"
        )

    st.write("")

    st.markdown("""
    <div class="result-box">

        <div class="small-muted">
            PROFIL PEMBELAJARAN
        </div>

        <h2>🎯 Fokus yang diperkuat</h2>

        <h3>
        Konsep dan penerapan Ekosistem
        </h3>

        <p>
        Sistem merekomendasikan kamu melanjutkan
        ke materi berikutnya setelah memahami
        konsep yang diperkuat.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.success(
        "🟢 Status pembelajaran: Penguasaan meningkat"
    )

    st.info(
        "Pada versi berikutnya, AI Tutor akan menggunakan "
        "model AI sungguhan dan seluruh progress siswa "
        "akan disimpan dalam database."
    )

    if st.button(
        "🔄 Mulai Pembelajaran Baru",
        use_container_width=True
    ):

        for key in defaults:
            if key not in ["page"]:
                if key in st.session_state:
                    del st.session_state[key]

        st.session_state.page = "home"

        st.rerun()
