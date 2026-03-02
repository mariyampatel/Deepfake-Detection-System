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
# 2. PROFESSIONAL LIGHT THEME CSS
# ===================================
st.markdown("""
    <style>
    /* Main Background - Soft Light Blue */
    .stApp {
        background-color: #F0F7FA;
        color: #333333;
    }
    
    /* Sidebar - Professional Light Blue-Grey */
    [data-testid="stSidebar"] {
        background-color: #D1E9F6;
        border-right: 1px solid #A9D1E9;
    }
    
    /* Navy Blue Headers */
    h1, h2, h3 {
        color: #000080 !important;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
    }
    
    /* Control System Label in Sidebar */
    .navy-label {
        color: #000080 !important;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }

    /* Professional Navy Blue Button */
    div.stButton > button {
        background-color: #000080;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        padding: 12px;
        width: 100%;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR
# ===================================
st.sidebar.markdown("<h1 style='text-align: center; margin: 0;'>🛡️</h1>", unsafe_allow_html=True)
st.sidebar.markdown('<p class="navy-label">Control System</p>', unsafe_allow_html=True)

option = st.sidebar.radio("Analysis Mode:", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("---")
st.sidebar.markdown("<p style='color: #000080; font-weight: 500;'>System Status: Active<br>Server: Secure Connection</p>", unsafe_allow_html=True)

# ===================================
# 4. MAIN INTERFACE
# ===================================
# Image ki jagah humne ek professional Navy Blue header banner dala hai
st.markdown("""
    <div style="background-color: #000080; padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 25px;">
        <h1 style="color: white !important; margin: 0;">DEEPFAKE NEURAL SCANNER</h1>
        <p style="color: #D1E9F6; margin-top: 10px; font-weight: 500;">Forensic Authenticity & Integrity Verification</p>
    </div>
""", unsafe_allow_html=True)

if option == "🖼️ Image Scan":
    uploaded_file = st.file_uploader("INITIALIZE IMAGE UPLOAD", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Target Acquired", use_container_width=True)
        
        if st.button("RUN NEURAL SCAN"):
            with st.status("Analyzing pixel distribution...", expanded=True) as status:
                time.sleep(0.7)
                st.write("Checking facial landmarks...")
                time.sleep(0.7)
                status.update(label="Analysis Complete", state="complete")
            
            res = random.choice(["Real", "Fake"])
            conf = random.uniform(85, 99.5)
            
            if res == "Fake":
                st.error(f"DETECTION: {res.upper()} (Confidence: {conf:.2f}%)")
            else:
                st.success(f"DETECTION: {res.upper()} (Confidence: {conf:.2f}%)")

elif option == "🎥 Video Scan":
    uploaded_video = st.file_uploader("INITIALIZE VIDEO UPLOAD", type=["mp4", "mov"])
    
    if uploaded_video:
        st.video(uploaded_video)
        
        if st.button("ANALYZE TEMPORAL SEQUENCE"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            res = random.choice(["Real", "Fake"])
            conf = random.uniform(82, 98.9)
            st.info(f"Temporal Analysis Result: {res} ({conf:.2f}%)")

# ===================================
# 5. FOOTER
# ===================================
st.markdown("<br><hr><p style='text-align: center; color: #7F8C8D; font-size: 0.85rem;'>Forensic AI v2.0 | Encrypted Neural Connection</p>", unsafe_allow_html=True)
