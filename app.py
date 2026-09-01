import streamlit as st

# =========================================================
# SALiM - Science Adaptive Learning Machine
# IPA Kelas X | 3 Subbab | Tanpa API Eksternal
# Developed by Tabdulghaffur
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
    "pre_answers": {},
    "pre_score": 0,
    "level": "",
    "focus": "",
    "subbab_index": 0,
    "subbab_answers": {},
    "subbab_scores": {},
    "post_answers": {},
    "post_score": 0,
    "submitted_subbab": False,
    "submitted_post": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================================================
# DATA PEMBELAJARAN
# =========================================================

SUBBAB = [
    {
        "title": "Komponen Ekosistem",
        "icon": "🌱",
        "material": """
        Ekosistem tersusun atas komponen biotik dan abiotik. Komponen biotik
        adalah makhluk hidup seperti tumbuhan, hewan, manusia, bakteri, dan jamur.
        Komponen abiotik adalah unsur tidak hidup seperti air, tanah, cahaya matahari,
        suhu, dan udara. Keduanya saling berinteraksi sehingga membentuk suatu ekosistem.
        """,
        "question": "Organisme yang mampu membuat makanan sendiri melalui fotosintesis disebut...",
        "options": ["Konsumen", "Produsen", "Pengurai", "Detritivor"],
        "answer": "Produsen",
        "explanation": "Produsen, seperti tumbuhan hijau, mampu membuat makanan sendiri melalui fotosintesis."
    },
    {
        "title": "Aliran Energi dalam Ekosistem",
        "icon": "☀️",
        "material": """
        Energi dalam ekosistem terutama berasal dari matahari. Energi tersebut
        ditangkap produsen melalui fotosintesis, kemudian berpindah ke konsumen
        melalui proses makan dan dimakan. Contoh rantai makanan:
        rumput → belalang → katak → ular. Energi mengalir dari satu tingkat trofik
        ke tingkat berikutnya.
        """,
        "question": "Pada rantai makanan rumput → belalang → katak → ular, organisme yang memperoleh energi langsung dari rumput adalah...",
        "options": ["Belalang", "Katak", "Ular", "Pengurai"],
        "answer": "Belalang",
        "explanation": "Belalang memakan rumput secara langsung sehingga memperoleh energi langsung dari produsen."
    },
    {
        "title": "Peran Dekomposer",
        "icon": "🦠",
        "material": """
        Dekomposer atau pengurai berperan menguraikan sisa makhluk hidup dan
        bahan organik menjadi zat yang lebih sederhana. Bakteri dan jamur merupakan
        contoh organisme yang berperan sebagai pengurai. Proses penguraian membantu
        mengembalikan unsur hara ke lingkungan sehingga dapat dimanfaatkan kembali
        oleh produsen.
        """,
        "question": "Apa fungsi utama bakteri dan jamur sebagai organisme pengurai dalam ekosistem?",
        "options": [
            "Menghasilkan energi matahari",
            "Menghasilkan makanan bagi produsen",
            "Menguraikan sisa organisme",
            "Menghentikan rantai makanan"
        ],
        "answer": "Menguraikan sisa organisme",
        "explanation": "Bakteri dan jamur menguraikan sisa organisme menjadi zat yang lebih sederhana dan membantu mengembalikan unsur hara ke lingkungan."
    },
]

# Pre-test memakai satu soal untuk setiap subbab
PRETEST = [
    {
        "question": "Organisme yang mampu membuat makanan sendiri melalui fotosintesis disebut...",
        "options": ["Konsumen", "Produsen", "Pengurai", "Detritivor"],
        "answer": "Produsen",
        "subbab": "Komponen Ekosistem"
    },
    {
        "question": "Pada rantai makanan rumput → belalang → katak → ular, organisme yang memperoleh energi langsung dari rumput adalah...",
        "options": ["Belalang", "Katak", "Ular", "Pengurai"],
        "answer": "Belalang",
        "subbab": "Aliran Energi dalam Ekosistem"
    },
    {
        "question": "Apa fungsi utama bakteri dan jamur sebagai organisme pengurai dalam ekosistem?",
        "options": [
            "Menghasilkan energi matahari",
            "Menghasilkan makanan bagi produsen",
            "Menguraikan sisa organisme",
            "Menghentikan rantai makanan"
        ],
        "answer": "Menguraikan sisa organisme",
        "subbab": "Peran Dekomposer"
    },
]

# Post-test menggunakan soal berbeda tetapi masih mengukur konsep yang sama
POSTTEST = [
    {
        "question": "Tumbuhan hijau dalam ekosistem terutama berperan sebagai...",
        "options": ["Produsen", "Konsumen", "Dekomposer", "Detritivor"],
        "answer": "Produsen"
    },
    {
        "question": "Dalam rantai makanan padi → tikus → ular → elang, tikus berperan sebagai...",
        "options": ["Produsen", "Konsumen tingkat I", "Konsumen tingkat II", "Pengurai"],
        "answer": "Konsumen tingkat I"
    },
    {
        "question": "Organisme yang membantu menguraikan daun dan bangkai menjadi zat yang lebih sederhana adalah...",
        "options": ["Tumbuhan", "Belalang", "Bakteri dan jamur", "Elang"],
        "answer": "Bakteri dan jamur"
    },
]

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

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1180px;
}

.hero {
    padding: 50px;
    border-radius: 28px;
    background: linear-gradient(135deg, #111827 0%, #1e293b 50%, #312e81 100%);
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
    max-width: 800px;
}

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

.material-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    min-height: 190px;
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

.ai-box {
    background: linear-gradient(135deg, #eef2ff, #ecfeff);
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
            SALiM menggunakan hasil tes diagnostik untuk menentukan
            fokus pembelajaran dan memberikan pengalaman belajar yang bertahap.
        </div>
        <div class="hero-desc" style="margin-top:12px;">
            Developed by Tabdulghaffur
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Mulai Perjalanan Belajarmu")

    col1, col2 = st.columns(2)

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
            placeholder="Contoh: Ahmad",
            key="home_name"
        )

        student_code = st.text_input(
            "Kode siswa",
            placeholder="Contoh: S001",
            key="home_code"
        )

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">📚 Materi IPA</div>
            <div class="card-desc">
                SALiM saat ini difokuskan pada materi Ekosistem
                dengan tiga subbab pembelajaran.
            </div>
        </div>
        """, unsafe_allow_html=True)

        material = st.selectbox(
            "Materi",
            ["Ekosistem"],
            key="home_material"
        )

    st.write("")

    if st.button("🚀 Mulai Pembelajaran", use_container_width=True):
        if not name.strip():
            st.warning("Masukkan nama siswa terlebih dahulu.")
        elif not student_code.strip():
            st.warning("Masukkan kode siswa terlebih dahulu.")
        else:
            st.session_state.name = name.strip()
            st.session_state.student_code = student_code.strip().upper()
            st.session_state.material = material
            st.session_state.pre_answers = {}
            st.session_state.pre_score = 0
            st.session_state.subbab_index = 0
            st.session_state.subbab_answers = {}
            st.session_state.subbab_scores = {}
            st.session_state.post_answers = {}
            st.session_state.post_score = 0
            st.session_state.submitted_subbab = False
            st.session_state.submitted_post = False
            st.session_state.page = "pretest"
            st.rerun()

    st.markdown("---")
    st.markdown("## 🔬 Subbab IPA")

    cols = st.columns(3)
    for i, item in enumerate(SUBBAB):
        with cols[i]:
            st.markdown(f"""
            <div class="material-card">
                <div class="material-icon">{item["icon"]}</div>
                <div class="material-title">Subbab {i+1}: {item["title"]}</div>
                <div class="material-text">
                    Pembelajaran adaptif berdasarkan pemahaman siswa.
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    cols = st.columns(3)

    stats = [
        ("3", "Subbab Pembelajaran"),
        ("AI", "Pembelajaran Adaptif"),
        ("∞", "Jalur Belajar Personal"),
    ]

    for col, (number, label) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class="stat">
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# PRE-TEST
# =========================================================

elif st.session_state.page == "pretest":

    st.title("🧠 Pre-test Diagnostik")
    st.caption(
        f"{st.session_state.name} • {st.session_state.material}"
    )

    st.progress(0.20)

    st.markdown("""
    <div class="card">
        <div class="card-title">Mengapa ada pre-test?</div>
        <div class="card-desc">
            Pre-test digunakan SALiM untuk mengetahui pemahaman awal
            siswa sebelum menentukan jalur pembelajaran adaptif.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for i, q in enumerate(PRETEST):
        st.markdown(f"""
        <div class="question-box">
            <div class="question-number">
                Pertanyaan {i+1:02d} • {q["subbab"]}
            </div>
            <div class="question-text">
                {q["question"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

        current = st.session_state.pre_answers.get(i)
        selected = st.radio(
            "Pilih jawaban:",
            q["options"],
            index=q["options"].index(current) if current in q["options"] else None,
            key=f"pre_{i}"
        )
        st.session_state.pre_answers[i] = selected

    if st.button("📊 Analisis Pemahaman Saya", use_container_width=True):
        if any(v is None for v in st.session_state.pre_answers.values()):
            st.warning("Jawab semua pertanyaan terlebih dahulu.")
        else:
            score = sum(
                st.session_state.pre_answers[i] == q["answer"]
                for i, q in enumerate(PRETEST)
            )

            st.session_state.pre_score = score

            if score == 0:
                st.session_state.level = "Pemula"
                st.session_state.focus = "Komponen, aliran energi, dan peran pengurai dalam ekosistem"
            elif score == 1:
                st.session_state.level = "Dasar"
                st.session_state.focus = "Konsep dasar ekosistem yang masih perlu diperkuat"
            elif score == 2:
                st.session_state.level = "Menengah"
                st.session_state.focus = "Konsep yang belum dikuasai secara konsisten"
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

    percentage = int((st.session_state.pre_score / len(PRETEST)) * 100)

    st.markdown(f"""
    <div class="result-box">
        <div class="small-muted">HASIL PRE-TEST</div>
        <div class="big-score">{percentage}%</div>
        <div>Tingkat pemahaman awal</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Skor", f"{st.session_state.pre_score}/{len(PRETEST)}")

    with c2:
        st.metric("Level", st.session_state.level)

    with c3:
        st.metric("Materi", st.session_state.material)

    st.markdown("## 🔎 Analisis Sistem")

    if st.session_state.pre_score <= 1:
        message = (
            "Pemahaman dasar masih perlu diperkuat. "
            "SALiM akan memberikan pembelajaran dari konsep paling dasar."
        )
    elif st.session_state.pre_score == 2:
        message = (
            "Kamu sudah memahami sebagian besar konsep dasar. "
            "SALiM akan memberikan penguatan pada konsep yang masih kurang."
        )
    else:
        message = (
            "Pemahaman awalmu sudah sangat baik. "
            "SALiM akan mengarahkanmu pada penerapan konsep."
        )

    st.markdown(f"""
    <div class="ai-box">
        <div class="ai-label">🤖 SALiM Learning Analysis</div>
        <div class="ai-question">{message}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Fokus Pembelajaran")
    st.info(st.session_state.focus)

    if st.button("🤖 Mulai Pembelajaran Adaptif", use_container_width=True):
        st.session_state.subbab_index = 0
        st.session_state.submitted_subbab = False
        st.session_state.page = "subbab"
        st.rerun()

# =========================================================
# SUBBAB PEMBELAJARAN
# =========================================================

elif st.session_state.page == "subbab":

    idx = st.session_state.subbab_index
    item = SUBBAB[idx]

    st.title(f"{item['icon']} Subbab {idx + 1}: {item['title']}")
    st.caption(
        f"{st.session_state.name} • Level {st.session_state.level}"
    )

    st.progress((idx + 1) / len(SUBBAB))

    st.markdown(f"""
    <div class="ai-box">
        <div class="ai-label">🧠 Adaptive Learning</div>
        <div class="ai-question">
            Pelajari konsep berikut sebelum mengerjakan soal.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📖 Materi")
    st.markdown(
        f'<div class="card"><div class="card-desc">{item["material"]}</div></div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="question-box">
        <div class="question-number">
            Latihan {idx + 1:02d} • {item["title"]}
        </div>
        <div class="question-text">
            {item["question"]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    saved_answer = st.session_state.subbab_answers.get(idx)
    selected = st.radio(
        "Pilih jawaban:",
        item["options"],
        index=item["options"].index(saved_answer)
        if saved_answer in item["options"] else None,
        key=f"subbab_radio_{idx}"
    )

    st.session_state.subbab_answers[idx] = selected

    if not st.session_state.submitted_subbab:
        if st.button("✅ Periksa Jawaban", use_container_width=True):
            if selected is None:
                st.warning("Pilih salah satu jawaban terlebih dahulu.")
            else:
                st.session_state.submitted_subbab = True
                st.rerun()
    else:
        if selected == item["answer"]:
            st.success("🎉 Jawaban benar!")
        else:
            st.error(f"❌ Jawaban belum tepat. Jawaban yang benar: {item['answer']}")

        st.markdown(f"""
        <div class="card">
            <div class="card-title">💡 Pembahasan</div>
            <div class="card-desc">{item["explanation"]}</div>
        </div>
        """, unsafe_allow_html=True)

        if selected == item["answer"]:
            st.session_state.subbab_scores[idx] = 1
        else:
            st.session_state.subbab_scores[idx] = 0

        if idx < len(SUBBAB) - 1:
            if st.button("➡️ Lanjut ke Subbab Berikutnya", use_container_width=True):
                st.session_state.subbab_index += 1
                st.session_state.submitted_subbab = False
                st.rerun()
        else:
            if st.button("📝 Lanjut ke Post-test", use_container_width=True):
                st.session_state.submitted_post = False
                st.session_state.page = "posttest"
                st.rerun()

# =========================================================
# POST-TEST
# =========================================================

elif st.session_state.page == "posttest":

    st.title("📝 Post-test")
    st.caption(
        f"{st.session_state.name} • {st.session_state.material}"
    )

    st.progress(0.90)

    st.markdown("""
    <div class="card">
        <div class="card-title">Evaluasi Akhir</div>
        <div class="card-desc">
            Jawablah pertanyaan berikut untuk melihat perubahan
            pemahaman setelah mengikuti pembelajaran SALiM.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for i, q in enumerate(POSTTEST):
        st.markdown(f"""
        <div class="question-box">
            <div class="question-number">Post-test {i+1:02d}</div>
            <div class="question-text">{q["question"]}</div>
        </div>
        """, unsafe_allow_html=True)

        current = st.session_state.post_answers.get(i)
        selected = st.radio(
            "Pilih jawaban:",
            q["options"],
            index=q["options"].index(current) if current in q["options"] else None,
            key=f"post_{i}"
        )
        st.session_state.post_answers[i] = selected

    if not st.session_state.submitted_post:
        if st.button("📊 Selesai & Lihat Hasil", use_container_width=True):
            if any(v is None for v in st.session_state.post_answers.values()):
                st.warning("Jawab semua pertanyaan terlebih dahulu.")
            else:
                score = sum(
                    st.session_state.post_answers[i] == q["answer"]
                    for i, q in enumerate(POSTTEST)
                )
                st.session_state.post_score = score
                st.session_state.submitted_post = True
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
            🎉 Pembelajaran selesai!
        </div>
        <div class="hero-desc">
            Berikut ringkasan perjalanan belajar yang telah kamu lakukan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"## 👋 {st.session_state.name}")
    st.write(f"Materi: **{st.session_state.material}**")

    pre_percentage = int(
        (st.session_state.pre_score / len(PRETEST)) * 100
    )
    post_percentage = int(
        (st.session_state.post_score / len(POSTTEST)) * 100
    )
    improvement = post_percentage - pre_percentage

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Pre-test", f"{pre_percentage}%")

    with c2:
        st.metric("Post-test", f"{post_percentage}%")

    with c3:
        st.metric(
            "Peningkatan",
            f"{improvement:+d}%",
            delta=f"{improvement:+d}%"
        )

    st.write("")

    subbab_total = sum(st.session_state.subbab_scores.values())
    subbab_percentage = int((subbab_total / len(SUBBAB)) * 100)

    st.markdown(f"""
    <div class="result-box">
        <div class="small-muted">HASIL PEMBELAJARAN SALiM</div>
        <div class="big-score">{post_percentage}%</div>
        <div>Skor post-test</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("### 📚 Hasil Tiap Subbab")

    for i, item in enumerate(SUBBAB):
        score = st.session_state.subbab_scores.get(i, 0)
        status = "✅ Benar" if score == 1 else "❌ Perlu penguatan"
        st.write(f"**Subbab {i+1}: {item['title']}** — {status}")

    if improvement > 0:
        st.success(
            f"🟢 Pemahaman meningkat sebesar {improvement}% "
            "setelah mengikuti pembelajaran."
        )
    elif improvement == 0:
        st.info(
            "🔵 Skor belum berubah. Materi masih dapat dipelajari kembali."
        )
    else:
        st.warning(
            f"🟠 Skor post-test lebih rendah {abs(improvement)}%. "
            "Disarankan mengulang materi."
        )

    st.info(
        "Catatan: versi ini menggunakan logika adaptif berbasis hasil tes "
        "diagnostik. Model deep learning/API AI dapat diintegrasikan pada tahap berikutnya."
    )

    if st.button("🔄 Mulai Pembelajaran Baru", use_container_width=True):
        for key in list(defaults.keys()):
            if key != "page" and key in st.session_state:
                del st.session_state[key]

        st.session_state.page = "home"
        st.rerun()
import streamlit as st

# =========================================================
# SALiM - Science Adaptive Learning Machine
# IPA Kelas X | 3 Subbab | Tanpa API Eksternal
# Developed by Tabdulghaffur
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
    "pre_answers": {},
    "pre_score": 0,
    "level": "",
    "focus": "",
    "subbab_index": 0,
    "subbab_answers": {},
    "subbab_scores": {},
    "post_answers": {},
    "post_score": 0,
    "submitted_subbab": False,
    "submitted_post": False,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# =========================================================
# DATA PEMBELAJARAN
# =========================================================

SUBBAB = [
    {
        "title": "Komponen Ekosistem",
        "icon": "🌱",
        "material": """
        Ekosistem tersusun atas komponen biotik dan abiotik. Komponen biotik
        adalah makhluk hidup seperti tumbuhan, hewan, manusia, bakteri, dan jamur.
        Komponen abiotik adalah unsur tidak hidup seperti air, tanah, cahaya matahari,
        suhu, dan udara. Keduanya saling berinteraksi sehingga membentuk suatu ekosistem.
        """,
        "question": "Organisme yang mampu membuat makanan sendiri melalui fotosintesis disebut...",
        "options": ["Konsumen", "Produsen", "Pengurai", "Detritivor"],
        "answer": "Produsen",
        "explanation": "Produsen, seperti tumbuhan hijau, mampu membuat makanan sendiri melalui fotosintesis."
    },
    {
        "title": "Aliran Energi dalam Ekosistem",
        "icon": "☀️",
        "material": """
        Energi dalam ekosistem terutama berasal dari matahari. Energi tersebut
        ditangkap produsen melalui fotosintesis, kemudian berpindah ke konsumen
        melalui proses makan dan dimakan. Contoh rantai makanan:
        rumput → belalang → katak → ular. Energi mengalir dari satu tingkat trofik
        ke tingkat berikutnya.
        """,
        "question": "Pada rantai makanan rumput → belalang → katak → ular, organisme yang memperoleh energi langsung dari rumput adalah...",
        "options": ["Belalang", "Katak", "Ular", "Pengurai"],
        "answer": "Belalang",
        "explanation": "Belalang memakan rumput secara langsung sehingga memperoleh energi langsung dari produsen."
    },
    {
        "title": "Peran Dekomposer",
        "icon": "🦠",
        "material": """
        Dekomposer atau pengurai berperan menguraikan sisa makhluk hidup dan
        bahan organik menjadi zat yang lebih sederhana. Bakteri dan jamur merupakan
        contoh organisme yang berperan sebagai pengurai. Proses penguraian membantu
        mengembalikan unsur hara ke lingkungan sehingga dapat dimanfaatkan kembali
        oleh produsen.
        """,
        "question": "Apa fungsi utama bakteri dan jamur sebagai organisme pengurai dalam ekosistem?",
        "options": [
            "Menghasilkan energi matahari",
            "Menghasilkan makanan bagi produsen",
            "Menguraikan sisa organisme",
            "Menghentikan rantai makanan"
        ],
        "answer": "Menguraikan sisa organisme",
        "explanation": "Bakteri dan jamur menguraikan sisa organisme menjadi zat yang lebih sederhana dan membantu mengembalikan unsur hara ke lingkungan."
    },
]

# Pre-test memakai satu soal untuk setiap subbab
PRETEST = [
    {
        "question": "Organisme yang mampu membuat makanan sendiri melalui fotosintesis disebut...",
        "options": ["Konsumen", "Produsen", "Pengurai", "Detritivor"],
        "answer": "Produsen",
        "subbab": "Komponen Ekosistem"
    },
    {
        "question": "Pada rantai makanan rumput → belalang → katak → ular, organisme yang memperoleh energi langsung dari rumput adalah...",
        "options": ["Belalang", "Katak", "Ular", "Pengurai"],
        "answer": "Belalang",
        "subbab": "Aliran Energi dalam Ekosistem"
    },
    {
        "question": "Apa fungsi utama bakteri dan jamur sebagai organisme pengurai dalam ekosistem?",
        "options": [
            "Menghasilkan energi matahari",
            "Menghasilkan makanan bagi produsen",
            "Menguraikan sisa organisme",
            "Menghentikan rantai makanan"
        ],
        "answer": "Menguraikan sisa organisme",
        "subbab": "Peran Dekomposer"
    },
]

# Post-test menggunakan soal berbeda tetapi masih mengukur konsep yang sama
POSTTEST = [
    {
        "question": "Tumbuhan hijau dalam ekosistem terutama berperan sebagai...",
        "options": ["Produsen", "Konsumen", "Dekomposer", "Detritivor"],
        "answer": "Produsen"
    },
    {
        "question": "Dalam rantai makanan padi → tikus → ular → elang, tikus berperan sebagai...",
        "options": ["Produsen", "Konsumen tingkat I", "Konsumen tingkat II", "Pengurai"],
        "answer": "Konsumen tingkat I"
    },
    {
        "question": "Organisme yang membantu menguraikan daun dan bangkai menjadi zat yang lebih sederhana adalah...",
        "options": ["Tumbuhan", "Belalang", "Bakteri dan jamur", "Elang"],
        "answer": "Bakteri dan jamur"
    },
]

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

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1180px;
}

.hero {
    padding: 50px;
    border-radius: 28px;
    background: linear-gradient(135deg, #111827 0%, #1e293b 50%, #312e81 100%);
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
    max-width: 800px;
}

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

.material-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    min-height: 190px;
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

.ai-box {
    background: linear-gradient(135deg, #eef2ff, #ecfeff);
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
            SALiM menggunakan hasil tes diagnostik untuk menentukan
            fokus pembelajaran dan memberikan pengalaman belajar yang bertahap.
        </div>
        <div class="hero-desc" style="margin-top:12px;">
            Developed by Tabdulghaffur
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Mulai Perjalanan Belajarmu")

    col1, col2 = st.columns(2)

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
            placeholder="Contoh: Ahmad",
            key="home_name"
        )

        student_code = st.text_input(
            "Kode siswa",
            placeholder="Contoh: S001",
            key="home_code"
        )

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">📚 Materi IPA</div>
            <div class="card-desc">
                SALiM saat ini difokuskan pada materi Ekosistem
                dengan tiga subbab pembelajaran.
            </div>
        </div>
        """, unsafe_allow_html=True)

        material = st.selectbox(
            "Materi",
            ["Ekosistem"],
            key="home_material"
        )

    st.write("")

    if st.button("🚀 Mulai Pembelajaran", use_container_width=True):
        if not name.strip():
            st.warning("Masukkan nama siswa terlebih dahulu.")
        elif not student_code.strip():
            st.warning("Masukkan kode siswa terlebih dahulu.")
        else:
            st.session_state.name = name.strip()
            st.session_state.student_code = student_code.strip().upper()
            st.session_state.material = material
            st.session_state.pre_answers = {}
            st.session_state.pre_score = 0
            st.session_state.subbab_index = 0
            st.session_state.subbab_answers = {}
            st.session_state.subbab_scores = {}
            st.session_state.post_answers = {}
            st.session_state.post_score = 0
            st.session_state.submitted_subbab = False
            st.session_state.submitted_post = False
            st.session_state.page = "pretest"
            st.rerun()

    st.markdown("---")
    st.markdown("## 🔬 Subbab IPA")

    cols = st.columns(3)
    for i, item in enumerate(SUBBAB):
        with cols[i]:
            st.markdown(f"""
            <div class="material-card">
                <div class="material-icon">{item["icon"]}</div>
                <div class="material-title">Subbab {i+1}: {item["title"]}</div>
                <div class="material-text">
                    Pembelajaran adaptif berdasarkan pemahaman siswa.
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")
    cols = st.columns(3)

    stats = [
        ("3", "Subbab Pembelajaran"),
        ("AI", "Pembelajaran Adaptif"),
        ("∞", "Jalur Belajar Personal"),
    ]

    for col, (number, label) in zip(cols, stats):
        with col:
            st.markdown(f"""
            <div class="stat">
                <div class="stat-number">{number}</div>
                <div class="stat-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# PRE-TEST
# =========================================================

elif st.session_state.page == "pretest":

    st.title("🧠 Pre-test Diagnostik")
    st.caption(
        f"{st.session_state.name} • {st.session_state.material}"
    )

    st.progress(0.20)

    st.markdown("""
    <div class="card">
        <div class="card-title">Mengapa ada pre-test?</div>
        <div class="card-desc">
            Pre-test digunakan SALiM untuk mengetahui pemahaman awal
            siswa sebelum menentukan jalur pembelajaran adaptif.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for i, q in enumerate(PRETEST):
        st.markdown(f"""
        <div class="question-box">
            <div class="question-number">
                Pertanyaan {i+1:02d} • {q["subbab"]}
            </div>
            <div class="question-text">
                {q["question"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

        current = st.session_state.pre_answers.get(i)
        selected = st.radio(
            "Pilih jawaban:",
            q["options"],
            index=q["options"].index(current) if current in q["options"] else None,
            key=f"pre_{i}"
        )
        st.session_state.pre_answers[i] = selected

    if st.button("📊 Analisis Pemahaman Saya", use_container_width=True):
        if any(v is None for v in st.session_state.pre_answers.values()):
            st.warning("Jawab semua pertanyaan terlebih dahulu.")
        else:
            score = sum(
                st.session_state.pre_answers[i] == q["answer"]
                for i, q in enumerate(PRETEST)
            )

            st.session_state.pre_score = score

            if score == 0:
                st.session_state.level = "Pemula"
                st.session_state.focus = "Komponen, aliran energi, dan peran pengurai dalam ekosistem"
            elif score == 1:
                st.session_state.level = "Dasar"
                st.session_state.focus = "Konsep dasar ekosistem yang masih perlu diperkuat"
            elif score == 2:
                st.session_state.level = "Menengah"
                st.session_state.focus = "Konsep yang belum dikuasai secara konsisten"
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

    percentage = int((st.session_state.pre_score / len(PRETEST)) * 100)

    st.markdown(f"""
    <div class="result-box">
        <div class="small-muted">HASIL PRE-TEST</div>
        <div class="big-score">{percentage}%</div>
        <div>Tingkat pemahaman awal</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Skor", f"{st.session_state.pre_score}/{len(PRETEST)}")

    with c2:
        st.metric("Level", st.session_state.level)

    with c3:
        st.metric("Materi", st.session_state.material)

    st.markdown("## 🔎 Analisis Sistem")

    if st.session_state.pre_score <= 1:
        message = (
            "Pemahaman dasar masih perlu diperkuat. "
            "SALiM akan memberikan pembelajaran dari konsep paling dasar."
        )
    elif st.session_state.pre_score == 2:
        message = (
            "Kamu sudah memahami sebagian besar konsep dasar. "
            "SALiM akan memberikan penguatan pada konsep yang masih kurang."
        )
    else:
        message = (
            "Pemahaman awalmu sudah sangat baik. "
            "SALiM akan mengarahkanmu pada penerapan konsep."
        )

    st.markdown(f"""
    <div class="ai-box">
        <div class="ai-label">🤖 SALiM Learning Analysis</div>
        <div class="ai-question">{message}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Fokus Pembelajaran")
    st.info(st.session_state.focus)

    if st.button("🤖 Mulai Pembelajaran Adaptif", use_container_width=True):
        st.session_state.subbab_index = 0
        st.session_state.submitted_subbab = False
        st.session_state.page = "subbab"
        st.rerun()

# =========================================================
# SUBBAB PEMBELAJARAN
# =========================================================

elif st.session_state.page == "subbab":

    idx = st.session_state.subbab_index
    item = SUBBAB[idx]

    st.title(f"{item['icon']} Subbab {idx + 1}: {item['title']}")
    st.caption(
        f"{st.session_state.name} • Level {st.session_state.level}"
    )

    st.progress((idx + 1) / len(SUBBAB))

    st.markdown(f"""
    <div class="ai-box">
        <div class="ai-label">🧠 Adaptive Learning</div>
        <div class="ai-question">
            Pelajari konsep berikut sebelum mengerjakan soal.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📖 Materi")
    st.markdown(
        f'<div class="card"><div class="card-desc">{item["material"]}</div></div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="question-box">
        <div class="question-number">
            Latihan {idx + 1:02d} • {item["title"]}
        </div>
        <div class="question-text">
            {item["question"]}
        </div>
    </div>
    """, unsafe_allow_html=True)

    saved_answer = st.session_state.subbab_answers.get(idx)
    selected = st.radio(
        "Pilih jawaban:",
        item["options"],
        index=item["options"].index(saved_answer)
        if saved_answer in item["options"] else None,
        key=f"subbab_radio_{idx}"
    )

    st.session_state.subbab_answers[idx] = selected

    if not st.session_state.submitted_subbab:
        if st.button("✅ Periksa Jawaban", use_container_width=True):
            if selected is None:
                st.warning("Pilih salah satu jawaban terlebih dahulu.")
            else:
                st.session_state.submitted_subbab = True
                st.rerun()
    else:
        if selected == item["answer"]:
            st.success("🎉 Jawaban benar!")
        else:
            st.error(f"❌ Jawaban belum tepat. Jawaban yang benar: {item['answer']}")

        st.markdown(f"""
        <div class="card">
            <div class="card-title">💡 Pembahasan</div>
            <div class="card-desc">{item["explanation"]}</div>
        </div>
        """, unsafe_allow_html=True)

        if selected == item["answer"]:
            st.session_state.subbab_scores[idx] = 1
        else:
            st.session_state.subbab_scores[idx] = 0

        if idx < len(SUBBAB) - 1:
            if st.button("➡️ Lanjut ke Subbab Berikutnya", use_container_width=True):
                st.session_state.subbab_index += 1
                st.session_state.submitted_subbab = False
                st.rerun()
        else:
            if st.button("📝 Lanjut ke Post-test", use_container_width=True):
                st.session_state.submitted_post = False
                st.session_state.page = "posttest"
                st.rerun()

# =========================================================
# POST-TEST
# =========================================================

elif st.session_state.page == "posttest":

    st.title("📝 Post-test")
    st.caption(
        f"{st.session_state.name} • {st.session_state.material}"
    )

    st.progress(0.90)

    st.markdown("""
    <div class="card">
        <div class="card-title">Evaluasi Akhir</div>
        <div class="card-desc">
            Jawablah pertanyaan berikut untuk melihat perubahan
            pemahaman setelah mengikuti pembelajaran SALiM.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for i, q in enumerate(POSTTEST):
        st.markdown(f"""
        <div class="question-box">
            <div class="question-number">Post-test {i+1:02d}</div>
            <div class="question-text">{q["question"]}</div>
        </div>
        """, unsafe_allow_html=True)

        current = st.session_state.post_answers.get(i)
        selected = st.radio(
            "Pilih jawaban:",
            q["options"],
            index=q["options"].index(current) if current in q["options"] else None,
            key=f"post_{i}"
        )
        st.session_state.post_answers[i] = selected

    if not st.session_state.submitted_post:
        if st.button("📊 Selesai & Lihat Hasil", use_container_width=True):
            if any(v is None for v in st.session_state.post_answers.values()):
                st.warning("Jawab semua pertanyaan terlebih dahulu.")
            else:
                score = sum(
                    st.session_state.post_answers[i] == q["answer"]
                    for i, q in enumerate(POSTTEST)
                )
                st.session_state.post_score = score
                st.session_state.submitted_post = True
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
            🎉 Pembelajaran selesai!
        </div>
        <div class="hero-desc">
            Berikut ringkasan perjalanan belajar yang telah kamu lakukan.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"## 👋 {st.session_state.name}")
    st.write(f"Materi: **{st.session_state.material}**")

    pre_percentage = int(
        (st.session_state.pre_score / len(PRETEST)) * 100
    )
    post_percentage = int(
        (st.session_state.post_score / len(POSTTEST)) * 100
    )
    improvement = post_percentage - pre_percentage

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Pre-test", f"{pre_percentage}%")

    with c2:
        st.metric("Post-test", f"{post_percentage}%")

    with c3:
        st.metric(
            "Peningkatan",
            f"{improvement:+d}%",
            delta=f"{improvement:+d}%"
        )

    st.write("")

    subbab_total = sum(st.session_state.subbab_scores.values())
    subbab_percentage = int((subbab_total / len(SUBBAB)) * 100)

    st.markdown(f"""
    <div class="result-box">
        <div class="small-muted">HASIL PEMBELAJARAN SALiM</div>
        <div class="big-score">{post_percentage}%</div>
        <div>Skor post-test</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("### 📚 Hasil Tiap Subbab")

    for i, item in enumerate(SUBBAB):
        score = st.session_state.subbab_scores.get(i, 0)
        status = "✅ Benar" if score == 1 else "❌ Perlu penguatan"
        st.write(f"**Subbab {i+1}: {item['title']}** — {status}")

    if improvement > 0:
        st.success(
            f"🟢 Pemahaman meningkat sebesar {improvement}% "
            "setelah mengikuti pembelajaran."
        )
    elif improvement == 0:
        st.info(
            "🔵 Skor belum berubah. Materi masih dapat dipelajari kembali."
        )
    else:
        st.warning(
            f"🟠 Skor post-test lebih rendah {abs(improvement)}%. "
            "Disarankan mengulang materi."
        )

    st.info(
        "Catatan: versi ini menggunakan logika adaptif berbasis hasil tes "
        "diagnostik. Model deep learning/API AI dapat diintegrasikan pada tahap berikutnya."
    )

    if st.button("🔄 Mulai Pembelajaran Baru", use_container_width=True):
        for key in list(defaults.keys()):
            if key != "page" and key in st.session_state:
                del st.session_state[key]

        st.session_state.page = "home"
        st.rerun()
