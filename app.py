import streamlit as st
import pandas as pd

# Set up wide canvas layout for mobile/desktop responsiveness
st.set_page_config(page_title="SewerGEMS Interactive Video Workbook", layout="wide")

# App Header
st.title("SewerGEMS Interactive Video Workbook 🎬")
st.markdown("---")

# 1. SIDEBAR: Course Navigation
st.sidebar.header("📁 Video Course Modules")
module = st.sidebar.selectbox(
    "Choose Video Lesson:",
    [
        "1. KMZ to DXF & ModelBuilder Import",
        "2. Design Constraints Configuration",
        "3. Sanitary Load & Demand Input",
        "4. Elevation Data (Trex) & Simulation",
        "5. Peak Factors & Environmental Modifiers",
        "6. Thiessen Polygon Area Loading"
    ]
)

# Dynamic sub-topic switching and video link assignment based on choice
# Note: Using standard instructional placeholders for video segment URLs
if "1. KMZ to DXF" in module:
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["1.1 Concept: KMZ vs DXF", "1.2 Guide: Using ModelBuilder"])
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=0s"  # Starts at 0m 0s
elif "2. Design Constraints" in module:
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["2.1 Concept: Velocity & Cover", "2.2 Guide: Capacity (D/d) & Slopes"])
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=95s"  # Starts at 1m 35s
elif "3. Sanitary Load" in module:
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["3.1 Concept: Sanitary Load Types", "3.2 Guide: Load Control Center"])
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=210s" # Starts at 3m 30s
elif "4. Elevation Data" in module:
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["4.1 Concept: Elevation Basics", "4.2 Guide: Using the Trex Tool"])
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=315s" # Starts at 5m 15s
elif "5. Peak Factors" in module:
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["5.1 Concept: Peak Modifiers", "5.2 Interactive: Flow Calculator"])
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=440s" # Starts at 7m 20s
elif "6. Thiessen Polygon" in module:
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["6.1 Concept: Polygon Theory", "6.2 Guide: LoadBuilder Setup"])
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=565s" # Starts at 9m 25s

st.markdown(f"### 📍 Current Lesson: {sub_topic}")

# 2. TWO-COLUMN SPLIT CANVAS LAYOUT
# Left Column = Instructions & Calculators | Right Column = Live Video Snippet
col_left, col_right = st.columns([1.1, 1])

with col_left:
    st.subheader("📝 Step-by-Step Interactive Guide")
    
    # --- MODULE 1 CONTENT ---
    if sub_topic == "1.1 Concept: KMZ vs DXF":
        st.info("**Concept:** Google Earth (`.kmz`) stores geographic lines, but SewerGEMS needs vector scale data (`.dxf`) to construct a structural model[cite: 6].")
        st.checkbox("1. Trace lines for conduits and points for manholes in Google Earth[cite: 4, 6].")
        st.checkbox("2. Save your folder as a `.kmz` file[cite: 6].")
        st.checkbox("3. Use a CAD converter to export it to a structural `.dxf` format[cite: 6].")
        
    elif sub_topic == "1.2 Guide: Using ModelBuilder":
        st.markdown("### **ModelBuilder Wizard Setup**")
        st.checkbox("1. In SewerGEMS, click **Tools** $\rightarrow$ **ModelBuilder**[cite: 6].")
        st.checkbox("2. Select **CAD Files (*.dxf)** as your source[cite: 6].")
        st.checkbox("3. Map Line layers to **Conduits** and Point layers to **Manholes**[cite: 6].")

    # --- MODULE 2 CONTENT ---
    elif sub_topic == "2.1 Concept: Velocity & Cover":
        st.warning("**Design Guardrails:** Flow must be fast enough to clean the pipe but slow enough to avoid structural damage[cite: 6].")
        st.write("* **Min Velocity:** $\ge 0.60 \text{ m/s}$ (prevents clogging)[cite: 6].")
        st.write("* **Max Velocity:** $\le 3.00 \text{ m/s}$ (prevents concrete wear)[cite: 6].")
        st.write("* **Min Cover Depth:** $\ge 1.00 \text{ m}$ (prevents pipe crushing)[cite: 6].")
        
    elif sub_topic == "2.2 Guide: Capacity (D/d) & Slopes":
        st.markdown("### **Partly Full Flow Constraints ($D/d$)**")
        st.checkbox("1. Go to **Components** $\rightarrow$ **Design Constraints**[cite: 6].")
        st.checkbox("2. Set maximum capacity ratio ($D/d$) between `0.75` and `0.80`[cite: 6].")

    # --- MODULE 3 CONTENT ---
    elif sub_topic == "3.1 Concept: Sanitary Load Types":
        st.info("**Concept:** Assigning how much baseline sewage wastewater is entering each manhole node[cite: 7].")
        pop = st.number_input("Tributary Population for Zone:", value=1200)
        per_capita = st.number_input("Water Consumption (L/capita/day):", value=150)
        ret_factor = st.slider("Wastewater Return Factor:", 0.70, 0.90, 0.85)
        total_flow = (pop * per_capita * ret_factor) / 86400
        st.metric("Calculated Target Flow for SewerGEMS:", f"{total_flow:.4f} L/s")

    elif sub_topic == "3.2 Guide: Load Control Center":
        st.markdown("### **Sanitary Load Control Center**")
        st.checkbox("1. Click **Tools** $\rightarrow$ **Sanitary Load Control Center**[cite: 7].")
        st.checkbox("2. Initialize rows for all nodes and input your calculated $L/s$ flows[cite: 7].")

    # --- MODULE 4 CONTENT ---
    elif sub_topic == "4.1 Concept: Elevation Basics":
        st.error("🔴 **Simulation Troubleshooting:** If your network throws a fatal error, check for completely missing ground or pipe invert elevations[cite: 7].")
        
    elif sub_topic == "4.2 Guide: Using the Trex Tool":
        st.markdown("### **Trex Terrain Extraction Wizard**")
        st.checkbox("1. Click **Tools** $\rightarrow$ **Trex**[cite: 7].")
        st.checkbox("2. Select your CAD Contour map or DEM file to extract elevations automatically[cite: 7].")

    # --- MODULE 5 CONTENT ---
    elif sub_topic == "5.1 Concept: Peak Modifiers":
        st.info("**Safety Margins:** Extreme flows must handle usage surges and weather infiltration[cite: 7].")
        
    elif sub_topic == "5.2 Interactive: Flow Calculator":
        st.latex(r"Q_{design} = (Q_{avg} \times PF) + Q_{inf}")
        q_avg = st.number_input("Average Flow (L/s):", value=10.0)
        pf = st.slider("Peak Factor Multiplier:", 1.5, 4.0, 3.0)
        q_inf = st.number_input("Infiltration (L/s):", value=1.5)
        st.success(f"**Total Design Capacity Target: {(q_avg * pf) + q_inf:.2f} L/s**")

    # --- MODULE 6 CONTENT ---
    elif sub_topic == "6.1 Concept: Polygon Theory":
        st.markdown("### **Thiessen Polygons**")
        st.write("Automatically creates geometric boundaries around manholes to divide load areas based on proximity[cite: 7].")
        
    elif sub_topic == "6.2 Guide: LoadBuilder Setup":
        st.markdown("### **LoadBuilder Distribution Wizard**")
        st.checkbox("1. Click **Tools** $\rightarrow$ **LoadBuilder**[cite: 7].")
        st.checkbox("2. Choose **Proportional Distribution by Area** to assign spatial population loads[cite: 7].")

# Right Column handles the dynamic video player
with col_right:
    st.subheader("📺 Video Demonstration")
    st.markdown("This video snippet will jump directly to the correct workflow timeline step:")
    # The native Streamlit video element automatically processes the timestamp parameter (&t=...)
    st.video(video_url)
