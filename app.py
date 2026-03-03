import streamlit as st
from PIL import Image

# 1. Page Configuration (Keep original icon)
st.set_page_config(
    page_title="AI Project Dashboard",
    page_icon="🐶",  # Keep the 'dogy' icon
    layout="wide"
)

# 2. Updated CSS: Integrating the Face-Scan Image as a Header
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    /* Keep Original Sidebar Colors */
    [data-testid="stSidebar"] {
        background-color: #1a1c24;
    }
    
    /* 1. KEY CHANGE: Dynamic Header Section using the Image as Background */
    #face-mesh-header {
        position: relative;
        overflow: hidden;
        border-radius: 10px;
        border: 1px solid #30363D;
        margin-bottom: 25px;
        background-color: #1C2128;
    }
    
    #face-mesh-image-overlay {
        width: 100%;
        height: auto;
        opacity: 0.2; /* Fades image into background */
        object-fit: cover;
    }
    
    #face-mesh-content {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: #E0E0E0;
        text-align: center;
        padding: 20px;
    }
    
    /* Title with Soft Green Glow to match image mesh */
    #face-mesh-content h1 {
        font-size: 42px;
        color: #00FF7F; /* Spring Green */
        margin-top: 0px;
        margin-bottom: 0px;
        font-weight: 700;
        text-shadow: 0px 0px 10px rgba(0, 255, 127, 0.4);
    }
    
    /* Data Points in Header using image color accents */
    .data-point {
        color: #00FF7F;
        font-weight: bold;
    }

    /* 2. Color Matching Cards: Using the soft gray/blue from the original */
    .dashboard-card {
        background-color: #262933; /* Soft gray/blue from original theme */
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363D;
    }
    
    /* Use original colors for normal text in cards */
    .dashboard-card h3 {
        color: #FFFFFF !important;
    }
    .dashboard-card p {
        color: #8B949E !important;
    }
    
    /* Professional Blue for interactive elements - non-chubne wala */
    .stButton>button {
        background-color: #1D4ED8; 
        color: white;
    }
    .stButton>button:hover {
        background-color: #2563EB;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR --- (Keeping it exactly as original)
with st.sidebar:
    st.image("56387", width=100)
    st.markdown("## Navigation 🐶")
    
    menu = st.radio("Go to", ["Home", "Scan Profile", "Database", "Analytics", "Settings"])
    
    st.divider()
    st.subheader("System Controls")
    scan_btn = st.button("Start New Scan")
    if scan_btn:
        st.success("Starting scan...")
    
    st.markdown("### Database Status")
    st.metric(label="Profiles Stored", value="1,245", delta="+5%")
    
    st.error("Urgent Security Alert!")

# --- MAIN CONTENT ---

# Page Logic
if menu == "Home":
    
    # --- DYNAMIC HEADER ---
    # Try to load the provided image. Set image_path to where you saved it.
    image_path = "header_image.png" 
    
    st.markdown('<div id="face-mesh-header">', unsafe_allow_html=True)
    
    try:
        # Load the image and get base64 to embed it
        import base64
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()
        
        st.markdown(f'<img id="face-mesh-image-overlay" src="data:image/png;base64,{encoded_image}">', unsafe_allow_html=True)
    except:
        # Placeholder or nothing if image fails
        st.markdown('<div id="face-mesh-image-overlay" style="min-height:200px"></div>', unsafe_allow_html=True)
        st.warning(f"Please place your image '{image_path}' in the same folder as app.py")

    # Content overlaid on top of the image
    st.markdown('<div id="face-mesh-content"><h1>BIOMETRIC COMMAND</h1>', unsafe_allow_html=True)
    st.markdown(f'<h3>Active Analysis: Match <span class="data-point">99.7%</span> | Artifacts: <span class="data-point">0.02</span></h3>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)
    
    st.divider()
    
    # --- DASHBOARD LAYOUT (Keeping original style and content) ---
    st.subheader("Project Overview")
    
    # Original-style columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### Profile Status")
        st.write("Current analysis of 1,245 profiles in database.")
        st.write("**Latest Scan:** John Doe | ✅ Matched")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### Database Info")
        st.write("AI model version: **VisionAI v2.1**")
        st.write("Database Integrity: **Good**")
        st.write("Last updated: 2 hours ago")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="dashboard-card">', unsafe_allow_html=True)
        st.markdown("### Model Metrics")
        st.write("Face Match Latency: **0.02s**")
        st.write("Face Detection Accuracy: **99.7%**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("---")
    
    st.subheader("Recent System Logs")
    # Original style logs
    st.code("""
    [INFO] 14:32:01 Initializing Facial Mesh... DONE
    [INFO] 14:32:02 Artifact Density: 0.02
    [INFO] 14:32:02 Motion Consistency: NORMAL
    [INFO] 14:32:03 Matching against Database: DONE (Profile #0012)
    [SUCCESS] 14:32:03 Profile John Doe confirmed. Latency: 0.02s
    """, language="bash")
    
    st.button("Request New Profile Authorization")

else:
    # Handle other pages as they were, but maybe link them better
    st.title(f"{menu} Page")
    st.write("This section is under development.")
