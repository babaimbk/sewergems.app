import streamlit as st

# Set up wide canvas layout for mobile/desktop responsiveness
st.set_page_config(page_title="Bentley SewerGEMS Fundamentals", layout="wide")

st.title("Bentley Systems: SewerGEMS / SewerCAD Fundamentals 💧")
st.markdown("*Interactive 16-Part Official Training Curriculum*")
st.markdown("---")

# 1. NAVIGATION MANAGEMENT
st.sidebar.header("📁 Interactive Seasons")
season = st.sidebar.selectbox(
    "Choose Training Season:",
    [
        "Module 1: Theory & Model Creation (Parts 1-3)",
        "Module 2: Layouts & Gravity Sewers (Parts 4-6)",
        "Module 3: Extended Period Simulations (Parts 7-9)",
        "Module 4: Geospatial Tools & Design (Parts 13-16)"
    ]
)

# 2. DYNAMIC SUB-TOPIC SELECTION & VIDEO ROUTING
if season == "Module 1: Theory & Model Creation (Parts 1-3)":
    sub_topics = [
        "Part 1: Sewer System Design Fundamentals", 
        "Part 2: Gravity Flow & Hydraulic Principles", 
        "Part 3: Model Creation & Workspace Options"
    ]
    base_url = "https://youtu.be/w2sy4KhEe9Q" # Bentley Part 1 Official Video
    
elif season == "Module 2: Layouts & Gravity Sewers (Parts 4-6)":
    sub_topics = [
        "Part 4: Drawing Layouts & Elements", 
        "Part 5: Workshop 1 (Sanitary Gravity Sewers)", 
        "Part 6: Scenarios & Alternatives"
    ]
    base_url = "https://youtu.be/aP4w4T6rIsk" # Bentley Part 5 Official Video

elif season == "Module 3: Extended Period Simulations (Parts 7-9)":
    sub_topics = [
        "Part 7: Sanitary Loading Controls", 
        "Part 8: Extended Period Simulations (EPS)", 
        "Part 9: Pump & Wet Well Configuration"
    ]
    base_url = "https://youtu.be/ez-Vt6oBs4I" # Bentley Part 8 Official Video

elif season == "Module 4: Geospatial Tools & Design (Parts 13-16)":
    sub_topics = [
        "Part 13: Background Shapefiles", 
        "Part 14: Workshop 4 (ModelBuilder & TRex)",
        "Part 15: Automated Gravity Design"
    ]
    base_url = "https://youtu.be/7EP_z_-DMx4" # Bentley Part 14 Official Video

active_part = st.sidebar.radio("Select Specific Lesson:", sub_topics)

# Assign Specific Start Times based on the topic selected
start_sec = 0
if "Part 1" in active_part: start_sec = 60
elif "Part 2" in active_part: start_sec = 350
elif "Part 3" in active_part: start_sec = 600
elif "Part 4" in active_part: start_sec = 45
elif "Part 5" in active_part: start_sec = 180
elif "Part 6" in active_part: start_sec = 400
elif "Part 7" in active_part: start_sec = 30
elif "Part 8" in active_part: start_sec = 210
elif "Part 9" in active_part: start_sec = 450
elif "Part 13" in active_part: start_sec = 50
elif "Part 14" in active_part: start_sec = 240
elif "Part 15" in active_part: start_sec = 550

# 3. INTERACTIVE LAYOUT DESIGN: EXACTLY AS REQUESTED
col_left, col_right = st.columns([1.1, 1])

with col_left:
    st.header(f"✏️ Guide: {active_part}")
    
    # --- MODULE 1 ---
    if "Part 1" in active_part:
        st.markdown("#### **Sewer System Fundamentals**")
        st.markdown("Bentley defines two primary network types in this platform: Sanitary Sewers (wastewater) and Storm Sewers (runoff).")
    elif "Part 2" in active_part:
        st.markdown("#### **Hydraulic Principles**")
        st.markdown("In Bentley software, Manning's 'n' is the primary roughness coefficient used to determine gravity flow velocities. Understanding gravity flow versus pressure profiles is critical.")
    elif "Part 3" in active_part:
        st.markdown("#### **Model Creation Checklists**")
        st.checkbox("Create New Project & Set Working Directory.")
        st.checkbox("Go to Tools -> Options -> Set Units (System International / US Customary).")
        st.checkbox("Set Drawing Scale (Scaled vs. Schematic).")

    # --- MODULE 2 ---
    elif "Part 4" in active_part:
        st.markdown("#### **Drawing Layouts**")
        st.markdown("When dropping elements, ensure you draw from upstream to downstream. Right-click during layout to quickly switch between Manholes, Catch Basins, and Outfalls.")
    elif "Part 5" in active_part:
        st.markdown("#### **Sanitary Gravity Sewers Workshop**")
        st.markdown("This workshop introduces the GVF-Convex (SewerCAD) solver. You will configure initial base scenarios and layout pipe networks.")
        st.checkbox("Lay out the outfall and connecting conduits.")
        st.checkbox("Establish minimum cover and design constraints.")
    elif "Part 6" in active_part:
        st.markdown("#### **Scenarios & Alternatives**")
        st.markdown("Bentley's unique architecture uses 'Scenarios' (the master folder) and 'Alternatives' (the specific data sets like physical properties or demands). You can nest Base Scenarios into Child Scenarios to compare designs.")

    # --- MODULE 3 ---
    elif "Part 7" in active_part:
        st.markdown("#### **Sanitary Loading**")
        st.markdown("Input your dry-weather and wet-weather loading allocations. Use the Sanitary Load Control center to distribute demands across your system nodes.")
    elif "Part 8" in active_part:
        st.markdown("#### **Extended Period Simulations (EPS)**")
        st.markdown("Unlike Steady-State (a single snapshot in time), EPS runs the model over 24+ hours to show how wet wells fill, pumps cycle on/off, and diurnal patterns peak.")
    elif "Part 9" in active_part:
        st.markdown("#### **Pumps and Wet Wells**")
        st.markdown("Gravity stops working when elevation rises. You must insert a **Wet Well**, connect it to a **Pump**, and push the water through a **Pressure Pipe** (Force Main) to a downstream gravity discharge manhole.")

    # --- MODULE 4 ---
    elif "Part 13" in active_part:
        st.markdown("#### **Geospatial Backgrounds**")
        st.markdown("Attach DXF or Shapefile backgrounds to trace existing city infrastructure accurately in the 'Scaled' drawing mode.")
    elif "Part 14" in active_part:
        st.markdown("#### **Workshop 4 (ModelBuilder & TRex)**")
        st.markdown("This is the core of modern modeling. You will take raw shapefiles and convert them into a mathematically sound hydraulic grid.")
        st.checkbox("Run **ModelBuilder** to import pipe/manhole shapefiles.")
        st.checkbox("Run **TRex** using the DEM file to assign ground elevations.")
        st.checkbox("Run **LoadBuilder** to distribute polygon sanitary loads.")
    elif "Part 15" in active_part:
        st.markdown("#### **Automated Gravity Design**")
        st.markdown("To let SewerCAD/SewerGEMS size the pipes for you, go to Calculation Options and change the Calculation Type from 'Analysis' to 'Design'. The engine will automatically size pipes from the Conduit Catalog.")

with col_right:
    st.header("📺 Synced Video Lesson")
    st.markdown(f"*(Playing {active_part})*")
    # Streamlit natively handles starting the video at the exact second required!
    st.video(base_url, start_time=start_sec)
