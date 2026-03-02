import streamlit as st
import random
from PIL import Image
import time

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Scanner",
    page_icon="👁️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. CYBER-THEMED CUSTOM CSS
# ===================================
st.markdown("""
    <style>
    /* Full Page Background Color / Gradient */
    .stApp {
        background: linear-gradient(135deg, #0b132b, #1c2541, #0b132b);
        color: #e0e1dd;
    }
    
    /* Sidebar Background Color */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1c2541, #0b132b);
        border-right: 1px solid #3a506b;
    }
    
    /* Typography */
    h1, h3 {
        color: #00FFEA !important;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }
    
    /* Custom Neon Button */
    div.stButton > button {
        background: transparent;
        color: #00FFEA;
        border: 2px solid #00FFEA;
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
        background: #00FFEA;
        color: #0b132b;
        box-shadow: 0 0 15px #00FFEA;
    }
    
    /* Result Cards */
    .scan-result-fake {
        background: rgba(255, 0, 60, 0.1);
        border-left: 5px solid #ff003c;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(255, 0, 60, 0.2);
    }
    .scan-result-real {
        background: rgba(0, 255, 234, 0.1);
        border-left: 5px solid #00FFEA;
        padding: 20px;
        border-radius: 5px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 255, 234, 0.2);
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
    """Dummy prediction logic"""
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ===================================
# 4. SIDEBAR
# ===================================
# Premium AI / Tech Face Image for Sidebar
st.sidebar.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80", caption="Neural Engine v2.4.1")

# NAVY BLUE "System Controls" on a light card for maximum visibility
st.sidebar.markdown("""
    <div style="background-color: #e0e1dd; padding: 12px; border-radius: 5px; text-align: center; margin-bottom: 20px; border-bottom: 3px solid #00FFEA;">
        <h2 style="color: #000080; margin: 0; font-family: 'Arial', sans-serif; font-weight: 900; font-size: 22px; text-transform: uppercase;">System Controls</h2>
    </div>
""", unsafe_allow_html=True)

option = st.sidebar.radio("Select Targeting Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #00FFEA; font-size: 0.85rem; font-family: monospace;'>● System Status: Active<br>● Server: Encrypted Connection</p>", unsafe_allow_html=True)

# ===================================
# 5. MAIN UI & HEADER IMAGE
# ===================================
# High-tech cyber security lens image for the main banner
st.image("https://images.unsplash.com/photo-1507146426996-ef05306b995a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", use_container_width=True)

st.title("DEEPFAKE NEURAL SCANNER")
st.markdown("<p style='text-align: center; color: #a8b2d1; margin-bottom: 30px; font-size: 1.1rem;'>Upload suspect media to our forensic neural network for authenticity verification.</p>", unsafe_allow_html=True)

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
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Running facial landmark analysis...</h4>", unsafe_allow_html=True)
            time.sleep(1) 
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Detecting pixel manipulation...</h4>", unsafe_allow_html=True)
            time.sleep(1.5)
            status_text.empty() 

            prediction, confidence = predict_dummy()

            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0;">🚨 THREAT DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #ccc; margin-top: 10px;">Artificial manipulation identified in media structure.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #00FFEA; margin: 0;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2>
                        <p style="color: #ccc; margin-top: 10px;">No deepfake artifacts detected in neural scan.</p>
                        <p class="score-text" style="color: #00FFEA;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
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
            status_text = st.empty()
            status_text.markdown("<h4 style='text-align: center; color: #ffbc42;'>Extracting frames for temporal analysis...</h4>", unsafe_allow_html=True)
            time.sleep(2)
            status_text.empty()

            prediction, confidence = predict_dummy()

            if prediction == "Fake":
                st.markdown(f"""
                    <div class="scan-result-fake">
                        <h2 style="color: #ff003c; margin: 0;">🚨 THREAT DETECTED: {prediction.upper()} 🚨</h2>
                        <p style="color: #ccc; margin-top: 10px;">Temporal inconsistencies and artificial artifacts identified.</p>
                        <p class="score-text" style="color: #ff003c;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="scan-result-real">
                        <h2 style="color: #00FFEA; margin: 0;">✅ MEDIA AUTHENTICATED: {prediction.upper()}</h2>
                        <p style="color: #ccc; margin-top: 10px;">Video sequence cleared by neural engine.</p>
                        <p class="score-text" style="color: #00FFEA;">{confidence * 100:.2f}%</p>
                        <p>Confidence Score</p>
                    </div>
                """, unsafe_allow_html=True)

# ===================================
# FOOTER
# ===================================
st.markdown("<br><hr style='border-color: #3a506b;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-family: monospace;'>DEEPGUARD AI v2.4.1 | ENCRYPTED CONNECTION</p>", unsafe_allow_html=True)
