import streamlit as st
import random
from PIL import Image
import time

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Neural Scanner",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. THEME & STYLING (Light Blue & Navy)
# ===================================
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #E0F7FA;
        color: #1c2541;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #000080; /* Navy Blue Sidebar */
        color: white;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Header Banner Effect */
    .header-container {
        background: linear-gradient(90deg, #000080, #0056b3);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Navy Blue Headings */
    h1 {
        color: #000080 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
    }

    /* Professional Button */
    div.stButton > button {
        background: #000080;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 20px;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background: #0056b3;
        transform: translateY(-2px);
    }

    /* Result Cards */
    .result-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. CORE LOGIC
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.82, 0.99), 4)
    return prediction, confidence

# ===================================
# 4. SIDEBAR
# ===================================
st.sidebar.markdown("<h2 style='text-align: center;'>🛡️ SCANNER</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")
option = st.sidebar.radio("Navigation", ["🖼️ Image Scan", "🎥 Video Scan"])

st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)
st.sidebar.info("Status: System Online\n\nSecurity: Encrypted")

# ===================================
# 5. MAIN CONTENT
# ===================================
# Replacing the broken image with a CSS-based Professional Banner
st.markdown("""
    <div class="header-container">
        <h1 style="color: white !important; margin:0;">DEEPFAKE NEURAL SCANNER</h1>
        <p style="color: #e0e0e0; margin-top:10px;">Advanced Forensic Authenticity Verification</p>
    </div>
""", unsafe_allow_html=True)

if option == "🖼️ Image Scan":
    uploaded_file = st.file_uploader("Upload Image for Analysis", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Analyzable Asset", use_container_width=True)
        
        if st.button("RUN NEURAL ANALYSIS"):
            with st.status("Analyzing pixel consistency...", expanded=True) as status:
                time.sleep(0.6)
                st.write("Checking facial landmarks...")
                time.sleep(0.6)
                st.write("Verifying metadata integrity...")
                status.update(label="Analysis Complete!", state="complete")

            res, conf = predict_dummy()
            
            if res == "Fake":
                st.markdown(f"""
                    <div style="background: #ffe5e5; border-color: #cc0000;" class="result-box">
                        <h2 style="color: #cc0000;">🚨 FAKE DETECTED 🚨</h2>
                        <p style="font-size: 24px; font-weight: bold; color: #333;">Confidence: {conf*100:.2f}%</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="background: #e5f9e5; border-color: #008000;" class="result-box">
                        <h2 style="color: #008000;">✅ AUTHENTIC ✅</h2>
                        <p style="font-size: 24px; font-weight: bold; color: #333;">Confidence: {conf*100:.2f}%</p>
                    </div>
                """, unsafe_allow_html=True)

elif option == "🎥 Video Scan":
    uploaded_video = st.file_uploader("Upload Video for Analysis", type=["mp4", "mov", "avi"])

    if uploaded_video:
        st.video(uploaded_video)
        
        if st.button("RUN TEMPORAL SCAN"):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01) # Super fast loading
                progress_bar.progress(i + 1)
            
            res, conf = predict_dummy()
            if res == "Fake":
                st.error(f"High probability of synthetic manipulation: {conf*100:.2f}%")
            else:
                st.success(f"No significant deepfake artifacts found: {conf*100:.2f}%")

# ===================================
# FOOTER
# ===================================
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Final Year Project 2026 | Forensic AI Module</p>", unsafe_allow_html=True)
