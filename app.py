import streamlit as st

# =========================================================
# KONFIGURASI
# =========================================================

st.set_page_config(
    page_title="SALiM - Sains Adaptive Learning Machine",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# DATA MATERI DAN SOAL
# =========================================================

MATERIALS = {
    "🌱 Ekosistem": {
        "description": "Memahami hubungan antara makhluk hidup dan lingkungan.",
        "questions": [
            {
                "question": "Organisme yang mampu membuat makanan sendiri melalui fotosintesis disebut...",
                "options": [
                    "Konsumen",
                    "Produsen",
                    "Pengurai",
                    "Detritivor"
                ],
                "answer": "Produsen",
                "explanation": "Produsen adalah organisme yang mampu membuat makanan sendiri, umumnya melalui fotosintesis. Contohnya tumbuhan hijau."
            },
            {
                "question": "Perhatikan rantai makanan berikut: Rumput → Belalang → Katak → Ular. Organisme yang memperoleh energi langsung dari rumput adalah...",
                "options": [
                    "Belalang",
                    "Katak",
                    "Ular",
                    "Pengurai"
                ],
                "answer": "Belalang",
                "explanation": "Belalang merupakan konsumen tingkat I karena memperoleh energi langsung dengan memakan produsen, yaitu rumput."
            },
            {
                "question": "Apa fungsi utama organisme pengurai dalam ekosistem?",
                "options": [
                    "Menghasilkan energi matahari",
                    "Menghasilkan makanan bagi produsen",
                    "Menguraikan sisa organisme",
                    "Menghentikan rantai makanan"
                ],
                "answer": "Menguraikan sisa organisme",
                "explanation": "Pengurai seperti bakteri dan jamur menguraikan sisa makhluk hidup sehingga unsur hara dapat kembali ke lingkungan."
            }
        ]
    },

    "🧬 Keanekaragaman Hayati": {
        "description": "Mengenal tingkat keanekaragaman hayati dan pentingnya pelestarian.",
        "questions": [
            {
                "question": "Keanekaragaman yang terjadi karena adanya variasi dalam satu spesies disebut keanekaragaman tingkat...",
                "options": [
                    "Gen",
                    "Jenis",
                    "Ekosistem",
                    "Bioma"
                ],
                "answer": "Gen",
                "explanation": "Keanekaragaman gen merupakan variasi sifat yang terdapat dalam satu spesies. Contohnya berbagai varietas mangga."
            },
            {
                "question": "Contoh keanekaragaman hayati tingkat jenis adalah...",
                "options": [
                    "Mangga manalagi dan mangga golek",
                    "Kucing dan harimau",
                    "Hutan hujan dan savana",
                    "Padi merah dan padi putih"
                ],
                "answer": "Kucing dan harimau",
                "explanation": "Kucing dan harimau merupakan organisme dari jenis yang berbeda sehingga termasuk keanekaragaman tingkat jenis."
            },
            {
                "question": "Pelestarian badak Jawa di Taman Nasional Ujung Kulon merupakan contoh konservasi...",
                "options": [
                    "Ex situ",
                    "In situ",
                    "Buatan",
                    "Genetik"
                ],
                "answer": "In situ",
                "explanation": "Konservasi in situ dilakukan dengan melestarikan organisme di habitat alaminya. Taman Nasional Ujung Kulon merupakan habitat alami badak Jawa."
            }
        ]
    },

    "🌍 Perubahan Lingkungan": {
        "description": "Menganalisis penyebab, dampak, dan solusi perubahan lingkungan.",
        "questions": [
            {
                "question": "Salah satu penyebab utama pencemaran udara di wilayah perkotaan adalah...",
                "options": [
                    "Fotosintesis tumbuhan",
                    "Emisi kendaraan bermotor",
                    "Penguapan air",
                    "Pelapukan batuan"
                ],
                "answer": "Emisi kendaraan bermotor",
                "explanation": "Gas buang kendaraan bermotor mengandung berbagai polutan yang dapat menurunkan kualitas udara."
            },
            {
                "question": "Peningkatan konsentrasi gas rumah kaca di atmosfer dapat menyebabkan...",
                "options": [
                    "Pemanasan global",
                    "Penurunan suhu bumi secara permanen",
                    "Berkurangnya gravitasi bumi",
                    "Berhentinya siklus air"
                ],
                "answer": "Pemanasan global",
                "explanation": "Gas rumah kaca seperti karbon dioksida dan metana dapat meningkatkan efek rumah kaca sehingga berkontribusi terhadap pemanasan global."
            },
            {
                "question": "Tindakan yang paling tepat untuk mengurangi sampah plastik adalah...",
                "options": [
                    "Menggunakan plastik sekali pakai lebih banyak",
                    "Membakar semua sampah plastik",
                    "Mengurangi penggunaan plastik sekali pakai",
                    "Membuang plastik ke sungai"
                ],
                "answer": "Mengurangi penggunaan plastik sekali pakai",
                "explanation": "Mengurangi penggunaan plastik sekali pakai merupakan langkah pencegahan yang efektif untuk mengurangi timbulan sampah plastik."
            }
        ]
    }
}


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "page": "home",
    "name": "",
    "student_code": "",
    "material": "🌱 Ekosistem",
    "score": 0,
    "answers": {},
    "level": "",
    "focus": "",
    "tutor_answered": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
);

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(99,102,241,0.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 10%,
            rgba(16,185,129,0.10),
            transparent 30%
        ),
        #f8fafc;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* HERO */

.hero {
    padding: 50px;
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        #111827,
        #1e293b,
        #312e81
    );
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 20px 50px rgba(15,23,42,0.15);
}

.hero-small {
    color: #cbd5e1;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 1.5px;
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
    max-width: 750px;
}

/* CARD */

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
}

.card-desc {
    color: #64748b;
    line-height: 1.6;
}

/* MATERIAL */

.material-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    min-height: 185px;
    box-shadow: 0 8px 25px rgba(15,23,42,0.05);
}

.material-icon {
    font-size: 34px;
}

.material-title {
    font-size: 19px;
    font-weight: 700;
    margin-top: 8px;
}

.material-text {
    color: #64748b;
    font-size: 14px;
    line-height: 1.6;
}

/* QUESTION */

.question-box {
    background: white;
    border-radius: 20px;
    padding: 28px;
    border: 1px solid #e2e8f0;
    margin-bottom: 12px;
}

.question-number {
    color: #6366f1;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.question-text {
    font-size: 20px;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.6;
    margin-top: 10px;
}

/* AI */

.ai-box {
    background: linear-gradient(
        135deg,
        #eef2ff,
        #ecfeff
    );
    border: 1px solid #c7d2fe;
    border-radius: 22px;
    padding: 28px;
    margin: 20px 0;
}

.ai-label {
    color: #4f46e5;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.ai-text {
    color: #1e1b4b;
    font-size: 19px;
    font-weight: 700;
    line-height: 1.6;
    margin-top: 8px;
}

/* RESULT */

.result-box {
    background: white;
    border-radius: 25px;
    padding: 35px;
    border: 1px solid #e2e8f0;
    text-align: center;
    box-shadow: 0 12px 40px rgba(15,23,42,0.07);
}

.big-score {
    font-size: 60px;
    font-weight: 800;
    color: #4f46e5;
}

.stButton > button {
    border-radius: 12px;
    min-height: 46px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

def footer():
    st.markdown("---")
    st.caption(
        "SALiM • Sains Adaptive Learning Machine • "
        "Developed by Tabdulghaffur © 2026"
    )


# =========================================================
# HOME
# =========================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">

        <div class="hero-small">
            IPA Kelas X • Kurikulum Merdeka
        </div>

        <div class="hero-title">
            🧬 SALiM
        </div>

        <div style="
            font-size:20px;
            font-weight:600;
            margin-bottom:15px;
        ">
            Sains Adaptive Learning Machine
        </div>

        <div class="hero-desc">
            Sistem pembelajaran adaptif yang membantu siswa
            belajar IPA sesuai dengan tingkat pemahaman,
            kebutuhan, dan perkembangan belajarnya.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🚀 Mulai Perjalanan Belajar")

    col1, col2 = st.columns([1, 1])

    with col1:

        st.markdown("""
        <div class="card">
            <div class="card-title">
                👤 Identitas Siswa
            </div>

            <div class="card-desc">
                Masukkan identitas sebelum memulai
                pembelajaran.
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
            <div class="card-title">
                📚 Pilih Materi
            </div>

            <div class="card-desc">
                Pilih salah satu materi IPA Kelas X
                untuk mengikuti tes diagnostik.
            </div>
        </div>
        """, unsafe_allow_html=True)

        material = st.selectbox(
            "Materi IPA",
            list(MATERIALS.keys())
        )

        if st.button(
            "🚀 Mulai Pembelajaran",
            use_container_width=True
        ):

            if not name.strip():

                st.warning(
                    "Silakan masukkan nama siswa."
                )

            elif not student_code.strip():

                st.warning(
                    "Silakan masukkan kode siswa."
                )

            else:

                st.session_state.name = name.strip()

                st.session_state.student_code = (
                    student_code.strip().upper()
                )

                st.session_state.material = material

                st.session_state.page = "diagnostic"

                st.rerun()

    st.markdown("## 🔬 Materi IPA Kelas X")

    c1, c2, c3 = st.columns(3)

    material_items = list(MATERIALS.items())

    for col, (title, data) in zip(
        [c1, c2, c3],
        material_items
    ):

        with col:

            icon = title.split()[0]
            name_only = title[2:]

            st.markdown(
                f"""
                <div class="material-card">

                    <div class="material-icon">
                        {icon}
                    </div>

                    <div class="material-title">
                        {name_only}
                    </div>

                    <div class="material-text">
                        {data["description"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    footer()


# =========================================================
# DIAGNOSTIC TEST
# =========================================================

elif st.session_state.page == "diagnostic":

    material = st.session_state.material
    questions = MATERIALS[material]["questions"]

    st.title("🧠 Tes Diagnostik")

    st.caption(
        f"{st.session_state.name} • "
        f"{material}"
    )

    st.progress(0.33)

    st.markdown("""
    <div class="card">

        <div class="card-title">
            Mengapa ada tes diagnostik?
        </div>

        <div class="card-desc">
            Tes ini digunakan untuk mengetahui konsep
            yang sudah kamu pahami dan konsep yang masih
            perlu diperkuat.
        </div>

    </div>
    """, unsafe_allow_html=True)

    answers = {}

    for i, q in enumerate(questions):

        st.markdown(
            f"""
            <div class="question-box">

                <div class="question-number">
                    Pertanyaan {i + 1} dari {len(questions)}
                </div>

                <div class="question-text">
                    {q["question"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        answers[i] = st.radio(
            "Pilih jawaban:",
            q["options"],
            key=f"diagnostic_{i}"
        )

        st.write("")

    if st.button(
        "📊 Periksa Jawaban",
        use_container_width=True
    ):

        score = 0

        result_data = []

        for i, q in enumerate(questions):

            selected = answers[i]

            correct = selected == q["answer"]

            if correct:
                score += 1

            result_data.append({
                "selected": selected,
                "correct": correct,
                "answer": q["answer"],
                "explanation": q["explanation"]
            })

        st.session_state.score = score
        st.session_state.answers = result_data

        percentage = int(
            (score / len(questions)) * 100
        )

        if percentage < 50:

            st.session_state.level = "Pemula"
            st.session_state.focus = (
                "Konsep dasar " + material[2:]
            )

        elif percentage < 80:

            st.session_state.level = "Menengah"
            st.session_state.focus = (
                "Pemahaman dan hubungan antar konsep"
            )

        else:

            st.session_state.level = "Mahir"
            st.session_state.focus = (
                "Penerapan konsep dalam situasi nyata"
            )

        st.session_state.page = "feedback"

        st.rerun()

    footer()


# =========================================================
# FEEDBACK JAWABAN
# =========================================================

elif st.session_state.page == "feedback":

    material = st.session_state.material
    questions = MATERIALS[material]["questions"]
    results = st.session_state.answers

    st.title("📝 Hasil Jawaban")

    percentage = int(
        (st.session_state.score / len(questions)) * 100
    )

    st.metric(
        "Skor Diagnostik",
        f"{st.session_state.score}/{len(questions)} "
        f"({percentage}%)"
    )

    st.divider()

    for i, result in enumerate(results):

        st.markdown(
            f"### Pertanyaan {i + 1}"
        )

        if result["correct"]:

            st.success(
                f"✅ Benar — Jawaban: {result['answer']}"
            )

        else:

            st.error(
                f"❌ Kurang tepat — "
                f"Jawaban yang benar: {result['answer']}"
            )

        st.info(
            f"💡 Pembahasan: {result['explanation']}"
        )

    st.divider()

    if st.session_state.level == "Pemula":

        st.warning(
            "Sistem mendeteksi bahwa beberapa konsep dasar "
            "masih perlu diperkuat."
        )

    elif st.session_state.level == "Menengah":

        st.info(
            "Pemahaman dasar sudah cukup baik. "
            "Beberapa konsep perlu diperdalam."
        )

    else:

        st.success(
            "Pemahaman awal sangat baik. "
            "Siswa dapat diarahkan ke penerapan konsep."
        )

    st.markdown("### 🎯 Fokus Pembelajaran")

    st.info(
        st.session_state.focus
    )

    if st.button(
        "🤖 Lanjut ke Pembelajaran Adaptif",
        use_container_width=True
    ):

        st.session_state.page = "tutor"

        st.rerun()

    footer()


# =========================================================
# AI TUTOR
# =========================================================

elif st.session_state.page == "tutor":

    material = st.session_state.material

    st.title("🤖 SALiM AI Tutor")

    st.caption(
        f"{material} • Level {st.session_state.level}"
    )

    st.markdown("""
    <div class="ai-box">

        <div class="ai-label">
            Adaptive Learning
        </div>

        <div class="ai-text">
            Saya sudah mempelajari hasil tes diagnostikmu.
            Sekarang kita akan belajar berdasarkan bagian
            yang masih perlu diperkuat.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎯 Fokus Belajar")

    st.info(
        st.session_state.focus
    )

    st.markdown("### 💬 Diskusi dengan SALiM")

    st.markdown("""
    <div class="card">

        <div class="card-title">
            🤖 SALiM
        </div>

        <p>
            Mari kita mulai dengan berpikir dari kehidupan
            sehari-hari.
        </p>

        <p>
            Menurutmu, mengapa perubahan pada satu komponen
            ekosistem dapat memengaruhi komponen lainnya?
        </p>

        <p style="color:#64748b;">
            Tidak perlu takut salah. Jelaskan dengan
            bahasamu sendiri.
        </p>

    </div>
    """, unsafe_allow_html=True)

    answer = st.text_area(
        "Jawabanmu",
        placeholder="Tuliskan pemikiranmu...",
        height=140
    )

    if st.button(
        "💬 Kirim Jawaban",
        use_container_width=True
    ):

        if not answer.strip():

            st.warning(
                "Silakan tuliskan jawaban terlebih dahulu."
            )

        else:

            st.session_state.tutor_answered = True

            st.success(
                "Jawabanmu sudah diterima."
            )

    if st.session_state.tutor_answered:

        st.markdown("""
        <div class="ai-box">

            <div class="ai-label">
                🤖 SALiM
            </div>

            <div class="ai-text">
                Bagus! Kamu sudah mulai menghubungkan
                perubahan satu komponen dengan kondisi
                komponen lainnya.
            </div>

            <p>
                Sekarang coba berpikir lebih jauh:
                jika jumlah produsen berkurang secara drastis,
                apa yang mungkin terjadi pada konsumen tingkat I?
            </p>

        </div>
        """, unsafe_allow_html=True)

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

    st.markdown("""
    <div class="hero">

        <div class="hero-small">
            Learning Journey Completed
        </div>

        <div class="hero-title">
            🎉 Pembelajaran Selesai
        </div>

        <div class="hero-desc">
            Kamu telah menyelesaikan sesi pembelajaran
            adaptif bersama SALiM.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"## 👋 {st.session_state.name}"
    )

    st.write(
        f"Materi: **{st.session_state.material}**"
    )

    percentage = int(
        (st.session_state.score / 3) * 100
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Pre-test",
            f"{percentage}%"
        )

    with c2:

        st.metric(
            "Post-test",
            "Simulasi 100%"
        )

    with c3:

        improvement = 100 - percentage

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

        <h2>🎯 Rekomendasi SALiM</h2>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.write(
        f"**Level awal:** "
        f"{st.session_state.level}"
    )

    st.write(
        f"**Fokus pembelajaran:** "
        f"{st.session_state.focus}"
    )

    st.success(
        "🟢 Sesi pembelajaran selesai."
    )

    st.info(
        "Pada versi berikutnya, SALiM dapat dihubungkan "
        "dengan AI sungguhan, database siswa, dan analisis "
        "pembelajaran yang lebih mendalam."
    )

    if st.button(
        "🔄 Mulai Pembelajaran Baru",
        use_container_width=True
    ):

        for key in list(defaults.keys()):

            if key != "page" and key in st.session_state:
                del st.session_state[key]

        st.session_state.page = "home"

        st.rerun()

    footer()
