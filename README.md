# GreenRouteAI
Mini-tool that analyzes the current co2 emissions and suggest the best region for your cloud work.

A simple Streamlit-based tool that helps you run cloud jobs in the greenest available region. It fetches real-time carbon intensity data and suggests where to route your task to minimize environmental impact.

## Features
- Real-time carbon intensity check (via Nowtricity or simulated data)
- Task input with estimated duration
- Recommends best region to run task
- Simulates future carbon trends (optional)
- Downloadable sustainability report

## How it helps
This tool is a part of the GreenRoute AI ecosystem, designed to make cloud workloads more sustainable by routing them to regions with the lowest carbon footprint at the time of execution.

## How to Use
1. Clone the repo
2. Run `streamlit run app.py`
3. Input your task and view the best region for sustainability
4. Download report if needed

## Future Additions
- Auto-routing to AWS/GCP
- Real-time carbon-aware cost simulation
- Integration with ML pipeline managers
