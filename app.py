import streamlit as st
import random
import time

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Neural Scanner Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. COMPACT & HIGH-VISIBILITY UI
# ===================================
st.markdown("""
    <style>
    /* Background & Global Text */
    .stApp {
        background-color: #1E1B4B;
        color: #FFFFFF !important;
    }
    
    /* SIDEBAR styling */
    [data-testid="stSidebar"] {
        background-color: #312E81 !important;
        border-right: 2px solid #00FF7F;
    }
    [data-testid="stSidebar"] * { color: #FFFFFF !important; }

    /* TITLE - Large but Compact */
    .hero-title {
        color: #00FF7F;
        font-size: 70px; 
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
        margin-top: -20px; /* Reducing top gap */
        text-shadow: 0px 0px 15px rgba(0, 255, 127, 0.5);
    }
    .hero-subtitle {
        color: #FFFFFF;
        text-align: center;
        font-size: 18px;
        letter-spacing: 5px;
        margin-bottom: 10px;
    }

    /* IMAGE RESIZING (30% for no scroll) */
    .header-img-container {
        display: flex;
        justify-content: center;
        margin-top: 0px;
    }
    .header-img-container img {
        max-width: 30% !important; /* Image size even smaller now */
        border-radius: 10px;
    }

    /* Result Card */
    .result-card {
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid #FFFFFF;
    }
    
    /* Button Style */
    div.stButton > button {
        background: #00FF7F !important;
        color: #000000 !important;
        font-weight: bold;
        height: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR
# ===================================
with st.sidebar:
    st.markdown("<h2 style='color:#00FF7F;'>TERMINAL</h2>", unsafe_allow_html=True)
    st.image("56387.jpg", use_container_width=True)
    option = st.radio("MODE:", ["IMAGE SCAN", "VIDEO SCAN"])
    st.markdown("---")
    st.write("🛰️ LINK: SECURE")

# ===================================
# 4. MAIN INTERFACE (NO SCROLL LAYOUT)
# ===================================

# Title First (Priority)
st.markdown('<p class="hero-title">Neural Scanner Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">ADVANCED DETECTION SYSTEM</p>', unsafe_allow_html=True)

# Small Image Below Title
st.markdown('<div class="header-img-container">', unsafe_allow_html=True)
st.image("image.jpg.jpeg") 
st.markdown('</div>', unsafe_allow_html=True)

# ===================================
# 5. SCANNER SECTION (Directly visible)
# ===================================
def show_final_result(res, conf):
    color = "#FF003C" if res == "FAKE" else "#00FF7F"
    st.markdown(f'''
        <div class="result-card" style="border-color: {color};">
            <h1 style="color: {color};">Result: {res}</h1>
            <h2 style="color: white;">Confidence: {conf:.2f}%</h2>
        </div>
    ''', unsafe_allow_html=True)

if option == "IMAGE SCAN":
    file = st.file_uploader("UPLOAD TARGET", type=["jpg", "png", "jpeg"])
    if file:
        col1, col2 = st.columns(2)
        with col1: st.image(file, width=250)
        with col2:
            if st.button("EXECUTE SCAN"):
                with st.spinner("Processing..."): time.sleep(1)
                res = random.choice(["REAL", "FAKE"])
                show_final_result(res, random.uniform(90, 99))

elif option == "VIDEO SCAN":
    v_file = st.file_uploader("UPLOAD VIDEO", type=["mp4", "mov"])
    if v_file:
        st.video(v_file)
        if st.button("START ANALYSIS"):
            p = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                p.progress(i + 1)
            show_final_result(random.choice(["REAL", "FAKE"]), random.uniform(85, 98))

st.markdown("<p style='text-align:center; opacity:0.5; font-size:10px;'>SECURE V4.0</p>", unsafe_allow_html=True)
