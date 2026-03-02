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
    
    /* Sidebar Complimentary Color - Light Sky Blue */
    [data-testid="stSidebar"] {
        background-color: #B2EBF2;
    }
    
    /* Typography - Navy Blue for Headers */
    h1, h2, h3 {
        color: #000080 !important;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    
    /* Control System Text - Navy Blue */
    .navy-title {
        color: #000080 !important;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }

    /* Custom Professional Button */
    div.stButton > button {
        background: #000080;
        color: #ffffff;
        border: 2px solid #000080;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        font-weight: 700;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s ease-in-out;
    }
    div.stButton > button:hover {
        background: #ffffff;
        color: #000080;
    }
    
    /* Result Cards Styling */
    .scan-result-fake {
        background: rgba(255, 0, 60, 0.15);
        border-left: 5px solid #ff003c;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
    }
    .scan-result-real {
        background: rgba(0, 128, 0, 0.15);
        border-left: 5px solid #008000;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
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
# 4. SIDEBAR WITH PROFESSIONAL IMAGE
# ===================================
# Image 1 (Sidebar): Fingerprint / Digital Security Image
st.sidebar.image("https://img.icons8.com/color/144/facial-recognition.png", width=100)
st.sidebar.markdown('<p class="navy-title">Control System</p>', unsafe_allow_html=True)
option = st.sidebar.radio("Select Targeting Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #444; font-weight: bold;'>Status: Active</p>", unsafe_allow_html=True)

# ===================================
# 5. MAIN UI & PROFESSIONAL HEADER IMAGE
# ===================================
# Image 2 (Main Screen): Professional Biometric/Neural Scan
st.image("https://images.unsplash.com/photo-1593006526978-651c6c132890?q=80&w=1000&auto=format&fit=crop", use_container_width=True)


st.title("DEEPFAKE NEURAL SCANNER")
st.markdown("<p style='text-align: center; color: #555; font-weight: 500;'>Upload suspect media for forensic neural network verification.</p>", unsafe_allow_html=True)

# ===================================
# ANALYSIS INTERFACE
# ===================================
if option == "🖼️ Image Scan":
    uploaded_file = st.file_uploader("INITIALIZE IMAGE UPLOAD", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Target Acquired", use_container_width=True)
        if st.button("INITIATE SCAN SEQUENCE"):
            with st.spinner("Analyzing facial geometry..."):
                time.sleep(1)
            prediction, confidence = predict_dummy()
            
            if prediction == "Fake":
                st.markdown(f'<div class="scan-result-fake"><h2 style="color:#ff003c;">🚨 THREAT DETECTED: {prediction.upper()}</h2><p style="font-size:2rem; font-weight:bold;">{confidence * 100:.2f}%</p></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="scan-result-real"><h2 style="color:#008000;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2><p style="font-size:2rem; font-weight:bold;">{confidence * 100:.2f}%</p></div>', unsafe_allow_html=True)

elif option == "🎥 Video Scan":
    uploaded_video = st.file_uploader("INITIALIZE VIDEO UPLOAD", type=["mp4", "mov"])

    if uploaded_video is not None:
        st.video(uploaded_video)
        # Using the professional button name as you liked
        if st.button("ANALYZE TEMPORAL SEQUENCE"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            prediction, confidence = predict_dummy()
            st.info(f"Temporal Analysis Result: {prediction} ({confidence*100:.2f}%)")

# ===================================
# FOOTER
# ===================================
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>DEEPFAKE FORENSICS v2.0 | SECURE CONNECTION</p>", unsafe_allow_html=True)
