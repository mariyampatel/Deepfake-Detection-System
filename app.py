import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="Vision AI Dashboard",
    page_icon="👁️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Professional Dark UI (No bright blue)
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }
    
    /* Sidebar Styling - Professional Dark Grey */
    [data-testid="stSidebar"] {
        background-color: #161B22;
        border-right: 1px solid #30363D;
    }
    
    /* Header Styling */
    .main-header {
        font-size: 36px;
        font-weight: 700;
        color: #2ECC71; /* Professional Emerald Green */
        margin-bottom: 10px;
        text-shadow: 0px 0px 10px rgba(46, 204, 113, 0.3);
    }
    
    /* Subtext */
    .sub-text {
        font-size: 18px;
        color: #8B949E;
        margin-bottom: 30px;
    }

    /* Cards/Containers */
    .stats-card {
        background-color: #1C2128;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363D;
        text-align: center;
    }

    /* Professional Button */
    .stButton>button {
        background-color: #238636;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 25px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2EA043;
        border: none;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🛠️ Control Panel")
    st.info("System Status: Online")
    
    menu = st.radio("Navigation", ["Home", "Biometric Scan", "Analytics", "Settings"])
    
    st.divider()
    st.markdown("### Scanner Settings")
    sensitivity = st.slider("Detection Sensitivity", 0, 100, 85)
    
    if st.button("Logout"):
        st.success("Logging out...")

# --- MAIN CONTENT ---

# Home Page Logic
if menu == "Home":
    # Hero Image (Aapki Image yahan display hogi)
    # Make sure to put your image file in the same folder as app.py
    try:
        header_img = Image.open("image.jpg.jpeg") # Image name check kar lena
        st.image(header_img, use_container_width=True)
    except:
        st.warning("Please place your header image in the folder as 'header_image.png'")

    st.markdown('<p class="main-header">Advanced Biometric Analysis</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Real-time facial recognition and architectural mapping system.</p>', unsafe_allow_html=True)

    # Stats Row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stats-card"><h3>99.7%</h3><p>Match Accuracy</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stats-card"><h3>0.02s</h3><p>Latency</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stats-card"><h3>Normal</h3><p>System Load</p></div>', unsafe_allow_html=True)

    st.write("---")
    
    # Bottom Section
    st.subheader("System Logs")
    st.code("""
    [INFO] Initializing Facial Mesh... DONE
    [INFO] Analyzing Artifact Density: 0.02
    [INFO] Motion Consistency Check: PASSED
    """, language="bash")

elif menu == "Biometric Scan":
    st.title("Live Scanner Interface")
    st.camera_input("Verify Identity")

else:
    st.title(f"{menu} Page")
    st.write("Section currently under maintenance.")
