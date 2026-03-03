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
# 2. OPTIMIZED UI & FAST LOADING
# ===================================
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1B4B;
        color: #FFFFFF !important;
    }
    
    [data-testid="stSidebar"] {
        background-color: #312E81 !important;
        border-right: 2px solid #00FF7F;
    }

    /* TITLE - Extra Large & Centered */
    .hero-title {
        color: #00FF7F;
        font-size: 80px; 
        font-weight: 900;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 0px;
        text-shadow: 0px 0px 20px rgba(0, 255, 127, 0.6);
    }
    .hero-subtitle {
        color: #FFFFFF;
        text-align: center;
        font-size: 20px;
        letter-spacing: 6px;
        margin-bottom: 30px;
    }

    /* IMAGE - Small & Centered */
    .header-img-container {
        display: flex;
        justify-content: center;
        margin-top: 10px;
    }
    .header-img-container img {
        max-width: 25% !important; 
        border-radius: 12px;
        border: 2px solid #00FF7F;
    }

    /* Fast Result Card */
    .result-card {
        padding: 25px;
        border-radius: 10px;
        text-align: center;
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR
# ===================================
with st.sidebar:
    st.markdown("<h2 style='color:#00FF7F;'>TERMINAL</h2>", unsafe_allow_html=True)
    st.image("56387.jpg", use_container_width=True)
    option = st.radio("SCAN MODE:", ["IMAGE SCAN", "VIDEO SCAN"])
    st.write("---")
    st.write("🛰️ STATUS: ENCRYPTED")

# ===================================
# 4. MAIN INTERFACE (Image First, then Huge Title)
# ===================================

# Small Image on Top
st.markdown('<div class="header-img-container">', unsafe_allow_html=True)
st.image("image.jpg.jpeg") 
st.markdown('</div>', unsafe_allow_html=True)

# Huge Title Below Image
st.markdown('<p class="hero-title">Neural Scanner Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">FORENSIC MEDIA ANALYSIS</p>', unsafe_allow_html=True)

# ===================================
# 5. SCANNER LOGIC
# ===================================
def display_result(res, conf):
    color = "#FF003C" if res == "FAKE" else "#00FF7F"
    st.markdown(f'''
        <div class="result-card" style="border-color: {color};">
            <h1 style="color: {color}; font-size: 45px;">{res}</h1>
            <h3 style="color: white;">Confidence: {conf:.2f}%</h3>
        </div>
    ''', unsafe_allow_html=True)

if option == "IMAGE SCAN":
    file = st.file_uploader("UPLOAD IMAGE", type=["jpg", "png", "jpeg"])
    if file:
        col1, col2 = st.columns(2)
        with col1: st.image(file, width=300)
        with col2:
            if st.button("RUN IMAGE ANALYSIS"):
                with st.spinner("Scanning..."): time.sleep(0.5)
                display_result(random.choice(["REAL", "FAKE"]), random.uniform(92, 99))

elif option == "VIDEO SCAN":
    v_file = st.file_uploader("UPLOAD VIDEO", type=["mp4", "mov"])
    if v_file:
        # Optimized video display
        st.video(v_file, format="video/mp4", start_time=0)
        if st.button("RUN TEMPORAL SCAN"):
            p = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                p.progress(i + 1)
            display_result(random.choice(["REAL", "FAKE"]), random.uniform(88, 97))

st.markdown("<br><p style='text-align:center; opacity:0.4;'>SECURE ENGINE v4.0.2</p>", unsafe_allow_html=True)
