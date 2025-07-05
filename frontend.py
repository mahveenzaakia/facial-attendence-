import streamlit as st
import subprocess
import pandas as pd
from datetime import datetime
import base64

# ---- Page config ----
st.set_page_config(page_title="Face Recognition Attendance", layout="centered")

# ---- Set background image with overlay ----
def set_background(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: white !important;
            }}
            .main-card {{
                background-color: rgba(0, 0, 0, 0.6);
                padding: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
                text-align: center;
                color: white !important;
            }}
            .stButton > button {{
                background-color: #4CAF50;
                color: white;
                padding: 0.6rem 1.2rem;
                font-size: 1rem;
                border: none;
                border-radius: 8px;
                transition: 0.3s;
            }}
            .stButton > button:hover {{
                background-color: #45a049;
                transform: scale(1.05);
            }}
            .css-1d391kg {{  /* Dataframe header and text */
                color: white !important;
                font-weight: bold;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Use your updated image file here:
set_background("SmartEye_Facial_Recognition.png")

# ---- Main UI Card ----
st.markdown("<div class='main-card'>", unsafe_allow_html=True)
st.markdown("<h1>🎓 Face Recognition Attendance System</h1>", unsafe_allow_html=True)
st.markdown("<p>Mark attendance with face recognition technology in real-time.</p>", unsafe_allow_html=True)

# ---- Buttons ----
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👤 Register New Face"):
        subprocess.run(["python", "add_faces.py"])
        st.success("Face registered successfully!")

with col2:
    if st.button("📸 Start Attendance"):
        subprocess.run(["python", "test.py"])
        st.success("Attendance process completed!")

with col3:
    if st.button("📊 View Attendance Log"):
        date = datetime.now().strftime("%d-%m-%Y")
        try:
            df = pd.read_csv(f"Attendance/Attendance_{date}.csv")
            st.dataframe(df)
        except FileNotFoundError:
            st.warning("No attendance record found for today.")

st.markdown("</div>", unsafe_allow_html=True)

# ---- Footer ----
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>© 2025 | Face Recognition System UI</p>", unsafe_allow_html=True)
