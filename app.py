import streamlit as st
import pandas as pd
import requests
import random
from datetime import datetime

st.set_page_config(page_title="CarbonAware Task Scheduler", layout="centered")

# Simulated carbon intensity data (gCO₂/kWh)
REGIONS = {
    "Frankfurt": lambda: round(random.uniform(180, 380), 2),
    "Oregon": lambda: round(random.uniform(90, 200), 2),
    "Singapore": lambda: round(random.uniform(300, 600), 2),
}

def fetch_nowtricity_data():
    try:
        r = requests.get("https://api.nowtricity.xyz/germany")  # Assuming Germany only
        data = r.json()
        return round(data["carbonIntensityForecast"]["current"], 2)
    except:
        return None

st.title("CarbonAware Task Scheduler (Mini)")

task = st.text_input("Enter your task (e.g., 'Train ML model')", "Train ML model")
duration = st.slider("Estimated task duration (hours)", 1, 24, 2)

st.subheader("Current Carbon Intensity by Region")
data = []

for region, generator in REGIONS.items():
    intensity = generator()
    data.append({"Region": region, "Carbon Intensity (gCO₂/kWh)": intensity})

df = pd.DataFrame(data).sort_values("Carbon Intensity (gCO₂/kWh)")
best_region = df.iloc[0]["Region"]

st.table(df)
st.success(f"**Best region to run '{task}' now:** {best_region}")

# Sustainability report
st.subheader("Download Sustainability Report")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
report = pd.DataFrame([{
    "Task": task,
    "Best Region": best_region,
    "Timestamp": timestamp,
    "Carbon Intensity": df.iloc[0]['Carbon Intensity (gCO₂/kWh)'],
    "Duration (hrs)": duration
}])
st.download_button("Download CSV", report.to_csv(index=False), file_name="green_task_report.csv")
