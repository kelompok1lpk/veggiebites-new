import streamlit as st

import streamlit as st

# Ganti dengan direct image URL kamu
background_url = "https://i.ibb.co.com/xqwsXfq8/IMG-0774.jpg"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- SESSION STATE UNTUK NAVIGASI ----------
if 'page' not in st.session_state:
    st.session_state.page = 0

# ---------- HALAMAN-HALAMAN ----------
def halaman_1():
    st.markdown(
        """
        <h1 style="
            font-weight: 1000;
            color: #1A1A1A;
            text-shadow: 1px 1px 3px rgba(255,255,255,0.6);
            background-color: rgba(255, 255, 255, 0.6);
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        ">
            🥦Helloooww welcome at VeggieBites guys!!
        </h1>
        """, 
        unsafe_allow_html=True
    )

    pilihan = st.radio(
        "Kamu termasuk tipe vegetarian yang mana nih?",
        [
            "Lacto-ovo (telur & susu masih aku makan sieh)",
            "Lacto (only susu, telur big no no)",
            "Ovo (telur oke sieh, tapi susu ga dulu deh)",
            "Vegan total (no hewani et all)"
        ]
    )

    if st.button("Next"):
        st.session_state["tipe_vegetarian"] = pilihan
        st.session_state.page += 1
