import streamlit as st

# ============================================================
# SALiM
# Sains Adaptive Learning Machine
# Prototype IPA Kelas X - Kurikulum Merdeka
# ============================================================

st.set_page_config(
    page_title="SALiM | Sains Adaptive Learning Machine",
    page_icon="🧬",
    layout="wide"
)

# ============================================================
# DATA MATERI
# ============================================================

MATERIALS = {
    "🌱 Ekosistem": {
        "description": "Memahami hubungan antara makhluk hidup dan lingkungannya.",
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
                "explanation": "Produsen adalah organisme yang mampu membuat makanan sendiri, terutama melalui fotosintesis. Contohnya adalah tumbuhan hijau."
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
                "explanation": "Belalang merupakan konsumen tingkat I karena memperoleh energi secara langsung dari produsen, yaitu rumput."
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
                "explanation": "Bakteri dan jamur sebagai pengurai menguraikan sisa makhluk hidup sehingga unsur hara dapat kembali ke lingkungan."
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
                "explanation": "Keanekaragaman gen adalah variasi sifat yang terdapat dalam satu spesies. Contohnya adalah berbagai varietas mangga."
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
                "explanation": "Gas rumah kaca seperti karbon dioksida dan metana meningkatkan efek rumah kaca sehingga berkontribusi terhadap pemanasan global."
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


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "name" not in st.session_state:
    st.session_state.name = ""

if "student_code" not in st.session_state:
    st.session_state.student_code = ""

if "material" not in st.session_state:
    st.session_state.material = "🌱 Ekosistem"

if "score" not in st.session_state:
    st.session_state.score = 0

if "answers" not in st.session_state:
    st.session_state.answers = []

if "level" not in st.session_state:
    st.session_state.level = ""

if "focus" not in st.session_state:
    st.session_state.focus = ""

if "tutor_answered" not in st.session_state:
    st.session_state.tutor_answered = False


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f5f7fb;
    }

    .main-title {
        font-size: 44px;
        font-weight: 800;
        color: #172033;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #64748b;
        margin-bottom: 25px;
    }

    .hero {
        padding: 42px;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #172033 0%,
            #26334d 55%,
            #4338ca 100%
        );
        color: white;
        margin-bottom: 30px;
    }

    .hero-label {
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 1.5px;
        color: #c7d2fe;
        text-transform: uppercase;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 800;
        margin-top: 8px;
    }

    .hero-name {
        font-size: 20px;
        font-weight: 600;
        color: #e0e7ff;
    }

    .hero-text {
        font-size: 16px;
        line-height: 1.7;
        color: #cbd5e1;
        max-width: 760px;
        margin-top: 12px;
    }

    .card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 700;
        color: #172033;
        margin-bottom: 8px;
    }

    .card-text {
        color: #64748b;
        line-height: 1.6;
    }

    .material {
        background-color: white;
        padding: 24px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        min-height: 170px;
    }

    .material-icon {
        font-size: 32px;
    }

    .material-title {
        font-size: 19px;
        font-weight: 700;
        color: #172033;
        margin-top: 8px;
    }

    .material-text {
        color: #64748b;
        font-size: 14px;
        line-height: 1.5;
        margin-top: 8px;
    }

    .question {
        background-color: white;
        padding: 28px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .question-label {
        color: #4f46e5;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .question-text {
        color: #172033;
        font-size: 20px;
        font-weight: 700;
        line-height: 1.6;
        margin-top: 8px;
    }

    .ai {
        background-color: #eef2ff;
        padding: 28px;
        border-radius: 20px;
        border: 1px solid #c7d2fe;
        margin: 20px 0;
    }

    .ai-label {
        color: #4f46e5;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    .ai-title {
        color: #1e1b4b;
        font-size: 20px;
        font-weight: 700;
        margin-top: 8px;
        line-height: 1.6;
    }

    .score {
        background-color: white;
        padding: 35px;
        border-radius: 22px;
        border: 1px solid #e2e8f0;
        text-align: center;
        margin-bottom: 25px;
    }

    .score-number {
        font-size: 58px;
        font-weight: 800;
        color: #4f46e5;
    }

    .score-label {
        color: #64748b;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

def show_footer():
    st.divider()

    st.caption(
        "SALiM • Sains Adaptive Learning Machine • "
        "Developed by Tabdulghaffur © 2026"
    )


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "home":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-label">
                IPA Kelas X • Kurikulum Merdeka
            </div>

            <div class="hero-title">
                🧬 SALiM
            </div>

            <div class="hero-name">
                Sains Adaptive Learning Machine
            </div>

            <div class="hero-text">
                Sistem pembelajaran adaptif berbasis kecerdasan
                buatan yang membantu siswa belajar sesuai
                tingkat pemahaman dan kebutuhan belajarnya.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🚀 Mulai Pembelajaran")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    👤 Identitas Siswa
                </div>

                <div class="card-text">
                    Masukkan identitas sebelum memulai
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

        student_code = st.text_input(
            "Kode siswa",
            placeholder="Contoh: S001"
        )

    with col2:

        st.markdown(
            """
            <div class="card">

                <div class="card-title">
                    📚 Pilih Materi
                </div>

                <div class="card-text">
                    Pilih salah satu materi IPA Kelas X
                    untuk memulai tes diagnostik.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        material = st.selectbox(
            "Materi IPA",
            list(MATERIALS.keys())
        )

        if st.button(
            "🚀 Mulai Pembelajaran",
            use_container_width=True
        ):

            if name.strip() == "":
                st.warning(
                    "Silakan masukkan nama siswa."
                )

            elif student_code.strip() == "":
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

    columns = st.columns(3)

    for column, (material_name, data) in zip(
        columns,
        MATERIALS.items()
    ):

        with column:

            icon = material_name[:2]
            title = material_name[2:]

            st.markdown(
                f"""
                <div class="material">

                    <div class="material-icon">
                        {icon}
                    </div>

                    <div class="material-title">
                        {title}
                    </div>

                    <div class="material-text">
                        {data["description"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    show_footer()


# ============================================================
# DIAGNOSTIC
# ============================================================

elif st.session_state.page == "diagnostic":

    material = st.session_state.material

    questions = MATERIALS[material]["questions"]

    st.title("🧠 Tes Diagnostik")

    st.caption(
        f"Siswa: {st.session_state.name}  •  "
        f"Materi: {material}"
    )

    st.progress(0.33)

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🎯 Tujuan Tes
            </div>

            <div class="card-text">
                Tes ini digunakan untuk mengetahui
                pemahaman awalmu. Hasilnya akan digunakan
                SALiM untuk menentukan fokus pembelajaran.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    selected_answers = []

    for index, question in enumerate(questions):

        st.markdown(
            f"""
            <div class="question">

                <div class="question-label">
                    Pertanyaan {index + 1} dari 3
                </div>

                <div class="question-text">
                    {question["question"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        selected = st.radio(
            "Pilih jawaban:",
            question["options"],
            key=f"answer_{index}"
        )

        selected_answers.append(selected)

    st.write("")

    if st.button(
        "📊 Periksa Jawaban",
        use_container_width=True
    ):

        score = 0
        results = []

        for index, question in enumerate(questions):

            selected = selected_answers[index]

            correct = (
                selected == question["answer"]
            )

            if correct:
                score += 1

            results.append(
                {
                    "selected": selected,
                    "correct": correct,
                    "answer": question["answer"],
                    "explanation": question["explanation"]
                }
            )

        st.session_state.score = score
        st.session_state.answers = results

        percentage = int(
            (score / 3) * 100
        )

        if percentage < 50:

            st.session_state.level = "Pemula"

            st.session_state.focus = (
                "Memperkuat konsep dasar "
                + material[2:]
            )

        elif percentage < 80:

            st.session_state.level = "Menengah"

            st.session_state.focus = (
                "Memperkuat hubungan antar konsep "
                "dan penerapannya"
            )

        else:

            st.session_state.level = "Mahir"

            st.session_state.focus = (
                "Penerapan konsep dalam situasi nyata "
                "dan soal tingkat tinggi"
            )

        st.session_state.page = "feedback"

        st.rerun()

    show_footer()


# ============================================================
# FEEDBACK
# ============================================================

elif st.session_state.page == "feedback":

    st.title("📝 Hasil Tes Diagnostik")

    score = st.session_state.score

    percentage = int(
        (score / 3) * 100
    )

    st.markdown(
        f"""
        <div class="score">

            <div class="score-number">
                {percentage}%
            </div>

            <div class="score-label">
                Skor Diagnostik
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        f"**{st.session_state.name}**, berikut hasil "
        "jawabanmu:"
    )

    for index, result in enumerate(
        st.session_state.answers
    ):

        st.markdown(
            f"### Pertanyaan {index + 1}"
        )

        st.write(
            f"**Jawabanmu:** {result['selected']}"
        )

        if result["correct"]:

            st.success(
                "✅ Jawaban benar!"
            )

        else:

            st.error(
                f"❌ Jawaban kurang tepat. "
                f"Jawaban yang benar: "
                f"{result['answer']}"
            )

        st.info(
            f"💡 **Pembahasan:** "
            f"{result['explanation']}"
        )

    st.divider()

    st.subheader("🧠 Analisis SALiM")

    if st.session_state.level == "Pemula":

        st.warning(
            "Pemahaman dasar masih perlu diperkuat."
        )

    elif st.session_state.level == "Menengah":

        st.info(
            "Pemahaman dasar sudah cukup baik, "
            "tetapi beberapa konsep perlu diperdalam."
        )

    else:

        st.success(
            "Pemahaman awal sudah baik. "
            "Siswa dapat diarahkan pada penerapan konsep."
        )

    st.markdown("### 🎯 Fokus Pembelajaran")

    st.info(
        st.session_state.focus
    )

    if st.button(
        "🤖 Lanjut ke SALiM AI Tutor",
        use_container_width=True
    ):

        st.session_state.page = "tutor"

        st.rerun()

    show_footer()


# ============================================================
# AI TUTOR
# ============================================================

elif st.session_state.page == "tutor":

    st.title("🤖 SALiM AI Tutor")

    st.caption(
        f"{st.session_state.material} • "
        f"Level: {st.session_state.level}"
    )

    st.markdown(
        """
        <div class="ai">

            <div class="ai-label">
                Adaptive Learning
            </div>

            <div class="ai-title">
                Halo! Saya SALiM.
            </div>

            <p>
                Saya sudah melihat hasil tes diagnostikmu.
                Sekarang kita akan belajar berdasarkan
                konsep yang masih perlu diperkuat.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🎯 Fokus Belajarmu")

    st.info(
        st.session_state.focus
    )

    st.markdown("### 💬 Pertanyaan SALiM")

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🤖 SALiM bertanya:
            </div>

            <p>
                Bayangkan terjadi perubahan besar pada
                lingkungan di sekitarmu.
                Menurutmu, bagaimana perubahan tersebut
                dapat memengaruhi makhluk hidup yang ada
                di dalamnya?
            </p>

            <p style="color:#64748b;">
                Jelaskan dengan bahasamu sendiri.
                Tidak perlu takut salah.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    tutor_answer = st.text_area(
        "Jawabanmu",
        placeholder=(
            "Tuliskan pendapatmu di sini..."
        ),
        height=150
    )

    if st.button(
        "💬 Kirim Jawaban",
        use_container_width=True
    ):

        if tutor_answer.strip() == "":

            st.warning(
                "Silakan tuliskan jawaban terlebih dahulu."
            )

        else:

            st.session_state.tutor_answered = True

            st.success(
                "Jawaban berhasil dikirim."
            )

    if st.session_state.tutor_answered:

        st.markdown(
            """
            <div class="ai">

                <div class="ai-label">
                    🤖 SALiM memberikan umpan balik
                </div>

                <div class="ai-title">
                    Bagus! Kamu sudah mulai
                    menghubungkan perubahan lingkungan
                    dengan kehidupan organisme.
                </div>

                <p>
                    Sekarang coba berpikir lebih mendalam.
                    Jika jumlah produsen dalam suatu
                    ekosistem berkurang secara drastis,
                    apa yang mungkin terjadi pada konsumen
                    tingkat pertama? Jelaskan alasannya.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    if st.button(
        "🎯 Selesaikan Pembelajaran",
        use_container_width=True
    ):

        st.session_state.page = "result"

        st.rerun()

    show_footer()


# ============================================================
# RESULT
# ============================================================

elif st.session_state.page == "result":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-label">
                Learning Journey Completed
            </div>

            <div class="hero-title">
                🎉 Pembelajaran Selesai
            </div>

            <div class="hero-text">
                Kamu telah menyelesaikan sesi pembelajaran
                bersama SALiM.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"## 👋 {st.session_state.name}"
    )

    st.write(
        f"Materi yang dipelajari: "
        f"**{st.session_state.material}**"
    )

    percentage = int(
        (st.session_state.score / 3) * 100
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Pre-test",
            f"{percentage}%"
        )

    with col2:

        st.metric(
            "Level Awal",
            st.session_state.level
        )

    with col3:

        st.metric(
            "Fokus Belajar",
            "Adaptif"
        )

    st.write("")

    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🎯 Ringkasan Pembelajaran
            </div>

            <p>
                SALiM menganalisis hasil tes diagnostik
                kemudian menentukan fokus pembelajaran
                berdasarkan kemampuan awal siswa.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        f"Rekomendasi SALiM: "
        f"{st.session_state.focus}"
    )

    st.success(
        "🟢 Sesi pembelajaran telah selesai."
    )

    st.warning(
        "Prototype ini masih menggunakan simulasi AI. "
        "Pada tahap berikutnya, SALiM dapat dihubungkan "
        "dengan model AI sungguhan dan database siswa."
    )

    if st.button(
        "🔄 Mulai Pembelajaran Baru",
        use_container_width=True
    ):

        st.session_state.clear()

        st.session_state.page = "home"

        st.rerun()

    show_footer()
