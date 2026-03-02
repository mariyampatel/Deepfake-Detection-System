import streamlit as st
import random
from PIL import Image

# ===================================
# 1. PAGE CONFIGURATION
# ===================================
st.set_page_config(
    page_title="Deepfake Detection System",
    page_icon="🛡️", # Upgraded to a security shield for a more professional vibe
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================================
# 2. CUSTOM CSS (SaaS UI Design)
# ===================================
# Clean, modern styling with soft shadows, hover effects, and responsive badges
st.markdown("""
    <style>
    /* Global spacing improvements */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Hero Section Styling */
    .hero-container {
        text-align: center;
        padding: 2rem 0 3rem 0;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: -webkit-linear-gradient(45deg, #4CAF50, #2E7D32);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: #666;
    }

    /* Result Card Styling */
    .result-card {
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: 1rem;
        background-color: rgba(255, 255, 255, 0.05); /* Works for light & dark mode */
        border: 1px solid rgba(128, 128, 128, 0.2);
    }
    
    /* Colored Confidence Badges */
    .badge-real {
        background-color: rgba(0, 200, 83, 0.15);
        color: #00C853;
        padding: 8px 20px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 1.4rem;
        display: inline-block;
        margin-bottom: 1rem;
        border: 2px solid #00C853;
    }
    .badge-fake {
        background-color: rgba(255, 23, 68, 0.15);
        color: #FF1744;
        padding: 8px 20px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 1.4rem;
        display: inline-block;
        margin-bottom: 1rem;
        border: 2px solid #FF1744;
    }

    /* Modern Button Hover Effects */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.15);
    }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        padding-top: 3rem;
        font-size: 0.9rem;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# ===================================
# 3. CORE LOGIC (UNTOUCHED)
# ===================================
def predict_dummy():
    """Dummy prediction function - DO NOT ALTER"""
    prediction = random.choice(["Real", "Fake"])
    confidence = round(random.uniform(0.75, 0.99), 4)
    return prediction, confidence

def display_results(prediction, confidence):
    """Helper function to render the sleek UI result card"""
    st.markdown("### Analysis Complete")
    
    # Determine styles based on result
    if prediction == "Real":
        badge_class = "badge-real"
        icon = "✅"
    else:
        badge_class = "badge-fake"
        icon = "🚨"

    # Render Custom HTML Card
    st.markdown(f"""
        <div class="result-card">
            <div class="{badge_class}">
                {icon} {prediction.upper()}
            </div>
            <h4 style="margin-bottom: 5px;">Confidence Score</h4>
            <h2 style="margin-top: 0;">{confidence * 100:.2f}%</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Render Streamlit Progress Bar for visual feedback
    st.progress(float(confidence))

# ===================================
# 4. APP LAYOUT & UI
# ===================================

# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">Deepfake Detection System</div>
        <div class="hero-subtitle">Advanced AI analysis for image and video authenticity</div>
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation with Emojis
st.sidebar.title("🛡️ Settings & Nav")
st.sidebar.markdown("Select the type of media you wish to analyse:")
option = st.sidebar.radio("Input Type", ["🖼️ Image Analysis", "🎥 Video Analysis"])

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Ensure your media is clear and faces are visible for the best accuracy.")

# Create two responsive columns for the main layout (Desktop: side-by-side, Mobile: stacked)
col1, col2 = st.columns([1, 1], gap="large")

# ===================================
# IMAGE ANALYSIS SECTION
# ===================================
if option == "🖼️ Image Analysis":
    with col1:
        st.subheader("1. Upload Media")
        uploaded_file = st.file_uploader("Drag and drop an image here", type=["jpg", "jpeg", "png"])

        # Preview Container
        if uploaded_file is not None:
            with st.container(border=True):
                image = Image.open(uploaded_file)
                st.image(image, caption="Media Preview", use_container_width=True)

    with col2:
        st.subheader("2. AI Analysis")
        
        # Empty state handling
        if uploaded_file is None:
            st.info("👈 Please upload an image to begin analysis.")
        else:
            # Predict button is now separated logically into the action column
            if st.button("🔍 Run Deepfake Analysis", type="primary"):
                with st.spinner("AI is examining facial artifacts and pixels..."):
                    # Core logic triggered
                    prediction, confidence = predict_dummy()
                    # Display upgraded UI results
                    display_results(prediction, confidence)

# ===================================
# VIDEO ANALYSIS SECTION
# ===================================
elif option == "🎥 Video Analysis":
    with col1:
        st.subheader("1. Upload Media")
        uploaded_video = st.file_uploader("Drag and drop a video here", type=["mp4", "mov", "avi"])

        if uploaded_video is not None:
            with st.container(border=True):
                st.video(uploaded_video)

    with col2:
        st.subheader("2. AI Analysis")
        
        if uploaded_video is None:
            st.info("👈 Please upload a video file to begin analysis.")
        else:
            if st.button("🔍 Run Deepfake Analysis", type="primary"):
                with st.spinner("Extracting frames and analyzing temporal anomalies..."):
                    # Core logic triggered
                    prediction, confidence = predict_dummy()
                    # Display upgraded UI results
                    display_results(prediction, confidence)

# ===================================
# 5. FOOTER
# ===================================
st.markdown("""
    <div class="footer">
        <hr>
        © 2026 Deepfake Detection System | Built for Final Year Project<br>
        <i>Secure • Fast • Reliable</i>
    </div>
""", unsafe_allow_html=True)
