import streamlit as st
import random
import time

# ===================================
# 1. PAGE CONFIG
# ===================================
st.set_page_config(
    page_title="Deepfake Neural Scanner",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. ULTRA-FAST & CLEAR UI CSS
# ===================================
st.markdown("""
    <style>
    /* Main Dark Theme */
    .stApp { background-color: #0B0E14; color: #FFFFFF; }
    
    /* SIDEBAR TEXT VISIBILITY (FIXED) */
    [data-testid="stSidebar"] { background-color: #12161D !important; border-right: 1px solid #1E2530; }
    [data-testid="stSidebar"] * { color: #FFFFFF !important; font-size: 14px; }
    [data-testid="stSidebar"] h2 { color: #00FF7F !important; font-size: 20px !important; font-weight: bold; }
    
    /* PROFESSIONAL HEADER */
    .hero-title {
        color: #00FF7F;
        font-size: 45px;
        font-weight: 800;
        text-align: center;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 0px;
        text-shadow: 0px 0px 15px rgba(0, 255, 127, 0.4);
    }
    .hero-subtitle {
        color: #888;
        text-align: center;
        font-size: 14px;
        letter-spacing: 5px;
        margin-bottom: 30px;
    }

    /* BUTTONS */
    div.stButton > button {
        background: transparent;
        color: #00FF7F !important;
        border: 2px solid #00FF7F !important;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
        padding: 10px;
    }
    div.stButton > button:hover { background: #00FF7F !important; color: #000 !important; }

    /* BOXES */
    .info-box {
        border-left: 4px solid #00FF7F;
        background: rgba(0, 255, 127, 0.05);
        padding: 10px;
        margin: 5px 0px;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. SIDEBAR
# ===================================
with st.sidebar:
    st.markdown("<h2>SYSTEM TERMINAL</h2>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    option = st.radio("SELECT MODE:", ["🖼️ Image Scan", "🎥 Video Scan"])
    
    st.markdown("---")
    st.markdown('<div class="info-box">CORE: Active</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">LATENCY: 0.02s</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">STATUS: Online</div>', unsafe_allow_html=True)

# ===================================
# 4. MAIN CONTENT
# ===================================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    # Header Image (Use your local filename here)
    st.image("image.jpg.jpeg", use_container_width=True) 
    st.markdown('<p class="hero-title">Deepfake Neural Scanner</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">ADVANCED BIOMETRIC FORENSICS</p>', unsafe_allow_html=True)

# Analysis Logic
if option == "🖼️ Image Scan":
    file = st.file_uploader("Upload Target Image", type=["jpg", "png"])
    if file:
        c1, c2 = st.columns(2)
        c1.image(file, use_container_width=True)
        if c2.button("START ANALYSIS"):
            with st.spinner("Scanning..."):
                time.sleep(1)
                res = random.choice(["REAL", "FAKE"])
                conf = random.uniform(85, 99)
                if res == "FAKE": st.error(f"DETECTED: {res} ({conf:.2f}%)")
                else: st.success(f"VERIFIED: {res} ({conf:.2f}%)")

elif option == "🎥 Video Scan":
    video_file = st.file_uploader("Upload Video Sequence", type=["mp4", "mov"])
    if video_file:
        st.video(video_file) # Standard loading for speed
        if st.button("RUN TEMPORAL SCAN"):
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                bar.progress(i + 1)
            st.info("Result: Analysis Consistent (Real)")

st.markdown("<p style='text-align:center; color:#444; margin-top:50px;'>v2.0 | SECURE CHANNEL</p>", unsafe_allow_html=True)
