import streamlit as st

st.session_state.page -= 1

def card_menu(judul, bahan, cocok):
    st.markdown(f"""
    <div style="
        border: 2px solid #f0c0d0;
        background-color: #fff0f5;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    ">
        <h4 style="margin-bottom:5px;">{judul}</h4>
        <p><b>Bahan:</b> {bahan}</p>
        <p><i>{cocok}</i></p>
    </div>
    """, unsafe_allow_html=True)

def halaman_3():
    tipe = st.session_state.get("tipe_vegetarian", "")
    st.title("🍽️ Rekomendasi Menu Buat Kamu!")

    if "Lacto-ovo" in tipe:
        st.subheader("🥚🍶 Menu untuk Lacto-Ovo Vegetarian")
        card_menu("🍳 Omelet Sayur", "Telur, bayam, keju, tomat", "Cocok untuk Lacto-Ovo")
        card_menu("🍓 Yoghurt Buah Granola", "Yoghurt, granola, buah segar", "Cocok untuk Lacto-Ovo")
        card_menu("🍝 Lasagna Keju & Sayur", "Pasta, keju, zucchini, saus tomat", "Cocok untuk Lacto-Ovo")
        card_menu("🥞 Pancake Pisang", "Pisang, telur, oat, susu", "Cocok untuk Lacto-Ovo")
        card_menu("🥯 Sandwich Telur & Keju", "Roti gandum, telur, keju", "Cocok untuk Lacto-Ovo")
        card_menu("🍛 Nasi Kari Tempe", "Tempe, kari, nasi", "Cocok untuk Lacto-Ovo")
        card_menu("🍮 Pudding Susu Cokelat", "Susu, agar, cokelat bubuk", "Cocok untuk Lacto-Ovo")

    elif "Lacto" in tipe:
        st.subheader("🥛 Menu untuk Lacto Vegetarian")
        card_menu("🧀 Tumis Brokoli Keju", "Brokoli, keju cheddar, bawang putih", "Cocok untuk Lacto")
        card_menu("🍨 Smoothie Susu Almond", "Susu almond, pisang, stroberi", "Cocok untuk Lacto")
        card_menu("🥗 Salad Sayur + Keju", "Selada, wortel, keju parut, tomat", "Cocok untuk Lacto")
        card_menu("🥣 Oatmeal Susu & Madu", "Oat, susu, madu, kayu manis", "Cocok untuk Lacto")
        card_menu("🍠 Sup Kentang Creamy", "Kentang, wortel, susu, daun bawang", "Cocok untuk Lacto")
        card_menu("🍕 Roti Pizza Mini", "Roti gandum, keju, saus tomat, sayuran", "Cocok untuk Lacto")
        card_menu("🧁 Muffin Susu & Kismis", "Tepung, susu, kismis, baking powder", "Cocok untuk Lacto")

    elif "Ovo" in tipe:
        st.subheader("🥚 Menu untuk Ovo Vegetarian")
        card_menu("🍳 Scrambled Egg Sayur", "Telur, bayam, tomat, jamur", "Cocok untuk Ovo")
        card_menu("🥑 Avocado Egg Toast", "Roti panggang, telur rebus, alpukat", "Cocok untuk Ovo")
        card_menu("🍜 Mie Sayur + Telur", "Mie telur, wortel, sawi, telur rebus", "Cocok untuk Ovo")
        card_menu("🍘 Nasi Goreng Telur", "Nasi, kecap, telur, buncis", "Cocok untuk Ovo")
        card_menu("🍛 Tahu Telur Saus Teriyaki", "Tahu, telur, kecap manis", "Cocok untuk Ovo")
        card_menu("🥪 Roti Lapis Telur", "Roti, telur dadar, tomat", "Cocok untuk Ovo")
        card_menu("🧁 Kue Telur Kukus", "Telur, gula, terigu, vanila", "Cocok untuk Ovo")

    elif "Vegan" in tipe:
        st.subheader("🌱 Menu untuk Vegan Total")
        card_menu("🥗 Quinoa Salad", "Quinoa, tomat, mentimun, olive oil", "Cocok untuk Vegan")
        card_menu("🍜 Sup Miso + Tofu", "Kaldu miso, tofu, rumput laut", "Cocok untuk Vegan")
        card_menu("🌯 Veggie Wrap", "Tortilla, hummus, sayur mentah", "Cocok untuk Vegan")
        card_menu("🍚 Nasi Tofu Lada Hitam", "Nasi, tahu, lada hitam, paprika", "Cocok untuk Vegan")
        card_menu("🥞 Pancake Vegan", "Oat, pisang, baking powder", "Cocok untuk Vegan")
        card_menu("🍝 Pasta Jamur Vegan", "Pasta, jamur, saus tomat", "Cocok untuk Vegan")
        card_menu("🍪 Cookies Vegan", "Oat, selai kacang, pisang", "Cocok untuk Vegan")

    else:
        st.warning("Kamu belum pilih tipe vegetarian. Balik ke halaman awal dulu yuk!")

    # Navigasi
    if st.button("Next"):
        st.session_state.page += 1
    if st.button("Back"):
        st.session_state.page -= 1

def halaman_4():
    tipe = st.session_state.get("tipe_vegetarian", "")
    st.title("Butuh Pengganti Bahan?")
    st.markdown(f"Kamu tipe: **{tipe}** 🌿")

    st.markdown("Masukkan bahan yang ingin diganti, nanti kita bantu kasih alternatifnya ya!")
    
    if "hasil_pengganti" not in st.session_state:
        st.session_state.hasil_pengganti = ""
    if "bahan_input" not in st.session_state:
        st.session_state.bahan_input = ""

    st.session_state.bahan_input = st.text_input("Masukkan nama bahan yang mau diganti:", value=st.session_state.bahan_input)

    if st.button("Search"):
        bahan = st.session_state.bahan_input.lower()
        pengganti = {
            "susu": "susu almond / oat milk",
            "telur": "chia egg (chia + air)",
            "daging": "jamur, tempe, atau tofu",
            "keju": "keju vegan berbasis kacang",
            "daging sapi": "tempe, tahu, jamur tiram, jackfruit, seitan",
            "daging ayam": "tempe, tahu, jamur tiram, jackfruit, seitan",
            "daging giling": "kacang hitam, kacang merah, walnut cincang, tahu hancur",
            "susu sapi": "susu almond, susu kedelai, oat milk, coconut milk",
            "keju cheddar": "keju vegan, nutritional yeast",
            "parmesan": "nutritional yeast, kacang mete blend",
            "cream cheese": "tahu sutra + lemon + garam (di-blend)",
            "mentega": "minyak kelapa, margarin vegan, alpukat",
            "mayones": "mayones vegan, tofu + mustard + lemon",
        }
        hasil = pengganti.get(bahan, "Bahan yang kamu cari belum ada di daftar. Coba bahan lain yuk!")
        st.session_state.hasil_pengganti = f"Pengganti untuk {bahan}: {hasil}"

    if st.session_state.hasil_pengganti:
        st.success(st.session_state.hasil_pengganti)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back", key="back4"):
            st.session_state.page -= 1
            st.session_state.hasil_pengganti = ""
    with col2:
        if st.button("Next", key="next4"):
            st.session_state.page += 1
            st.session_state.hasil_pengganti = ""
import streamlit.components.v1 as components

def halaman_5():
    st.title("🥦Terima Kasih Sudah Mampir di VeggieBites!!💚")

    # Ledakan sayur tanpa henti pakai JS + HTML
    components.html(
        """
        <style>
        body {
            overflow: hidden;
            margin: 0;
            padding: 0;
        }
        .sayur {
            position: fixed;
            width: 50px;
            height: 50px;
            pointer-events: none;
            z-index: 9999;
            animation: explode 1.5s linear forwards;
        }

        @keyframes explode {
            0% { transform: translate(0, 0) scale(0.2) rotate(0deg); opacity: 0; }
            30% { opacity: 1; transform: scale(1.2) rotate(180deg); }
            100% { 
                transform: translate(var(--x), var(--y)) rotate(720deg); 
                opacity: 0; 
            }
        }
        </style>

        <script>
        const icons = [
            "https://img.icons8.com/color/96/000000/carrot.png",
            "https://img.icons8.com/color/96/000000/broccoli.png",
            "https://img.icons8.com/color/96/000000/tomato.png",
            "https://img.icons8.com/color/96/000000/cucumber.png",
            "https://img.icons8.com/color/96/000000/peas.png",
            "https://img.icons8.com/color/96/000000/eggplant.png"
        ];

        function explodeSayur() {
            const sayur = document.createElement("img");
            sayur.src = icons[Math.floor(Math.random() * icons.length)];
            sayur.className = "sayur";
            const x = (Math.random() - 0.5) * window.innerWidth * 1.2;
            const y = (Math.random() - 0.5) * window.innerHeight * 1.2;
            sayur.style.left = `${Math.random() * window.innerWidth}px`;
            sayur.style.top = `${Math.random() * window.innerHeight}px`;
            sayur.style.setProperty('--x', `${x}px`);
            sayur.style.setProperty('--y', `${y}px`);
            document.body.appendChild(sayur);
            setTimeout(() => document.body.removeChild(sayur), 2000);
        }

        setInterval(explodeSayur, 300); // meletup tiap 0.3 detik terus-menerus
        </script>
        """,
        height=200
    )

    st.markdown("🌽Semoga sehat selalu dan makin happy bareng VeggieBites yaa!! 🥗💚")
    if st.button("Back"):
        st.session_state.page -= 1

# ini juga
halaman_fungsi = [halaman_1, halaman_2, halaman_3, halaman_4, halaman_5]

# tambahin nih
halaman_fungsi[st.session_state.page]()
