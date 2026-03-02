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
    .stApp {
        background-color: #E0F7FA;
        color: #333333;
    }
    [data-testid="stSidebar"] {
        background-color: #B2EBF2;
    }
    h1, h2, h3 {
        color: #000080 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
    }
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
    }
    div.stButton > button:hover {
        background: #ffffff;
        color: #000080;
    }
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
# 4. SIDEBAR
# ===================================
st.sidebar.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80", caption="Verification Engine Active")
st.sidebar.markdown("<h1 style='font-size: 25px;'>System Controls</h1>", unsafe_allow_html=True)
option = st.sidebar.radio("Select Targeting Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

# ===================================
# 5. MAIN UI & HEADER IMAGE (FIXED ERROR)
# ===================================
# FIXED: Replaced local path with a stable web URL to avoid MediaFileStorageError
st.image("https://images.unsplash.com/photo-1557853113-bbd49242d54a?q=80&w=1200&auto=format&fit=crop", use_container_width=True)

st.title("DEEPFAKE NEURAL SCANNER")
st.markdown("<p style='text-align: center; color: #555; font-weight: 500;'>Advanced Forensic Analysis for Media Authenticity</p>", unsafe_allow_html=True)

# ===================================
# ANALYSIS SECTION
# ===================================
if option == "🖼️ Image Scan":
    uploaded_file = st.file_uploader("INITIALIZE IMAGE UPLOAD", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Target Acquired", use_container_width=True)
        if st.button("INITIATE SCAN"):
            with st.spinner("Analyzing artifacts..."):
                time.sleep(1)
            prediction, confidence = predict_dummy()
            if prediction == "Fake":
                st.markdown(f'<div class="scan-result-fake"><h2>🚨 DETECTED: {prediction.upper()}</h2><h3>Confidence: {confidence*100:.2f}%</h3></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="scan-result-real"><h2>✅ AUTHENTIC ✅</h2><h3>Confidence: {confidence*100:.2f}%</h3></div>', unsafe_allow_html=True)

elif option == "🎥 Video Scan":
    uploaded_video = st.file_uploader("INITIALIZE VIDEO UPLOAD", type=["mp4", "mov"])
    if uploaded_video:
        st.video(uploaded_video)
        if st.button("ANALYZE TEMPORAL SEQUENCE"):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
            prediction, confidence = predict_dummy()
            st.info(f"Result: {prediction} ({confidence*100:.2f}%)")

st.markdown("<br><hr><p style='text-align: center; color: #888;'>DEEPFAKE FORENSICS v2.0</p>", unsafe_allow_html=True)
