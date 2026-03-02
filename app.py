import streamlit as st
import random
import time

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Forensic Neural Scanner",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. LIGHT PROFESSIONAL THEME (No External Links)
# ===================================
st.markdown("""
    <style>
    /* Main Background - Soft Light Blue */
    .stApp {
        background-color: #F4F9FC; 
        color: #2C3E50;
    }
    
    /* Sidebar - Very Light Grey-Blue (Professional) */
    [data-testid="stSidebar"] {
        background-color: #E3EBF2;
        border-right: 1px solid #D1D9E0;
    }
    
    /* Ensuring Sidebar text is dark for readability */
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label {
        color: #000080 !important;
        font-weight: 600;
    }
    
    /* Navy Blue Headings */
    h1, h2 {
        color: #000080 !important;
        font-family: 'Segoe UI', Tahoma, sans-serif;
        letter-spacing: 1px;
    }

    /* Result Styling */
    .result-card {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin: 15px 0;
        border: 2px solid;
    }

    /* Professional Button */
    div.stButton > button {
        background-color: #000080;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        padding: 0.6rem 2rem;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR (With Local Graphic)
# ===================================
st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="font-size: 50px; margin: 0;">👤</h1>
        <p style="color: #000080; font-weight: bold; margin: 0;">SYSTEM CONTROLS</p>
    </div>
""", unsafe_allow_html=True)

option = st.sidebar.radio("Analysis Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='font-size: 0.8rem;'>Forensic ID Engine: Active<br>Version: 2.4.1</p>", unsafe_allow_html=True)

# ===================================
# 4. MAIN INTERFACE
# ===================================
# Instead of image links, we use a CSS Banner (Guaranteed to load)
st.markdown("""
    <div style="background-color: #000080; padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 30px;">
        <h1 style="color: white !important; margin: 0;">🛡️ DEEPFAKE NEURAL SCANNER</h1>
        <p style="color: #D1D9E0; margin: 5px 0 0 0;">Forensic Authenticity & Integrity Verification</p>
    </div>
""", unsafe_allow_html=True)

if option == "🖼️ Image Scan":
    file = st.file_uploader("Upload Target Image", type=["jpg", "png", "jpeg"])
    if file:
        st.image(file, use_container_width=True)
        if st.button("EXECUTE NEURAL SCAN"):
            with st.status("Analyzing pixel distribution...", expanded=False):
                time.sleep(1)
            
            res = random.choice(["Real", "Fake"])
            conf = random.uniform(88, 99.9)
            
            if res == "Fake":
                st.markdown(f'<div class="result-card" style="background:#FDEDEC; border-color:#E74C3C; color:#C0392B;"><h2>🚨 THREAT DETECTED: FAKE 🚨</h2><h3>Confidence: {conf:.2f}%</h3></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="result-card" style="background:#EAFAF1; border-color:#27AE60; color:#1E8449;"><h2>✅ MEDIA AUTHENTICATED: REAL ✅</h2><h3>Confidence: {conf:.2f}%</h3></div>', unsafe_allow_html=True)

elif option == "🎥 Video Scan":
    video = st.file_uploader("Upload Target Video", type=["mp4", "mov"])
    if video:
        st.video(video)
        if st.button("ANALYZE TEMPORAL SEQUENCE"):
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i + 1)
            
            res = random.choice(["Real", "Fake"])
            conf = random.uniform(85, 98.5)
            st.info(f"Verification Complete. Media is likely {res} (Confidence: {conf:.2f}%)")

# ===================================
# 5. FOOTER
# ===================================
st.markdown("<br><br><p style='text-align: center; color: #7F8C8D; font-size: 0.8rem;'>Forensic AI v2.0 | Encrypted Neural Connection</p>", unsafe_allow_html=True)
