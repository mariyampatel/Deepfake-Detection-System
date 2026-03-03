import streamlit as st
import random
import time

# ================= ==================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Neural Scanner Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= ==================
# 2. INTENSE ULTRA-DARK UI (EYE-FRIENDLY & VISIBLE)
# ================= ==================
st.markdown("""
    <style>
    /* Global Application Background - Deep Space Black for maximum comfort */
    .stApp {
        background-color: #050608;
        color: #E0E0E0;
    }
    
    /* SIDEBAR - Ultra High Visibility (FIXED) */
    [data-testid="stSidebar"] {
        background-color: #0B0D11 !important;
        border-right: 2px solid #00FF7F; /* Green outline to define edge */
    }
    /* Making all text, labels, and icons in sidebar PURE WHITE for legibility */
    [data-testid="stSidebar"] *, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] p { 
        color: #FFFFFF !important; 
        font-weight: 500;
    }
    [data-testid="stSidebar"] h2 {
        color: #00FF7F !important;
        text-shadow: 0px 0px 10px rgba(0, 255, 127, 0.4);
    }

    /* HEADER TYPOGRAPHY */
    .hero-title {
        color: #00FF7F;
        font-size: 52px;
        font-weight: 800;
        text-align: center;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-top: 20px;
        margin-bottom: 0px;
        text-shadow: 0px 0px 20px rgba(0, 255, 127, 0.6);
    }
    .hero-subtitle {
        color: #888;
        text-align: center;
        font-size: 16px;
        letter-spacing: 8px;
        margin-top: -15px;
        margin-bottom: 40px;
    }

    /* GLASSMORPHISM CARD FOR RESULTS */
    .result-box {
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        background: rgba(255, 255, 255, 0.03); /* subtle white layer */
        backdrop-filter: blur(10px); /* blur effect */
        -webkit-backdrop-filter: blur(10px);
        border: 2px solid #FFFFFF;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }
    .result-text {
        font-size: 32px;
        font-weight: bold;
        text-transform: uppercase;
        margin-bottom: 5px;
    }
    .confidence-text {
        font-size: 18px;
        color: #FFFFFF;
    }

    /* INPUT ACCENTS (Uploader & Status Bar) */
    .stFileUploader label { color: #FFFFFF !important; }
    .stProgress > div > div > div > div { background-color: #00FF7F; }
    
    /* FAST INTERACTIVE BUTTON */
    div.stButton > button {
        background: transparent;
        color: #00FF7F;
        border: 2px solid #00FF7F;
        border-radius: 5px;
        padding: 12px 20px;
        font-weight: 700;
        transition: 0.3s ease;
        width: 100%;
    }
    div.stButton > button:hover {
        background: #00FF7F;
        color: #000000;
        border: 2px solid #00FF7F;
        box-shadow: 0px 0px 15px rgba(0, 255, 127, 0.6);
    }
    </style>
""", unsafe_allow_html=True)

# ================= ==================
# 3. CORE LOGIC (Content Unchanged)
# ===================================
def predict_dummy():
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

# ================= ==================
# 4. SIDEBAR - Pro layout
# ================= ==================
with st.sidebar:
    st.markdown("<h2>SYSTEM TERMINAL</h2>", unsafe_allow_html=True)
    # Technical GIF for Sidebar (using high-visibility source)
    st.image("56387.jpg", use_container_width=True)
    
    st.markdown("---")
    option = st.radio("SELECT MODE:", ["🖼️ Image Scan", "🎥 Video Scan"])
    
    st.markdown("---")
    st.info("System Status: Alpha-Secure")
    st.markdown("Artifact Density: 0.02")
    st.markdown("Latency: 0.02s")

# ================= ==================
# 5. HOME PAGE UI
# ================= ==================
col1, col2, col3 = st.columns([1, 8, 1])
with col2:
    # Use provided main image
    st.image("image.jpg.jpeg", use_container_width=True) 
    
    st.markdown('<p class="hero-title">Neural Scanner Pro</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">ADVANCED BIOMETRIC FORENSICS ENGINE V2.0</p>', unsafe_allow_html=True)

# ================= ==================
# 6. ANALYSIS SECTION
# ================= ==================
container = st.container()

with container:
    if option == "🖼️ Image Scan":
        uploaded_file = st.file_uploader("DROP FILE HERE FOR DEEP ANALYSIS", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            c1, c2 = st.columns(2)
            c1.image(uploaded_file, caption="Target Acquired", use_container_width=True)
            with c2:
                st.markdown("### Analysis TERMINAL")
                if st.button("EXECUTE NEURAL SCAN"):
                    with st.spinner("Decoding facial mesh..."):
                        time.sleep(1)
                    prediction, confidence = predict_dummy()
                    
                    if prediction == "Fake":
                        st.markdown(f'''
                            <div class="result-box" style="border-color: #FF003C; box-shadow: 0px 0px 15px rgba(255, 0, 60, 0.4);">
                                <p class="result-text" style="color: #FF003C !important;">🚨 DETECTED: {prediction.upper()}</p>
                                <p class="confidence-text">Deep Artifact Analysis: {confidence*100:.2f}%</p>
                            </div>
                        ''', unsafe_allow_html=True)
                    else:
                        st.markdown(f'''
                            <div class="result-box" style="border-color: #00FF7F; box-shadow: 0px 0px 15px rgba(0, 255, 127, 0.4);">
                                <p class="result-text" style="color: #00FF7F !important;">✅ VERIFIED: AUTHENTIC</p>
                                <p class="confidence-text">Pattern Consistency Check: {confidence*100:.2f}%</p>
                            </div>
                        ''', unsafe_allow_html=True)

    elif option == "🎥 Video Scan":
        uploaded_video = st.file_uploader("UPLOAD MULTI-FRAME SEQUENCE", type=["mp4", "mov"])
        if uploaded_video:
            st.video(uploaded_video)
            if st.button("ANALYZE TEMPORAL SEQUENCE"):
                progress = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress.progress(i + 1)
                st.success("Sequence Analysis Complete: Normal Consistency (Real)")

st.markdown("<br><br><p style='text-align:center; color:#555;'>Alpha-Secure Channel | v2.0</p>", unsafe_allow_html=True)

