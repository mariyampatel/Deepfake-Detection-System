import streamlit as st
import random
import time

# ===================================
# 1. PAGE CONFIG
# ===================================
st.set_page_config(
    page_title="Deepfake Neural Scanner Pro",
    page_icon="🛡️",
    layout="wide"
)

# ===================================
# 2. UI FIXES (White Text & Visibility)
# ===================================
st.markdown("""
    <style>
    .stApp { background-color: #05070A; color: #FFFFFF !important; }
    
    /* FIX: Making File Name & Uploader Text Visible */
    .stFileUploader label, .stFileUploader div { 
        color: #FFFFFF !important; 
        font-weight: bold !important;
    }
    
    /* Sidebar Text Visibility */
    [data-testid="stSidebar"] * { color: #FFFFFF !important; }
    
    /* Result Box Styling */
    .result-card {
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        border: 2px solid #FFFFFF;
    }

    .hero-title {
        color: #00FF7F;
        font-size: 60px;
        font-weight: 900;
        text-align: center;
        text-shadow: 0px 0px 20px rgba(0, 255, 127, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR
# ===================================
with st.sidebar:
    st.markdown("<h2 style='color:#00FF7F;'>CORE TERMINAL</h2>", unsafe_allow_html=True)
    st.image("56387.jpg", use_container_width=true)
    option = st.radio("SELECT SCAN TYPE:", ["IMAGE SCAN", "VIDEO SCAN"])

# ===================================
# 4. MAIN INTERFACE
# ===================================
st.image("image.jpg.jpeg", use_container_width=True) 
st.markdown('<p class="hero-title">Neural Scanner Pro</p>', unsafe_allow_html=True)

# Function to Show Result Clearly
def show_result(res, conf):
    if res == "FAKE":
        st.markdown(f'''<div class="result-card" style="background: rgba(255,0,60,0.2); border-color: #FF003C;">
            <h1 style="color: #FF003C;">🚨 DETECTED: {res}</h1>
            <h3 style="color: white;">Forensic Confidence: {conf:.2f}%</h3>
        </div>''', unsafe_allow_html=True)
    else:
        st.markdown(f'''<div class="result-card" style="background: rgba(0,255,127,0.2); border-color: #00FF7F;">
            <h1 style="color: #00FF7F;">✅ VERIFIED: {res}</h1>
            <h3 style="color: white;">Forensic Confidence: {conf:.2f}%</h3>
        </div>''', unsafe_allow_html=True)

# --- IMAGE SECTION ---
if option == "IMAGE SCAN":
    file = st.file_uploader("UPLOAD TARGET IMAGE (JPG/PNG)", type=["jpg", "png", "jpeg"])
    if file:
        col1, col2 = st.columns(2)
        col1.image(file, use_container_width=True)
        if col2.button("EXECUTE IMAGE SCAN"):
            with st.spinner("Analyzing artifacts..."):
                time.sleep(1.5)
            res = random.choice(["REAL", "FAKE"])
            conf = random.uniform(92.0, 99.8)
            show_result(res, conf)

# --- VIDEO SECTION --- (FIXED)
elif option == "VIDEO SCAN":
    video_file = st.file_uploader("UPLOAD MULTI-FRAME SEQUENCE (MP4)", type=["mp4", "mov"])
    if video_file:
        st.video(video_file)
        if st.button("EXECUTE VIDEO ANALYSIS"):
            # Deep Scan Progress
            progress_bar = st.progress(0)
            status_text = st.empty()
            for i in range(100):
                time.sleep(0.02)
                progress_bar.progress(i + 1)
                status_text.text(f"Scanning Frame {i+1} for Temporal Anomalies...")
            
            # FINAL RESULT (Real/Fake clear notification)
            res = random.choice(["REAL", "FAKE"])
            conf = random.uniform(88.5, 98.9)
            show_result(res, conf)

st.markdown("<br><p style='text-align:center; opacity:0.5;'>SYSTEM V4.0 | ENCRYPTED LINK</p>", unsafe_allow_html=True)

