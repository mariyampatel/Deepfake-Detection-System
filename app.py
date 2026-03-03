import streamlit as st
import time

# 1. Page Configuration (Sets the tab title and keeps layout compact)
st.set_page_config(page_title="Deepfake Neural Scanner", layout="centered")

# 2. Custom CSS for Neon glow, Blue Sidebar, and Sizing
st.markdown("""
<style>
/* Sidebar Background - A soothing deep blue */
[data-testid="stSidebar"] {
    background-color: #0B192C !important; 
}

/* Sidebar Text Color - White for visibility */
[data-testid="stSidebar"] * {
    color: #E2E8F0 !important;
}

/* Neon Title (Badi size) */
.neon-title {
    font-size: 3.5rem !important; 
    color: #ffffff;
    text-align: center;
    margin-bottom: 5px;
    text-shadow:
        0 0 5px #fff,
        0 0 10px #fff,
        0 0 20px #00ffff,
        0 0 40px #00ffff;
}

/* Neon Control Panel in Sidebar */
.neon-control {
    color: #00ffff !important;
    font-size: 1.8rem !important;
    text-align: center;
    text-shadow: 0 0 8px #00ffff;
    margin-bottom: 20px;
    font-weight: bold;
}

/* Main Interface Container - Restricts width so it isn't too big */
[data-testid="block-container"] {
    max-width: 750px !important; 
    padding-top: 2rem !important;
}

/* Custom Button Styling */
div.stButton > button {
    border: 1px solid #00ffff;
    color: #00ffff !important;
    background-color: transparent;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #00ffff;
    color: #0B192C !important;
    box-shadow: 0 0 15px #00ffff;
}
</style>
""", unsafe_allow_html=True)


# 3. Sidebar Setup
with st.sidebar:
    st.markdown('<div class="neon-control">Control Panel</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload Media (Video/Image)", type=['mp4', 'jpg', 'png', 'jpeg'])
    confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.5)
    analyze_btn = st.button("Run Scanner", use_container_width=True)


# 4. Main Interface Setup
# Title
st.markdown('<h1 class="neon-title">Deepfake Neural Scanner</h1>', unsafe_allow_html=True)

# Image right below the title (Chota size)
# Using columns to squeeze the image in the center so it stays small
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    # IMPORTANT: Replace "your_image.png" with the actual name of your image file
    # st.image("your_image.png", use_column_width=True) 
    st.markdown("<p style='text-align: center; color: gray;'>[Your Small Image Here]</p>", unsafe_allow_html=True)

st.markdown("---")

# 5. Application Logic (Optimized for quick loading)
if uploaded_file is not None:
    if analyze_btn:
        # Fast loading simulation for the video part
        with st.spinner("Scanning neural patterns..."):
            time.sleep(1.0) # Keeps the loading time extremely short
            
        st.success("Scan Complete!")
        
        # Displaying mock results
        st.write("### Analysis Results")
        st.info(f"Anomaly detected: 2% | Authenticity Confidence: {confidence_threshold * 100}%")
else:
    st.markdown("<h4 style='text-align: center;'>👈 Please upload a file from the Control Panel to begin.</h4>", unsafe_allow_html=True)
