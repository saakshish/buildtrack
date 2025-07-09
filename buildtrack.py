import streamlit as st
import pandas as pd
import networkx as nx

st.set_page_config(page_title="BuildTrack", layout="wide")
st.title("🏗️ BuildTrack – Smart Construction Scheduler & Optimizer")

tab1, tab2, tab3 = st.tabs(["📋 Task Scheduler", "🚚 Delivery Optimizer", "⏳ Delay Risk Predictor"])

# ---------------- TAB 1: TASK SCHEDULER ----------------
with tab1:
    st.header("📋 Task Dependency Scheduler")
    uploaded_file = st.file_uploader("📁 Upload Task CSV (columns: Task, DependsOn)", type="csv")

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.subheader("📄 Uploaded Task Data")
            st.dataframe(df)

            G = nx.DiGraph()
            edges_list = []

            for _, row in df.iterrows():
                task = row['Task']
                G.add_node(task)
                if pd.notna(row['DependsOn']):
                    deps = str(row['DependsOn']).split(",")
                    for dep in deps:
                        dep = dep.strip()
                        if dep:
                            G.add_edge(dep, task)
                            edges_list.append((dep, task))

            st.subheader("🔗 Dependencies")
            st.write(edges_list)

            if nx.is_directed_acyclic_graph(G):
                execution_order = list(nx.topological_sort(G))
                st.success("✅ Recommended Task Execution Order:")
                st.write(execution_order)
            else:
                st.error("❌ Dependency cycle found! Please fix the task list.")

        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.info("👈 Upload your task CSV to begin.")

# ---------------- TAB 2: DELIVERY OPTIMIZER ----------------
with tab2:
    st.header("🚚 Delivery Route Optimizer")
    uploaded_graph = st.file_uploader("📁 Upload Route CSV (columns: From, To, Distance)", type="csv", key="route")

    if uploaded_graph:
        try:
            df2 = pd.read_csv(uploaded_graph)
            st.subheader("📄 Uploaded Route Data")
            st.dataframe(df2)

            G2 = nx.DiGraph()
            for _, row in df2.iterrows():
                G2.add_edge(row['From'], row['To'], weight=row['Distance'])

            source = st.selectbox("📍 Select Warehouse/Source Node", df2['From'].unique())

            if st.button("🔎 Show Shortest Paths"):
                lengths, paths = nx.single_source_dijkstra(G2, source)
                st.subheader("📊 Shortest Distances from Source")
                st.write(lengths)

                st.subheader("🗺️ Paths")
                for dest, path in paths.items():
                    st.write(f"{source} ➡️ {dest} : {path}")

        except Exception as e:
            st.error(f"Error processing file: {e}")
    else:
        st.info("👈 Upload your route CSV to begin delivery planning.")

with tab3:
    st.subheader("⏳ Delay Risk Predictor")

    st.markdown("Use this tool to predict if a construction task is likely to be delayed based on resource availability and task type.")

    # --- Input Section ---
    task_type = st.selectbox("Select Task Type", ["Critical", "Medium", "Finishing"])
    resources = st.number_input("Resources Available", min_value=1, max_value=20, value=5)
    duration = st.number_input("Estimated Duration (in Days)", min_value=1, max_value=30, value=5)

    # --- Encode Inputs ---
    task_type_map = {"Critical": 0, "Finishing": 1, "Medium": 2}
    input_data = [[task_type_map[task_type], resources, duration]]

    import joblib
    try:
        model = joblib.load("delay_risk_model.pkl")

        if st.button("🔍 Predict Delay Risk"):
            prediction = model.predict(input_data)[0]
            confidence = model.predict_proba(input_data)[0][prediction]

            # DEBUG: Show raw output
            st.write(f"🔍 Raw Prediction: {prediction} (0 = On Time, 1 = Delay)")

            if prediction == 1:
                st.error(f"⚠️ High risk of delay! (Confidence: {confidence:.2%})")
            else:
                st.success(f"✅ Task is likely to be on track. (Confidence: {confidence:.2%})")
    except FileNotFoundError:
        st.error("❌ Model file not found. Please make sure 'delay_risk_model.pkl' is in the same folder.")
