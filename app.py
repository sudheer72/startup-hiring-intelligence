import streamlit as st
import pandas as pd
from scoring_engine import score_startup

st.set_page_config(
    page_title="Startup Hiring Intelligence",
    layout="wide",
)

st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("## 🚀 Startup Hiring Intelligence Dashboard")
st.markdown(
    "This dashboard identifies, scores, and ranks startups based on their **hiring intent and funding strength**."
)

st.sidebar.markdown("## 🔍 Filters")

search_text = st.sidebar.text_input(
    "Search (Company, Country, Investor)"
)

min_score = st.sidebar.slider(
    "Minimum Hiring Score",
    min_value=0,
    max_value=100,
    value=0
)

uploaded_file = st.file_uploader(
    "Upload startup funding dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df = df.rename(columns={
        "Amount (USD)": "Amount_USD",
        "Hiring Tier": "Hiring_Tier",
        "Tech Roles": "Tech_Roles",
        "ATS Provider": "ATS_Provider",
        "Lead Investor": "Lead_Investor",
        "Date Announced": "Date_Announced"
    })

    scores = []
    priorities = []
    reasons = []

    for _, row in df.iterrows():
        score, priority, reason = score_startup(row)
        scores.append(score)
        priorities.append(priority)
        reasons.append(reason)

    df["Hiring_Score"] = scores
    df["Hiring_Priority"] = priorities
    df["Reason"] = reasons

    if search_text:
        search_text = search_text.lower()
        df = df[
            df.astype(str)
            .apply(lambda x: x.str.lower().str.contains(search_text))
            .any(axis=1)
        ]

    df = df[df["Hiring_Score"] >= min_score]

    df = df.sort_values("Hiring_Score", ascending=False).reset_index(drop=True)
    df.insert(0, "Rank", df.index + 1)

    st.markdown("### 📊 Scored Startup Output")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.download_button(
        label="⬇️ Download Qualified Startups (CSV)",
        data=df.to_csv(index=False),
        file_name="qualified_startups.csv",
        mime="text/csv"
    )
