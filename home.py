import streamlit as st
import os

# ---- Page Configuration ----
st.set_page_config(page_title="IdentiFace", layout="wide")

# ---- Set Background from Unsplash ----
def set_online_background(image_url):
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        html, body, [class*="st-"] {{
            font-family: 'Roboto', sans-serif;
        }}

        .stApp {{
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.7)), url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }}

        .banner {{
            text-align: center;
            padding: 4rem 2rem;
            background-color: rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            margin: 6rem auto;
            width: 75%;
            box-shadow: 0 8px 30px rgba(0,0,0,0.4);
            backdrop-filter: blur(4px);
        }}

        .quote {{
            margin-top: 2rem;
            font-size: 1.5rem;
            color: #ffffff;
            font-weight: 600;
        }}

        .subtext {{
            font-size: 1.1rem;
            color: #dddddd;
            margin-top: 0.5rem;
        }}

        .login-btn {{
            background-color: #0072CE;
            color: white;
            font-size: 1.2rem;
            padding: 0.8rem 2rem;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s ease;
        }}

        .login-btn:hover {{
            background-color: #005ba1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---- Set Background Image ----
set_online_background("https://images.unsplash.com/photo-1571260899304-425eee4c7efc?auto=format&fit=crop&w=1950&q=80")

# ---- Hero Banner Content ----
st.markdown("<div class='banner'>", unsafe_allow_html=True)
st.markdown("<h1>Welcome to <span style='color:#00FFAA;'>IdentiFace</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.2rem;'>AI-Powered Face Recognition Attendance System</p>", unsafe_allow_html=True)

# ---- Add Tagline & Subtext ----
st.markdown("""
    <div class="quote">“Smarter Attendance for a Smarter Tomorrow”</div>
    <div class="subtext">Experience a new way of tracking presence — fast, reliable, and touchless.</div>
""", unsafe_allow_html=True)

# ---- Login Button ----
if st.button("🔐 Login"):
    os.system("streamlit run frontend.py")
    st.stop()

st.markdown("</div>", unsafe_allow_html=True)
