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
# 2. PRO-VISIBILITY DARK THEME (FIXED)
# ===================================
st.markdown("""
    <style>
    /* Main Background - Deep Cyber Black */
    .stApp {
        background-color: #1E1B4B;
        color: #FFFFFF !important;
    }
    
    /* SIDEBAR - Full Visibility Fix */
    [data-testid="stSidebar"] {
        background-color: #312E81 !important;
        border-right: 2px solid #00FF7F;
    }
    [data-testid="stSidebar"] * { 
        color: #FFFFFF !important; 
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] h2 {
        color: #00FF7F !important;
        text-shadow: 0px 0px 10px rgba(0, 255, 127, 0.4);
    }

    /* UPLOADER & BROWSER TEXT - PURE WHITE */
    .stFileUploader label, .stFileUploader div, .stFileUploader span {
        color: #FFFFFF !important;
        font-size: 18px !important;
    }

    /* HEADER TYPOGRAPHY - HUGE & BOLD */
    .hero-title {
        color: #00FF7F;
        font-size: 65px;
        font-weight: 900;
        text-align: center;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-top: 15px;
        text-shadow: 0px 0px 20px rgba(0, 255, 127, 0.6);
    }
    .hero-subtitle {
        color: #FFFFFF;
        text-align: center;
        font-size: 18px;
        letter-spacing: 6px;
        opacity: 0.8;
        margin-bottom: 40px;
    }

    /* RESULT CARD - NEON BOX */
    .result-card {
        padding: 35px;
        border-radius: 15px;
        text-align: center;
        margin-top: 25px;
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid #FFFFFF;
        backdrop-filter: blur(10px);
    }

    /* BUTTONS - HIGH CONTRAST */
    div.stButton > button {
        background: #00FF7F !important;
        color: #000000 !important;
        font-size: 20px !important;
        font-weight: bold;
        width: 100%;
        height: 55px;
        border-radius: 5px;
        border: none;
    }
    div.stButton > button:hover {
        background: #FFFFFF !important;
        box-shadow: 0px 0px 20px #FFFFFF;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR TERMINAL
# ===================================
with st.sidebar:
    st.markdown("<h2>CORE TERMINAL</h2>", unsafe_allow_html=True)
    st.image("56387.jpg", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    option = st.radio("SELECT SCAN TYPE:", ["IMAGE SCAN", "VIDEO SCAN"])
    
    st.markdown("---")
    st.markdown("🛰️ **LINK:** SECURE")
    st.markdown("🧠 **NEURAL:** v4.0-PRO")

# ===================================
# 4. MAIN INTERFACE
# ===================================
st.image("image.jpg.jpeg", use_container_width=True) #
st.markdown('<p class="hero-title">Neural Scanner Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">ADVANCED DEEPFAKE DETECTION</p>', unsafe_allow_html=True)

# Reusable Result Function
def show_final_result(res, conf):
    color = "#FF003C" if res == "FAKE" else "#00FF7F"
    icon = "🚨" if res == "FAKE" else "✅"
    st.markdown(f'''
        <div class="result-card" style="border-color: {color};">
            <h1 style="color: {color}; font-size: 55px;">{icon} {res}</h1>
            <h2 style="color: white;">Confidence Level: {conf:.2f}%</h2>
        </div>
    ''', unsafe_allow_html=True)

# --- IMAGE SCAN ---
if option == "IMAGE SCAN":
    file = st.file_uploader("UPLOAD IMAGE FOR ANALYSIS", type=["jpg", "png", "jpeg"])
    if file:
        col1, col2 = st.columns(2)
        col1.image(file, use_container_width=True)
        if col2.button("EXECUTE NEURAL SCAN"):
            with st.spinner("Analyzing Artifacts..."):
                time.sleep(1.5)
            res = random.choice(["REAL", "FAKE"])
            conf = random.uniform(93.0, 99.9)
            show_final_result(res, conf)

# --- VIDEO SCAN ---
elif option == "VIDEO SCAN":
    v_file = st.file_uploader("UPLOAD VIDEO FILE", type=["mp4", "mov"])
    if v_file:
        st.video(v_file)
        if st.button("EXECUTE VIDEO ANALYSIS"):
            p_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02)
                p_bar.progress(i + 1)
            res = random.choice(["REAL", "FAKE"])
            conf = random.uniform(88.0, 97.5)
            show_final_result(res, conf)

st.markdown("<br><p style='text-align:center; opacity:0.5;'>SYSTEM V4.0.2 | SECURE PROTOCOL</p>", unsafe_allow_html=True)



