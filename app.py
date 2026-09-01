import streamlit as st

# ============================================================
# SALiM - Sains Adaptive Learning Machine
# Prototype Pembelajaran IPA Kelas X
# ============================================================

st.set_page_config(
    page_title="SALiM | IPA Kelas X",
    page_icon="🧬",
    layout="wide"
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>
    .stApp {
        background: #f5f7fb;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #172033;
    }

    .hero {
        background: linear-gradient(135deg, #172033, #3730a3);
        padding: 40px;
        border-radius: 24px;
        color: white;
        margin-bottom: 30px;
    }

    .hero-small {
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 1px;
        color: #c7d2fe;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 800;
        margin-top: 8px;
    }

    .hero-subtitle {
        font-size: 20px;
        font-weight: 600;
        color: #e0e7ff;
    }

    .hero-description {
        font-size: 16px;
        color: #cbd5e1;
        line-height: 1.7;
        margin-top: 12px;
    }

    .card {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 700;
        color: #172033;
    }

    .card-text {
        color: #64748b;
        line-height: 1.6;
    }

    .question-box {
        background: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    .question-number {
        color: #4f46e5;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 1px;
    }

    .question-text {
        color: #172033;
        font-size: 19px;
        font-weight: 700;
        line-height: 1.6;
        margin-top: 8px;
    }

    .result-box {
        background: white;
        padding: 35px;
        border-radius: 22px;
        border: 1px solid #e2e8f0;
        text-align: center;
        margin: 20px 0;
    }

    .score {
        font-size: 55px;
        font-weight: 800;
        color: #4f46e5;
    }

    .footer {
        text-align: center;
        color: #64748b;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# DATA MATERI
# ============================================================

MATERI = {
    "🌱 Ekosistem": {
        "deskripsi": "Mempelajari hubungan antara makhluk hidup dan lingkungannya.",
        "soal": [
            {
                "tanya": "Organisme yang mampu membuat makanan sendiri melalui fotosintesis disebut...",
                "pilihan": [
                    "Konsumen",
                    "Produsen",
                    "Pengurai",
                    "Detritivor"
                ],
                "jawaban": "Produsen",
                "bahas": "Produsen adalah organisme yang mampu membuat makanan sendiri, terutama melalui fotosintesis. Contohnya adalah tumbuhan hijau."
            },
            {
                "tanya": "Pada rantai makanan Rumput → Belalang → Katak → Ular, organisme yang memperoleh energi langsung dari rumput adalah...",
                "pilihan": [
                    "Rumput",
                    "Belalang",
                    "Katak",
                    "Ular"
                ],
                "jawaban": "Belalang",
                "bahas": "Belalang merupakan konsumen tingkat pertama karena mendapatkan energi langsung dari produsen, yaitu rumput."
            },
            {
                "tanya": "Apa fungsi utama organisme pengurai dalam ekosistem?",
                "pilihan": [
                    "Menghasilkan energi matahari",
                    "Menghasilkan oksigen",
                    "Menguraikan sisa organisme",
                    "Menghentikan rantai makanan"
                ],
                "jawaban": "Menguraikan sisa organisme",
                "bahas": "Pengurai seperti bakteri dan jamur menguraikan sisa makhluk hidup sehingga unsur hara dapat kembali ke lingkungan."
            }
        ]
    },

    "🧬 Keanekaragaman Hayati": {
        "deskripsi": "Mengenal tingkat keanekaragaman hayati dan pentingnya pelestarian.",
        "soal": [
            {
                "tanya": "Keanekaragaman yang terjadi karena adanya variasi dalam satu spesies disebut keanekaragaman tingkat...",
                "pilihan": [
                    "Gen",
                    "Jenis",
                    "Ekosistem",
                    "Bioma"
                ],
                "jawaban": "Gen",
                "bahas": "Keanekaragaman gen adalah variasi sifat yang terdapat dalam satu spesies. Contohnya berbagai varietas mangga."
            },
            {
                "tanya": "Contoh keanekaragaman hayati tingkat jenis adalah...",
                "pilihan": [
                    "Mangga manalagi dan mangga golek",
                    "Kucing dan harimau",
                    "Padi merah dan padi putih",
                    "Kelapa hijau dan kelapa gading"
                ],
                "jawaban": "Kucing dan harimau",
                "bahas": "Kucing dan harimau merupakan organisme dari jenis yang berbeda sehingga termasuk keanekaragaman tingkat jenis."
            },
            {
                "tanya": "Pelestarian badak Jawa di Taman Nasional Ujung Kulon merupakan contoh konservasi...",
                "pilihan": [
                    "Ex situ",
                    "In situ",
                    "Buatan",
                    "Laboratorium"
                ],
                "jawaban": "In situ",
                "bahas": "Konservasi in situ dilakukan dengan melestarikan organisme di habitat alaminya."
            }
        ]
    },

    "🌍 Perubahan Lingkungan": {
        "deskripsi": "Menganalisis penyebab, dampak, dan solusi perubahan lingkungan.",
        "soal": [
            {
                "tanya": "Salah satu penyebab utama pencemaran udara di wilayah perkotaan adalah...",
                "pilihan": [
                    "Fotosintesis tumbuhan",
                    "Emisi kendaraan bermotor",
                    "Penguapan air",
                    "Pelapukan batuan"
                ],
                "jawaban": "Emisi kendaraan bermotor",
                "bahas": "Gas buang kendaraan bermotor mengandung berbagai polutan yang dapat menurunkan kualitas udara."
            },
            {
                "tanya": "Peningkatan konsentrasi gas rumah kaca di atmosfer dapat menyebabkan...",
                "pilihan": [
                    "Pemanasan global",
                    "Berkurangnya gravitasi bumi",
                    "Berhentinya siklus air",
                    "Hilangnya seluruh oksigen"
                ],
                "jawaban": "Pemanasan global",
                "bahas": "Peningkatan gas rumah kaca memperkuat efek rumah kaca dan berkontribusi terhadap pemanasan global."
            },
            {
                "tanya": "Tindakan yang paling tepat untuk mengurangi sampah plastik adalah...",
                "pilihan": [
                    "Menggunakan plastik sekali pakai lebih banyak",
                    "Membakar semua plastik",
                    "Mengurangi penggunaan plastik sekali pakai",
                    "Membuang plastik ke sungai"
                ],
                "jawaban": "Mengurangi penggunaan plastik sekali pakai",
                "bahas": "Mengurangi penggunaan plastik sekali pakai merupakan salah satu langkah paling efektif untuk mengurangi timbulan sampah plastik."
            }
        ]
    }
}


# ============================================================
# SESSION STATE
# ============================================================

if "halaman" not in st.session_state:
    st.session_state.halaman = "home"

if "nama" not in st.session_state:
    st.session_state.nama = ""

if "kode" not in st.session_state:
    st.session_state.kode = ""

if "materi" not in st.session_state:
    st.session_state.materi = "🌱 Ekosistem"

if "hasil" not in st.session_state:
    st.session_state.hasil = []

if "skor" not in st.session_state:
    st.session_state.skor = 0

if "level" not in st.session_state:
    st.session_state.level = ""

if "jawaban_tutor" not in st.session_state:
    st.session_state.jawaban_tutor = ""


# ============================================================
# FOOTER
# ============================================================

def footer():
    st.markdown(
        '<div class="footer">SALiM • Sains Adaptive Learning Machine<br>'
        'Developed by Tabdulghaffur © 2026</div>',
        unsafe_allow_html=True
    )


# ============================================================
# HALAMAN HOME
# ============================================================

if st.session_state.halaman == "home":

    st.markdown(
        '<div class="hero">'
        '<div class="hero-small">IPA KELAS X • KURIKULUM MERDEKA</div>'
        '<div class="hero-title">🧬 SALiM</div>'
        '<div class="hero-subtitle">Sains Adaptive Learning Machine</div>'
        '<div class="hero-description">'
        'Sistem pembelajaran adaptif yang membantu siswa '
        'belajar IPA sesuai tingkat pemahaman, kebutuhan, '
        'dan perkembangan belajarnya.'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )

    st.header("🚀 Mulai Pembelajaran")

    kiri, kanan = st.columns(2)

    with kiri:

        st.subheader("👤 Identitas Siswa")

        st.write(
            "Masukkan identitas sebelum memulai pembelajaran."
        )

        nama = st.text_input(
            "Nama siswa",
            placeholder="Contoh: Ahmad"
        )

        kode = st.text_input(
            "Kode siswa",
            placeholder="Contoh: S001"
        )

    with kanan:

        st.subheader("📚 Pilih Materi")

        st.write(
            "Pilih materi IPA Kelas X yang akan dipelajari."
        )

        materi = st.selectbox(
            "Materi",
            list(MATERI.keys())
        )

        st.write("")

        if st.button(
            "🚀 Mulai Pembelajaran",
            type="primary",
            use_container_width=True
        ):

            if not nama.strip():
                st.warning("Silakan masukkan nama siswa.")

            elif not kode.strip():
                st.warning("Silakan masukkan kode siswa.")

            else:

                st.session_state.nama = nama.strip()
                st.session_state.kode = kode.strip().upper()
                st.session_state.materi = materi
                st.session_state.halaman = "diagnostik"

                st.rerun()

    st.divider()

    st.header("🔬 Materi IPA Kelas X")

    kolom = st.columns(3)

    for i, (nama_materi, data) in enumerate(MATERI.items()):

        with kolom[i]:

            st.markdown(
                '<div class="card">',
                unsafe_allow_html=True
            )

            st.subheader(nama_materi)

            st.write(data["deskripsi"])

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

    footer()


# ============================================================
# TES DIAGNOSTIK
# ============================================================

elif st.session_state.halaman == "diagnostik":

    st.title("🧠 Tes Diagnostik")

    st.write(
        f"**Siswa:** {st.session_state.nama}"
    )

    st.write(
        f"**Kode:** {st.session_state.kode}"
    )

    st.write(
        f"**Materi:** {st.session_state.materi}"
    )

    st.progress(0.33)

    st.info(
        "Jawablah ketiga pertanyaan berikut. "
        "Hasil tes digunakan SALiM untuk menentukan "
        "fokus pembelajaran."
    )

    soal = MATERI[
        st.session_state.materi
    ]["soal"]

    jawaban_siswa = []

    for i, q in enumerate(soal):

        st.markdown(
            '<div class="question-box">',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="question-number">'
            f'PERTANYAAN {i + 1} DARI 3'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="question-text">'
            f'{q["tanya"]}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        pilihan = st.radio(
            "Pilih jawaban:",
            q["pilihan"],
            key=f"soal_{i}"
        )

        jawaban_siswa.append(pilihan)

    st.write("")

    if st.button(
        "📊 Periksa Jawaban",
        type="primary",
        use_container_width=True
    ):

        skor = 0
        hasil = []

        for i, q in enumerate(soal):

            benar = (
                jawaban_siswa[i] == q["jawaban"]
            )

            if benar:
                skor += 1

            hasil.append(
                {
                    "nomor": i + 1,
                    "jawaban": jawaban_siswa[i],
                    "benar": benar,
                    "kunci": q["jawaban"],
                    "bahasan": q["bahas"]
                }
            )

        st.session_state.skor = skor
        st.session_state.hasil = hasil

        nilai = (skor / 3) * 100

        if nilai < 50:
            st.session_state.level = "Pemula"

        elif nilai < 80:
            st.session_state.level = "Menengah"

        else:
            st.session_state.level = "Mahir"

        st.session_state.halaman = "hasil"

        st.rerun()

    footer()


# ============================================================
# HASIL TES
# ============================================================

elif st.session_state.halaman == "hasil":

    st.title("📊 Hasil Tes Diagnostik")

    nilai = int(
        (st.session_state.skor / 3) * 100
    )

    st.markdown(
        '<div class="result-box">',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="score">{nilai}</div>',
        unsafe_allow_html=True
    )

    st.write("Nilai diagnostik")

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Jawaban Benar",
            f"{st.session_state.skor}/3"
        )

    with col2:
        st.metric(
            "Nilai",
            f"{nilai}"
        )

    with col3:
        st.metric(
            "Level",
            st.session_state.level
        )

    st.divider()

    st.subheader("📝 Pembahasan Jawaban")

    for hasil in st.session_state.hasil:

        st.markdown(
            f"### Pertanyaan {hasil['nomor']}"
        )

        st.write(
            f"**Jawaban siswa:** "
            f"{hasil['jawaban']}"
        )

        if hasil["benar"]:

            st.success(
                "✅ Jawaban benar!"
            )

        else:

            st.error(
                f"❌ Jawaban belum tepat. "
                f"Jawaban yang benar: "
                f"{hasil['kunci']}"
            )

        st.info(
            f"💡 **Pembahasan:** "
            f"{hasil['bahasan']}"
        )

    st.divider()

    st.subheader("🧠 Analisis SALiM")

    if st.session_state.level == "Pemula":

        st.warning(
            "Pemahaman konsep dasar masih perlu diperkuat."
        )

        fokus = (
            "Memahami konsep dasar dan istilah penting "
            "dalam materi."
        )

    elif st.session_state.level == "Menengah":

        st.info(
            "Pemahaman dasar sudah cukup baik, "
            "tetapi masih perlu pendalaman."
        )

        fokus = (
            "Menghubungkan beberapa konsep dan "
            "menerapkannya dalam situasi sederhana."
        )

    else:

        st.success(
            "Pemahaman awal sangat baik."
        )

        fokus = (
            "Menerapkan konsep pada permasalahan "
            "dan situasi kehidupan nyata."
        )

    st.subheader("🎯 Rekomendasi Pembelajaran")

    st.write(fokus)

    if st.button(
        "🤖 Lanjut ke SALiM AI Tutor",
        type="primary",
        use_container_width=True
    ):

        st.session_state.halaman = "tutor"

        st.rerun()

    footer()


# ============================================================
# AI TUTOR
# ============================================================

elif st.session_state.halaman == "tutor":

    st.title("🤖 SALiM AI Tutor")

    st.caption(
        f"{st.session_state.materi} • "
        f"Level awal: {st.session_state.level}"
    )

    st.info(
        "SALiM menyesuaikan pembelajaran berdasarkan "
        "hasil tes diagnostikmu."
    )

    st.subheader("🎯 Fokus Pembelajaran")

    if st.session_state.level == "Pemula":

        st.write(
            "Kita akan memperkuat konsep dasar terlebih dahulu."
        )

    elif st.session_state.level == "Menengah":

        st.write(
            "Kita akan memperdalam hubungan antar konsep."
        )

    else:

        st.write(
            "Kita akan mengembangkan kemampuan penerapan "
            "dan berpikir kritis."
        )

    st.divider()

    st.subheader("💬 Pertanyaan dari SALiM")

    st.write(
        "Menurutmu, mengapa keseimbangan dalam suatu "
        "ekosistem penting bagi kehidupan makhluk hidup?"
    )

    jawaban = st.text_area(
        "Tuliskan jawabanmu:",
        placeholder="Tulis jawaban dengan bahasamu sendiri...",
        height=150
    )

    if st.button(
        "💬 Kirim Jawaban",
        type="primary",
        use_container_width=True
    ):

        if not jawaban.strip():

            st.warning(
                "Silakan tuliskan jawaban terlebih dahulu."
            )

        else:

            st.session_state.jawaban_tutor = jawaban

            st.success(
                "Jawaban berhasil dikirim ke SALiM."
            )

            st.subheader("🤖 Umpan Balik SALiM")

            st.write(
                "Bagus! Kamu sudah mencoba menghubungkan "
                "keseimbangan ekosistem dengan kehidupan "
                "makhluk hidup."
            )

            st.info(
                "Coba pikirkan lebih lanjut: apa yang terjadi "
                "jika salah satu populasi dalam rantai makanan "
                "menurun secara drastis?"
            )

    st.divider()

    if st.button(
        "🏁 Selesaikan Pembelajaran",
        use_container_width=True
    ):

        st.session_state.halaman = "selesai"

        st.rerun()

    footer()


# ============================================================
# SELESAI
# ============================================================

elif st.session_state.halaman == "selesai":

    st.markdown(
        '<div class="hero">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-small">'
        'LEARNING JOURNEY COMPLETED'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-title">'
        '🎉 Pembelajaran Selesai'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-description">'
        'Terima kasih telah belajar bersama SALiM.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.subheader(
        f"👋 Sampai jumpa, {st.session_state.nama}!"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Nilai Diagnostik",
            f"{int((st.session_state.skor / 3) * 100)}"
        )

    with col2:
        st.metric(
            "Level",
            st.session_state.level
        )

    with col3:
        st.metric(
            "Materi",
            st.session_state.materi.split(" ", 1)[1]
        )

    st.success(
        "🟢 Sesi pembelajaran SALiM telah selesai."
    )

    st.info(
        "Prototype berikutnya dapat dikembangkan dengan "
        "AI sungguhan, database hasil belajar, pre-test, "
        "post-test, dan dashboard guru."
    )

    if st.button(
        "🔄 Kembali ke Halaman Awal",
        type="primary",
        use_container_width=True
    ):

        st.session_state.clear()

        st.session_state.halaman = "home"

        st.rerun()

    footer()
