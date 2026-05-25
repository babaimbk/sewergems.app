import streamlit as st

# Configure the page to look more like a wide canvas
st.set_page_config(page_title="SewerGEMS AI Assistant", layout="wide")

def main():
    st.title("SewerGEMS AI Design Assistant")
    st.markdown("Based on the CivCom Engineers Tutorial Series")

    # Sidebar for Workflow State Management
    st.sidebar.header("Design Workflow")
    workflow_step = st.sidebar.radio(
        "Select Phase:",
        [
            "1. KMZ/DXF Import & Setup",
            "2. Design Constraints",
            "3. Sanitary Load & Demand",
            "4. Elevation & Simulation",
            "5. Peak Factor & Infiltration",
            "6. Thiessen Polygon Loads"
        ]
    )

    # Canvas Layout: Split into Chat (Left) and Workspace (Right)
    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.subheader("AI Tutor & Guidance")
        st.info(f"Currently assisting with: **{workflow_step}**")
        
        # Chat Interface
        user_query = st.text_input("Ask a question about this step:")
        if st.button("Ask AI"):
            if user_query:
                # Placeholder for LLM/RAG call
                st.success(f"AI Response: To handle '{workflow_step}', ensure you have your CAD/GIS data ready...")

    with col2:
        st.subheader("Workspace & Configuration")
        
        # Dynamic UI based on workflow step
        if "Peak Factor" in workflow_step:
            st.markdown("### Advanced Parameters")
            peak_factor = st.slider("Peak Factor", 1.0, 5.0, 2.5)
            storm_allowance = st.number_input("Storm Allowance (L/s)", 0.0, 100.0, 10.0)
            infiltration = st.number_input("Infiltration Rate", 0.0, 50.0, 5.0)
            if st.button("Generate Config Report"):
                st.json({"Peak Factor": peak_factor, "Storm Allowance": storm_allowance, "Infiltration": infiltration})
                
        elif "Sanitary Load" in workflow_step:
            st.markdown("### Load Calculator")
            population = st.number_input("Population Served", 1000)
            per_capita_demand = st.number_input("Per Capita Demand (L/day)", 150)
            if st.button("Calculate Flow"):
                st.metric("Total Load (L/day)", population * per_capita_demand)

        else:
            st.write("Use this workspace to configure parameters for the selected workflow step.")

if __name__ == "__main__":
    main()
