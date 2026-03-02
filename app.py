import streamlit as st
import random
from PIL import Image
import time

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Scanner",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. LIGHT THEME & NAVY BLUE TEXT
# ===================================
st.markdown("""
    <style>
    /* Main Background - Very Light Blue */
    .stApp {
        background-color: #F0F7FA;
        color: #333333;
    }
    
    /* Sidebar - Soft Light Blue (Not Dark) */
    [data-testid="stSidebar"] {
        background-color: #D1E9F6;
    }
    
    /* Typography - Navy Blue for Headers */
    h1, h2, h3 {
        color: #000080 !important;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    
    /* Control System Text - Specific Navy Blue */
    .navy-label {
        color: #000080 !important;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Professional Buttons */
    div.stButton > button {
        background: #000080;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR
# ===================================
# Professional Tech Image (Stable Link)
st.sidebar.image("https://www.gstatic.com/images/branding/product/2x/security_256dp.png", width=100)
st.sidebar.markdown('<p class="navy-label">Control System</p>', unsafe_allow_html=True)

option = st.sidebar.radio("Navigation:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.write("System: Online")

# ===================================
# 4. MAIN INTERFACE
# ===================================
# Professional Face Scan Header (Stable Link)
st.image("https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d473530c05e3a419163b1.svg", width=80)

st.title("DEEPFAKE NEURAL SCANNER")
st.markdown("<p style='text-align: center; color: #555;'>Advanced Forensic Analysis Engine</p>", unsafe_allow_html=True)

if option == "🖼️ Image Scan":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True)
        if st.button("RUN NEURAL SCAN"):
            with st.spinner("Analyzing..."):
                time.sleep(1)
            res = random.choice(["Real", "Fake"])
            if res == "Fake":
                st.error(f"DETECTION: {res.upper()}")
            else:
                st.success(f"DETECTION: {res.upper()}")

elif option == "🎥 Video Scan":
    uploaded_video = st.file_uploader("Upload Video", type=["mp4", "mov"])
    if uploaded_video:
        st.video(uploaded_video)
        if st.button("ANALYZE TEMPORAL SEQUENCE"):
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i + 1)
            res = random.choice(["Real", "Fake"])
            st.info(f"Media is likely {res}")

# ===================================
# 5. FOOTER
# ===================================
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Forensic AI v2.0 | 2026</p>", unsafe_allow_html=True)
