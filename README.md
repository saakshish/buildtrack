\# 🏗️ BuildTrack – Smart Construction Scheduler \& Optimizer

\*\*BuildTrack\*\* is an intuitive Streamlit-based web application designed to simplify construction management. It offers powerful tools for scheduling tasks based on dependencies, optimizing delivery routes, and predicting delay risks using machine learning. Built with construction teams and site managers in mind, it enables smart, data-driven decisions on the fly.


\## 🚀 Features

\### 📋 Task Dependency Scheduler
\- Upload a `.csv` file containing task names and their dependencies.
\- Visualize all dependencies as edge pairs.
\- Automatically detect circular dependencies.
\- Get the recommended execution order using topological sorting.

\### 🚚 Delivery Route Optimizer
\- Upload a `.csv` route file containing source, destination, and distance.
\- Select a source node (e.g., warehouse) and get:
&nbsp; - Shortest distances to all reachable nodes.
&nbsp; - Path breakdown using Dijkstra’s algorithm.

\### ⏳ Delay Risk Predictor
\- Predict whether a task is at risk of being delayed based on:
&nbsp; - Task type (Critical, Medium, Finishing)
&nbsp; - Number of available resources
&nbsp; - Estimated duration

\- Built using a Random Forest classifier trained on synthetic data.
\## 📂 File Structure
| File                | Description                                                   

| `buildtrack.py`          | Main Streamlit application with all three modules integrated. 

| `train\_model.py`        | Script to train and export the delay risk prediction model.    

| `delay\_risk\_model.pkl` | Pre-trained Random Forest model used for predicting task delays. 

|`requirements.txt`        | Python dependencies to run the app.                            

| `tasks.csv`              | Sample task list with dependencies. 

| `routes.csv`             | Sample graph data for delivery route optimization. 


\## 📥 Installation

```bash
git clone https://github.com/saakshish/buildtrack.git

cd buildtrack

pip install -r requirements.txt

streamlit run buildtrack.py


🧠 Model Details (Delay Risk Predictor)

Algorithm: Random Forest Classifier
Input Features-
TaskType: Encoded (Critical = 0, Finishing = 1, Medium = 2)
Resources: Integer count
Duration: Estimated days
Target: Delayed (0 = On Time, 1 = Delay)


To retrain:
```bash
python train\_model.py

🛠️ Tech Stack-
Python
Streamlit
pandas
networkx
scikit-learn
joblib





