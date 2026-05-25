import streamlit as st

# Set layout to a wide dashboard canvas
st.set_page_config(page_title="SewerGEMS Interactive Masterclass", layout="wide")

# Main Header
st.title("SewerGEMS Interactive Tutorial App 🎓")
st.markdown("---")

# 1. SIDEBAR NAVIGATION (Divided into Videos & Sub-topics)
st.sidebar.header("📁 Course Content")

main_module = st.sidebar.selectbox(
    "Select a Main Video Module:",
    [
        "Module 1: Network Setup & Import",
        "Module 2: Design Constraints",
        "Module 3: Sanitary Load & Demand",
        "Module 4: Elevation & Simulation",
        "Module 5: Peak Factors & Infiltration",
        "Module 6: Thiessen Polygon Method"
    ]
)

# Dynamic sub-topic switching based on main module
if main_module == "Module 1: Network Setup & Import":
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["1.1 Concept: KMZ vs DXF", "1.2 Guide: Using ModelBuilder"])
elif main_module == "Module 2: Design Constraints":
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["2.1 Concept: Velocity & Cover", "2.2 Guide: Capacity (D/d) & Slopes"])
elif main_module == "Module 3: Sanitary Load & Demand":
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["3.1 Concept: Sanitary Load Types", "3.2 Guide: Load Control Center"])
elif main_module == "Module 4: Elevation & Simulation":
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["4.1 Concept: Elevation Basics", "4.2 Guide: Using the Trex Tool"])
elif main_module == "Module 5: Peak Factors & Infiltration":
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["5.1 Concept: Peak Modifiers", "5.2 Interactive: Flow Calculator"])
elif main_module == "Module 6: Thiessen Polygon Method":
    sub_topic = st.sidebar.radio("Go to Sub-Topic:", ["6.1 Concept: Polygon Theory", "6.2 Guide: LoadBuilder Setup"])

# 2. MAIN WORKSPACE CANVAS
st.subheader(f"📍 Current Lesson: {sub_topic}")

# --- MODULE 1 CONTENT ---
if sub_topic == "1.1 Concept: KMZ vs DXF":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.info("**Concept:** Google Earth (`.kmz`) stores geographic paths, but hydraulic engines like SewerGEMS need vector scale data (`.dxf`) to construct a perfect structural layout model.")
        st.markdown("""
        * **Step 1:** Trace your network path layout alignment in Google Earth.
        * **Step 2:** Save it as a `.kmz` file.
        * **Step 3:** Use AutoCAD or a GIS conversion engine to export it to a structural `.dxf` format.
        """)
    with col2:
        st.markdown("### 📱 How to Use This App Step-by-Step")
        st.success("Follow these steps on your computer while looking at your phone screen:")
        st.checkbox("1. Open Google Earth and locate your project zone.")
        st.checkbox("2. Trace lines for conduits and place points for manholes.")
        st.checkbox("3. Right-click your folder and select 'Save Place As' (.kmz).")

elif sub_topic == "1.2 Guide: Using ModelBuilder":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.markdown("""
        ### **ModelBuilder Wizard Setup**
        Instead of tracing pipes by hand, SewerGEMS uses **ModelBuilder** to automatically build your network map from your DXF file.
        """)
        st.code("""
        Data Source: CAD Files (.dxf)
        Unit Mapping: Meters (or Feet)
        Layer Mapping: 
          - Lines --> Conduits
          - Points --> Manholes / Junctions
        """, language="text")
    with col2:
        st.markdown("### 📱 How to Use This App Step-by-Step")
        st.checkbox("1. In SewerGEMS, click **Tools** -> **ModelBuilder**.")
        st.checkbox("2. Click **New**, select **CAD Files**, and browse for your DXF.")
        st.checkbox("3. Specify your data units precisely.")
        st.checkbox("4. Map your layers to correct element types and click **Finish**.")

# --- MODULE 2 CONTENT ---
elif sub_topic == "2.1 Concept: Velocity & Cover":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.warning("**Design Guardrails:** Gravity networks must comply with strict engineering constraints.")
        st.markdown("""
        * **Self-Cleansing Velocity ($\ge 0.6 \text{ m/s}$):** Moves wastewater solids so they do not settle and clog pipes.
        * **Max Velocity ($\le 3.0 \text{ m/s}$):** Stops highly abrasive fluids from eroding structural pipe walls.
        * **Minimum Cover ($\ge 1.0 \text{ m}$):** Ensures soil depth protects pipes from surface traffic collapse.
        """)
    with col2:
        st.markdown("### 📱 Interactive Constraints Reference")
        material = st.selectbox("Select Pipe Material Type:", ["Concrete", "PVC / HDPE"])
        if material == "Concrete":
            st.metric("Recommended Min/Max Velocity", "0.6 - 3.0 m/s")
            st.metric("Standard Min Cover Depth", "1.0 Meter")
        else:
            st.metric("Recommended Min/Max Velocity", "0.6 - 4.0 m/s")
            st.metric("Standard Min Cover Depth", "0.8 Meter")

elif sub_topic == "2.2 Guide: Capacity (D/d) & Slopes":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.markdown("""
        ### **Partly Full Flow Ratio (D/d)**
        * $d$ = depth of water flow
        * $D$ = total inside diameter of the pipe
        * **Rule:** A gravity sewer must *never* run completely full ($D/d = 1.0$). Keep it between **0.75 and 0.85** so sewer gases have space to escape without pressurizing.
        """)
    with col2:
        st.markdown("### 📱 How to Use This App Step-by-Step")
        st.checkbox("1. Open **Components** menu in SewerGEMS.")
        st.checkbox("2. Click **Design Constraints**.")
        st.checkbox("3. Select the **Gravity Pipe** tab.")
        st.checkbox("4. Set your maximum $D/d$ threshold value to 0.75.")

# --- MODULE 3 CONTENT ---
elif sub_topic == "3.1 Concept: Sanitary Load Types":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.info("**Concept:** You must tell SewerGEMS how much sewage water enters each manhole from surrounding homes.")
        st.markdown("""
        * **Unit Demand:** Assigning flow per capita (e.g., liters/person/day).
        * **Pattern Loads:** Accounts for time-of-day changes (more water is used in the morning than at midnight).
        """)
    with col2:
        st.markdown("### 🧮 Live Demand Tester")
        pop = st.number_input("Enter Population For Zone:", value=1000)
        per_capita = st.number_input("Water consumption per capita (L/day):", value=150)
        ret_factor = st.slider("Wastewater Return Factor:", 0.70, 0.90, 0.80)
        
        total_flow = (pop * per_capita * ret_factor) / 86400
        st.subheader(f"Calculated Input Flow: {total_flow:.3f} L/s")

elif sub_topic == "3.2 Guide: Load Control Center":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.markdown("""
        ### **Sanitary Load Control Center**
        Instead of clicking every manhole individually, use this global spreadsheet manager to apply wastewater inputs across your entire model at once.
        """)
    with col2:
        st.markdown("### 📱 How to Use This App Step-by-Step")
        st.checkbox("1. Go to **Tools** -> **Sanitary Load Control Center**.")
        st.checkbox("2. Click the **Add** dropdown icon at the top.")
        st.checkbox("3. Choose 'Initialize Loads for All Nodes' or select a group.")
        st.checkbox("4. Enter your calculated design flow rates in the data columns.")

# --- MODULE 4 CONTENT ---
elif sub_topic == "4.1 Concept: Elevation Basics":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.markdown("""
        ### **Ground vs. Invert Levels**
        Gravity sewer modeling depends completely on elevations:
        * **Ground Elevation:** Top surface level of your manhole.
        * **Invert Elevation:** The absolute bottom internal flow line of your pipes or structures.
        """)
    with col2:
        st.markdown("### 📱 Troubleshooting Simulation Errors")
        err = st.radio("Select an Issue:", ["Red Errors", "Yellow Warnings"])
        if err == "Red Errors":
            st.error("🔴 Fatal: The calculation engine cannot run. Check for completely missing elevation values or isolated, disconnected pipes.")
        else:
            st.warning("🟡 Warning: The engine computed results, but found structural layout violations (e.g., pipes placed too shallow or velocities dropping below 0.6 m/s).")

elif sub_topic == "4.2 Guide: Using the Trex Tool":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.markdown("""
        ### **Trex (Terrain Extractor)**
        Typing in thousands of ground elevation numbers by hand takes too long. **Trex** matches your network grid against an external surface profile map to extract elevations automatically.
        """)
    with col2:
        st.markdown("### 📱 How to Use This App Step-by-Step")
        st.checkbox("1. Click **Tools** -> **Trex**.")
        st.checkbox("2. Choose your File Source Type (DXF Contours, DEM, or Shapefile).")
        st.checkbox("3. Set your primary elevation unit field.")
        st.checkbox("4. Click **Apply** to map surface data directly to your elements.")

# --- MODULE 5 CONTENT ---
elif sub_topic == "5.1 Concept: Peak Modifiers":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.info("**Safety Margins:** Sewers must handle worst-case scenarios, not just basic daily averages.")
        st.markdown("""
        * **Peak Factor:** Multiplies your baseline average flows to protect against heavy morning/evening usage surges.
        * **Infiltration:** Adds an extra allowance for groundwater leaking into underground pipe cracks.
        * **Storm Allowance:** Safety padding for heavy rainfall leaking through ventilated manhole covers.
        """)
    with col2:
        st.markdown("### 📱 App Workflow Application Steps")
        st.checkbox("1. Open the Components menu -> Extreme Flows.")
        st.checkbox("2. Set up an Extreme Flow Method (e.g., Harmon or Babbitt formula setup).")
        st.checkbox("3. Apply this method to your active calculation options pipeline configuration.")

elif sub_topic == "5.2 Interactive: Flow Calculator":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Mathematical Formula Engine")
        st.latex(r"Q_{design} = (Q_{avg} \times PF) + Q_{inf} + Q_{storm}")
    with col2:
        st.markdown("### 🧮 Interactive Dynamic Solver")
        q_avg = st.number_input("Average Base Flow (L/s):", value=10.0)
        pf = st.slider("Peak Factor Multiplier:", 1.5, 4.5, 3.0)
        q_inf = st.number_input("Infiltration Flow (L/s):", value=1.2)
        q_storm = st.number_input("Storm Water Allowance (L/s):", value=0.5)
        
        q_design = (q_avg * pf) + q_inf + q_storm
        st.success(f"**Total Design Capacity Needed: {q_design:.2f} L/s**")

# --- MODULE 6 CONTENT ---
elif sub_topic == "6.1 Concept: Polygon Theory":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.markdown("""
        ### **Thiessen Polygon Service Allocations**
        * **What it does:** Generates geometric layout boundaries around each manhole structure.
        * **The Rule:** Any address inside a specific polygon boundary is closer to its enclosed manhole than to any other node in the system.
        * This allows you to precisely calculate and distribute localized population density loads to the right nodes.
        """)
    with col2:
        st.markdown("### 📱 How to Use This App Step-by-Step")
        st.checkbox("1. Prepare a boundary shapefile or CAD map of your service zones.")
        st.checkbox("2. Ensure your manhole node XY coordinate placements are finalized.")
        st.checkbox("3. Keep this layout file ready to run inside the LoadBuilder tool.")

elif sub_topic == "6.2 Guide: LoadBuilder Setup":
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### 📊 Interactive Presentation Slide")
        st.markdown("""
        ### **LoadBuilder Distribution Wizard**
        SewerGEMS utilizes the **LoadBuilder** module to automatically read spatial data maps and calculate polygon-based area demands.
        """)
    with col2:
        st.markdown("### 📱 How to Use This App Step-by-Step")
        st.checkbox("1. Click **Tools** -> **LoadBuilder**.")
        st.checkbox("2. Select **Area Load Data** -> **Proportional Distribution by Area**.")
        st.checkbox("3. Set your Node Layer as your Manholes.")
        st.checkbox("4. Choose your population density layer as the service area boundary file.")
        st.checkbox("5. Click **Calculate** to automatically apply distributed L/s demands.")
