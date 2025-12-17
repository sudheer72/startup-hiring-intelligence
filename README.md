# Startup Hiring Intelligence Dashboard

A reproducible Streamlit-based dashboard that scores, ranks, and visualizes startups based on their likelihood of active tech hiring, using funding and hiring signals as input data.

This project focuses on the decision-making and visualization layer of a startup intelligence pipeline.

---

## Overview

<img width="1919" height="851" alt="Image" src="https://github.com/user-attachments/assets/f2babb41-9274-4a61-aa08-b9bc4d5d3fb6" />

After uploading the CSV file we can see the data of csv and also we can download the csv data
<img width="1916" height="880" alt="Image" src="https://github.com/user-attachments/assets/d2d0da73-b45a-4ecf-8f85-1e0b80807fea" />
The goal of this project is to help identify high-priority startups that are most likely to be actively hiring for technical roles.

The system assumes startup funding and hiring data as given input and focuses on:
- Scoring logic
- Ranking and prioritization
- Clean, verifiable visualization
- Reproducible outputs

This mirrors how real-world pipelines work, where ingestion and enrichment happen upstream and downstream systems consume structured data.

---

## Key Features

- Upload startup funding and hiring dataset (CSV)
- Probability-based hiring score (0–100)
- Priority classification (High / Medium / Low)
- Interactive AG Grid table:
  - Hover-based column menu (⋮)
  - Sort, pin, autosize, hide columns
  - Dark theme UI
- Sidebar filters for exploration
- Downloadable scored output (CSV)
- Fully reproducible (no screenshots or videos)

---

## Scoring Logic (High Level)

Each startup is scored using multiple signals:
- Funding size
- Hiring tier
- Number of active tech roles
- ATS presence (e.g. Greenhouse, Ashby)

These signals are combined into a transparent, deterministic probability score that reflects hiring intent.

---

## Data Source

This project uses sample startup funding and hiring data similar to the output produced by the reference repository:

AddyCuber/startup-data-pipeline

The data is treated as input to the system.  
The focus here is on downstream scoring, ranking, and visualization rather than data ingestion or scraping.

The solution is data-agnostic and works with any dataset that follows the same schema.

---

## Architecture

CSV Input
   ↓
Scoring Engine (Python)
   ↓
Ranking & Priority Classification
   ↓
Interactive Dashboard (Streamlit + AG Grid)
   ↓
Downloadable Output
 

---

## Tech Stack

- Python 3.x
- Streamlit
- Pandas
- streamlit-aggrid

---

## Run Locally

1. Clone the repository
```bash
git clone https://github.com/sudheer72/startup-hiring-intelligence.git
cd startup-hiring-intelligence
````

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

```bash
streamlit run app.py
```

Upload the CSV file when prompted.

---

## Reproducibility

* All logic is contained in the repository
* No external APIs required to run the demo
* Anyone can clone the repo, run the app, and reproduce the output
* Output can be independently verified via CSV download

---

## Intended Use Cases

* Hiring intelligence
* Startup scouting
* Sales / GTM lead prioritization
* Internal decision dashboards

---

## Notes

This project intentionally focuses on the decision and visualization layer of a startup intelligence workflow.
Upstream ingestion, enrichment, and crawling pipelines are assumed to be handled separately.

---
