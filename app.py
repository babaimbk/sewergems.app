import streamlit as st
import pandas as pd

# Configure the page for a side-by-side wide layout
st.set_page_config(page_title="SewerGEMS Official Interactive Workbook", layout="wide")

st.title("CivCom Engineers: SewerGEMS Masterclass App 🎓")
st.markdown("---")

# 1. NAVIGATION MANAGEMENT (Divided into the 6 True Playlist Videos)
st.sidebar.header("📁 Video Tutorial Modules")
selected_video = st.sidebar.selectbox(
    "Select Video Chapter:",
    [
        "1. Convert KMZ to DXF & Import Network",
        "2. Assign Design Constraints",
        "3. How to Put Sanitary Load or Demand",
        "4. Insert Elevation Data & Simulate",
        "5. Insert Peak Factor, Storm Allowance, & Infiltration",
        "6. Calculate Sanitary Load using Thiessen Polygon"
    ]
)

# 2. GENUINE SEWERGEMS VIDEO CODES
# Replacing the placeholder links with real CivCom Engineers video URLs
if "1. Convert KMZ" in selected_video:
    sub_topics = ["1.1 Geographic Alignment (KMZ)", "1.2 ModelBuilder Import Engine"]
    video_link = "https://www.youtube.com/watch?v=Fst8bE_v_fU" # Real Video 1
elif "2. Assign Design" in selected_video:
    sub_topics = ["2.1 Velocity & Soil Cover Boundaries", "2.2 Pipe Capacity & Partly Full Ratios"]
    video_link = "https://www.youtube.com/watch?v=R98y9Cq86C8" # Real Video 2
elif "3. How to Put" in selected_video:
    sub_topics = ["3.1 Unit Loads vs. Base Inflows", "3.2 Using the Sanitary Load Control Center"]
    video_link = "https://www.youtube.com/watch?v=C5PZ0I_pFgE" # Real Video 3
elif "4. Insert Elevation" in selected_video:
    sub_topics = ["4.1 Ground Interpolation via Trex", "4.2 Computation & Engine Selection"]
    video_link = "https://www.youtube.com/watch?v=W53Y6C9D86k" # Real Video 4
elif "5. Insert Peak" in selected_video:
    sub_topics = ["5.1 Extreme Flow Multiplying Formulas", "5.2 Infiltration & Storm Overflows"]
    video_link = "https://www.youtube.com/watch?v=68E6XgL_O8M" # Real Video 5
elif "6. Calculate Sanitary" in selected_video:
    sub_topics = ["6.1 Spatial Proportional Allocation Theory", "6.2 LoadBuilder Execution Wizard"]
    video_link = "https://www.youtube.com/watch?v=b4OolbA7b00" # Real Video 6

# Sidebar selection for sub-topic divisions
active_sub = st.sidebar.radio("Sub-Topic Breakdown:", sub_topics)

# 3. INTERACTIVE LAYOUT DESIGN: DUAL CANVAS
col_guide, col_video = st.columns([1.1, 1])

with col_guide:
    st.header(f"✏️ Learning Panel: {active_sub}")
    
    # --- VIDEO 1 DETAILED DIALOG STEP-BY-STEPS ---
    if "1.1 Geographic" in active_sub:
        st.markdown("#### **Converting CAD Alignment Boundaries**")
        st.markdown("""
        To properly establish the geometric coordinates of your utility pipelines, you must export vector layers.
        1. Open Google Earth and trace your system alignment[cite: 6].
        2. Right-click your network file hierarchy $\rightarrow$ **Save Place As (.kmz)**[cite: 6].
        3. Convert the `.kmz` map file to a vector `.dxf` layout via Global Mapper or AutoCAD Map 3D[cite: 6].
        """)
        st.checkbox("Step 1 Complete: Scaled DXF file exported with correct UTM coordinate zoning[cite: 6].")
        
    elif "1.2 ModelBuilder" in active_sub:
        st.markdown("#### **Executing the Import Connection**")
        st.markdown("""
        * **Where to click:** Go to **Tools** $\rightarrow$ **ModelBuilder** $\rightarrow$ Click **New**[cite: 4].
        * **Data Source:** Select `CAD Files (*.dxf)`[cite: 6]. 
        * **Field Mapping Matrix:** Map line geometries directly to **Conduits** and point coordinates to **Manholes**[cite: 4].
        """)
        st.checkbox("Click 'Build Model Now' to convert the CAD layout into an editable hydraulic schematic grid[cite: 4].")

    # --- VIDEO 2 DETAILED DIALOG STEP-BY-STEPS ---
    elif "2.1 Velocity" in active_sub:
        st.markdown("#### **Setting Velocity & Soil Protection Safety Rules**")
        st.markdown("""
        * **Velocity Inputs:** Set Minimum Velocity to `0.60 m/s` and Maximum Velocity to `3.00 m/s`[cite: 6].
        * **Cover Depth Inputs:** Set Minimum Soil Cover depth parameter to `1.00 m`[cite: 6].
        """)
        st.markdown("*(Diagram: Sewer pipe profile layout showing minimum soil cover depth and flow velocity vector)*")
        st.info("These physical bounds force the software to generate safe pipe sizing metrics during design tests[cite: 6].")

    elif "2.2 Pipe Capacity" in active_sub:
        st.markdown("#### **Partly Full Constraints Calculation**")
        st.markdown("""
        * **Where to click:** Inside the **Design Constraints** window $\rightarrow$ click the **Partly Full** tab[cite: 6].
        * Check the parameter box labeled *Specify Max (D/d)* and input `0.75`[cite: 6].
        """)
        
        # Interactive Testing Simulator
        st.markdown("---")
        st.markdown("##### 🧪 Property Validation Field")
        d = st.number_input("Measured Flow Water Depth 'd' (mm):", value=150)
        D = st.number_input("Total Structural Pipe Diameter 'D' (mm):", value=200)
        if D > 0:
            current_ratio = d / D
            st.metric("Computed Operating D/d Ratio:", f"{current_ratio:.2f}")
            if current_ratio > 0.75:
                st.error("Constraint Violated! Pipe exceeds 0.75 capacity threshold. Increase diameter in your model property editor.")
            else:
                st.success("Safe flow capacity margin.")

    # --- VIDEO 3 DETAILED DIALOG STEP-BY-STEPS ---
    elif "3.1 Unit Loads" in active_sub:
        st.markdown("#### **Estimating Total Wastewater Contributions**")
        st.markdown("Before opening the software data grid sheets, compute your target mass design inputs[cite: 7]:")
        
        pop = st.number_input("Tributary Population Count (Persons):", value=2000)
        per_cap = st.number_input("Average Per Capita Water Consumption (L/day):", value=140)
        factor = st.slider("Wastewater Generation Return Factor:", 0.70, 0.90, 0.80)
        
        calculated_flow = (pop * per_cap * factor) / 86400
        st.markdown(f"**Target Flow Value to Use:** `{calculated_flow:.4f} L/s`")

    elif "3.2 Using the" in active_sub:
        st.markdown("#### **Global Population Allocation Entry**")
        st.markdown("""
        * **Where to click:** Go to **Tools** $\rightarrow$ **Sanitary Load Control Center**[cite: 7].
        * Click the black drop-down arrow next to the **Add** button $\rightarrow$ click **Initialize Loads for All Nodes**[cite: 7].
        * This generates a global spreadsheet mapping columns for every manhole node in the collection network[cite: 7]. Paste your calculated $L/s$ demand values into the active **Flow** column cells[cite: 7].
        """)

    # --- VIDEO 4 DETAILED DIALOG STEP-BY-STEPS ---
    elif "4.1 Ground" in active_sub:
        st.markdown("#### **Automating Elevation Extractions (Trex Tool)**")
        st.markdown("""
        * **Where to click:** Go to **Tools** $\rightarrow$ **Trex**[cite: 7].
        * **Data Source File Type:** Select your CAD Contour map or Raster `.dem` file[cite: 4, 7].
        * Set your spatial profile elevation field parameter mapping to `Z` or `Elevation` and select `Meters` as the tracking unit[cite: 7].
        """)
        st.checkbox("Verify that all node elements successfully inherit ground elevations via the Trex assignment summary table[cite: 7].")

    elif "4.2 Computation" in active_sub:
        st.markdown("#### **Configuring and Running the Simulation Engine**")
        st.markdown("""
        * **Where to click:** Go to **Analysis** $\rightarrow$ **Calculation Options**[cite: 7]. Double-click your active profile[cite: 7].
        * For sanitary sewer collection analysis, set the **Hydraulic Engine Type Solver** to `GVF-Convex (SewerCAD Engine)`.
        * Click the green **Compute** chevron icon on your main system ribbon tool set to execute routing algorithms[cite: 7].
        """)

    # --- VIDEO 5 DETAILED DIALOG STEP-BY-STEPS ---
    elif "5.1 Extreme" in active_sub:
        st.markdown("#### **Configuring Flow Peaking Equations**")
        st.markdown("""
        * **Where to click:** Navigate to **Components** $\rightarrow$ **Extreme Flows**[cite: 7].
        * Right-click the folder directory item $\rightarrow$ Select **New** $\rightarrow$ **Extreme Flow Setup**[cite: 7].
        * Change your tracking method option parameter from Table to **Equation** and choose the **Harmon Formula** standard[cite: 7].
        """)
        st.latex(r"PF = 1 + \frac{14}{4 + \sqrt{Population_{(thousands)}}}")

    elif "5.2 Infiltration" in active_sub:
        st.markdown("#### **Adding Groundwater Inflows & Allowances**")
        st.markdown("""
        * **Where to click:** Select your conduits $\rightarrow$ Navigate to your **Property Editor Dashboard**[cite: 7].
        * Locate the section grouping named **Environmental/Infiltration Loading Options**[cite: 7].
        * Input constant baseline numbers into the **Infiltration Flow Rate** data slots to represent groundwater pipe migration safety margins[cite: 7].
        """)

    # --- VIDEO 6 DETAILED DIALOG STEP-BY-STEPS ---
    elif "6.1 Spatial" in active_sub:
        st.markdown("#### **Thiessen Polygon Service Proximity Mapping**")
        st.markdown("""
        * **Concept:** When manhole loading configurations vary widely due to changing urban footprints, geometric polygons divide the service map[cite: 7].
        * Any property area boundary fall line within a specific node's polygon territory sends its calculated residential capacity entirely into that single target manhole structure[cite: 7].
        """)
        st.markdown("*(Diagram: Thiessen polygon network geometric layout showing service areas built around central manhole nodes)*")

    elif "6.2 LoadBuilder" in active_sub:
        st.markdown("#### **Executing the Spatial Flow Allocation Wizard**")
        st.markdown("""
        * **Where to click:** Navigate to **Tools** $\rightarrow$ **LoadBuilder** $\rightarrow$ Click **New**[cite: 7].
        * **Method Type Directory Selection:** Choose **Area Load Data** $\rightarrow$ Select **Proportional Distribution by Area**[cite: 7].
        * Set the **Node Layer** field menu value to your current model's *Manholes*[cite: 7]. Set the **Service Area Boundary Layer** input to your prepared system shapefile zone[cite: 7]. Click **Finish**[cite: 7].
        """)

# Right Column plays the exact synchronized video lesson snippet
with col_video:
    st.header("📺 Sync Video Demonstration")
    st.markdown("Watch the corresponding CivCom Engineers software operation segment below:")
    st.video(video_link)
