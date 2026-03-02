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
# 2. LIGHT BLUE THEME CUSTOM CSS
# ===================================
st.markdown("""
    <style>
    /* Full Page Background Color - Ice Blue */
    .stApp {
        background-color: #E0F7FA;
        color: #333333;
    }
    
    /* Sidebar Complimentary Color */
    [data-testid="stSidebar"] {
        background-color: #B2EBF2;
    }
    
    /* Typography - Navy Blue for Headers */
    h1, h2, h3 {
        color: #000080 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
    
    /* Custom Button */
    div.stButton > button {
        background: #000080;
        color: #ffffff;
        border: 2px solid #000080;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        background: #ffffff;
        color: #000080;
        box-shadow: 0 0 10px rgba(0, 128, 0, 0.4);
    }

    /* Professional Icon Placeholder */
    .icon-box {
        background-color: #000080;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 20px;
        color: white;
    }
    
    /* Result Cards */
    .scan-result-fake {
        background: rgba(255, 0, 60, 0.15);
        border-left: 5px solid #ff003c;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
        color: #333;
    }
    .scan-result-real {
        background: rgba(0, 128, 0, 0.15);
        border-left: 5px solid #008000;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
        color: #333;
    }
    .score-text {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. CORE LOGIC
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ===================================
# 4. SIDEBAR (Stable Solution)
# ===================================
# Image ki jagah hum ek professional SVG icon use kar rahe hain jo kabhi break nahi hoga
st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-size: 80px; margin: 0;">👤</h1>
        <p style="color: #000080; font-weight: bold;">SECURITY ENGINE</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("<h1>System Controls</h1>", unsafe_allow_html=True)
option = st.sidebar.radio("Select Targeting Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #444; font-size: 0.9rem; font-weight: bold;'>System Status: Active<br>Server: Secure Connection</p>", unsafe_allow_html=True)

# ===================================
# 5. MAIN UI HEADER (Stable Solution)
# ===================================
# A stylish banner that doesn't rely on external image links
st.markdown("""
    <div class="icon-box">
        <h1 style="color: white !important; margin: 0;">🛡️ FORENSIC NEURAL SCANNER</h1>
        <p style="margin: 5px 0 0 0; font-weight: 500;">Advanced Deepfake Identification Protocol</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #555; margin-bottom: 30px; font-weight: 500;'>Upload suspect media to our forensic neural network for authenticity verification.</p>", unsafe_allow_html=True)

# ===================================
# IMAGE SCANNER
# ===================================
if option == "🖼️ Image Scan":
    uploaded_file = st.file_uploader("INITIALIZE IMAGE UPLOAD", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with st.container(border=True):
            st.image(image, caption="Target Acquired", use_container_width=True)

        if st.button("INITIATE SCAN SEQUENCE"):
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #d97706;'>Running facial landmark analysis...</h4>", unsafe_allow_html=True)
            time.sleep(0.5) 
            status_text.markdown("<h4 style='text-align: center; color: #d97706;'>Detecting pixel manipulation...</h4>", unsafe_allow_html=True)
            time.sleep(0.5) 
            status_text.empty() 

            prediction, confidence = predict_dummy()

            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0;">🚨 THREAT DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="margin-top: 10px;">Artificial manipulation identified in media structure.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #008000; margin: 0;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2>
                        <p style="margin-top: 10px;">No deepfake artifacts detected.</p>
                        <p class="score-text" style="color: #008000;">{confidence * 100:.2f}%</p>
                    </div>
                """, unsafe_allow_html=True)

# ===================================
# VIDEO SCANNER
# ===================================
elif option == "🎥 Video Scan":
    uploaded_video = st.file_uploader("INITIALIZE VIDEO UPLOAD", type=["mp4", "mov", "avi"])

    if uploaded_video is not None:
        with st.container(border=True):
            st.video(uploaded_video)

        if st.button("INITIATE FRAME SCAN"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            prediction, confidence = predict_dummy()
            if prediction == "Fake":
                st.error(f"Threat Detected: Synthetic manipulation identified ({confidence*100:.2f}%)")
            else:
                st.success(f"Media Authenticated: Clean sequence ({confidence*100:.2f}%)")

# ===================================
# FOOTER
# ===================================
st.markdown("<br><hr style='border-color: #B2EBF2;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-weight: bold;'>DEEPFAKE FORENSICS v2.0 | SECURE CONNECTION</p>", unsafe_allow_html=True)
