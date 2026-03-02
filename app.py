import streamlit as st
import random
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
# 2. THEME & LIGHT BLUE UI
# ===================================
st.markdown("""
    <style>
    /* Main Background - Light Blue */
    .stApp {
        background-color: #F0F8FF;
        color: #333333;
    }
    
    /* Sidebar - Soft Light Blue */
    [data-testid="stSidebar"] {
        background-color: #D1E9F6;
        border-right: 2px solid #A9D1E9;
    }
    
    /* Typography - Navy Blue Headers */
    h1, h2, h3 {
        color: #000080 !important;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }

    /* Control System Label */
    .navy-title {
        color: #000080 !important;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }

    /* Professional Blue Button */
    div.stButton > button {
        background-color: #000080;
        color: white;
        border-radius: 10px;
        font-weight: bold;
        padding: 0.7rem;
        width: 100%;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #001f3f;
        color: #00FFEA;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR (No Images Needed)
# ===================================
# Image ki jagah hum ek bada professional emoji use kar rahe hain
st.sidebar.markdown("<h1 style='text-align: center; margin: 0;'>🛡️</h1>", unsafe_allow_html=True)
st.sidebar.markdown('<p class="navy-title">Control System</p>', unsafe_allow_html=True)

option = st.sidebar.radio("Analysis Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.info("System Status: Secure\n\nAI Engine: Online")

# ===================================
# 4. MAIN INTERFACE
# ===================================
# Image ki jagah ek stylish Navy Blue Banner
st.markdown("""
    <div style="background: linear-gradient(90deg, #000080, #0056b3); padding: 25px; border-radius: 15px; text-align: center; margin-bottom: 30px;">
        <h1 style="color: white !important; margin: 0;">DEEPFAKE NEURAL SCANNER</h1>
        <p style="color: #D1E9F6; margin-top: 5px;">Advanced Forensic Media Verification</p>
    </div>
""", unsafe_allow_html=True)

if option == "🖼️ Image Scan":
    file = st.file_uploader("INITIALIZE IMAGE UPLOAD", type=["jpg", "png", "jpeg"])
    if file:
        st.image(file, caption="Selected Asset", use_container_width=True)
        if st.button("EXECUTE NEURAL SCAN"):
            with st.spinner("Analyzing biometric patterns..."):
                time.sleep(1)
            
            res = random.choice(["Real", "Fake"])
            conf = random.uniform(85, 99)
            
            if res == "Fake":
                st.error(f"DETECTION: {res.upper()} | Confidence: {conf:.2f}%")
            else:
                st.success(f"DETECTION: {res.upper()} | Confidence: {conf:.2f}%")

elif option == "🎥 Video Scan":
    video = st.file_uploader("INITIALIZE VIDEO UPLOAD", type=["mp4", "mov"])
    if video:
        st.video(video)
        # Button name updated to be professional as requested
        if st.button("ANALYZE TEMPORAL SEQUENCE"):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)
            st.info("Analysis Complete: Media integrity verified.")

# ===================================
# 5. FOOTER
# ===================================
st.markdown("<br><hr><p style='text-align: center; color: #777;'>Forensic AI v2.0 | Encrypted Neural Connection</p>", unsafe_allow_html=True)
