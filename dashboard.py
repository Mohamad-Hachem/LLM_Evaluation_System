import json
import streamlit as st
import pandas as pd


st.title("LLM Evaluation Dashboard")


with open("experiments_summary.json", "r", encoding="utf-8") as file:
    experiments = json.load(file)


rows = []

for experiment in experiments:
    rows.append({
        "Experiment": experiment["experiment"],
        "Answer Relevancy": experiment["metrics"]["answer_relevancy"],
        "Faithfulness": experiment["metrics"]["faithfulness"],
        "Context Relevancy": experiment["metrics"]["context_relevancy"],
        "Correctness": experiment["metrics"]["correctness"],
    })


df = pd.DataFrame(rows)


st.subheader("Experiment Comparison")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.subheader("Metrics Comparison")

chart_df = df.set_index("Experiment")

st.bar_chart(chart_df)

st.subheader("Experiment Comparison")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)


st.subheader("Metrics Comparison")

chart_df = df.set_index("Experiment")

st.bar_chart(chart_df)

st.subheader("Inspect Experiment")

selected_experiment = st.selectbox(
    "Choose an experiment",
    df["Experiment"]
)

selected_row = df[
    df["Experiment"] == selected_experiment
].iloc[0]


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Answer Relevancy",
    f"{selected_row['Answer Relevancy']:.2f}"
)

col2.metric(
    "Faithfulness",
    f"{selected_row['Faithfulness']:.2f}"
)

col3.metric(
    "Context Relevancy",
    f"{selected_row['Context Relevancy']:.2f}"
)

col4.metric(
    "Correctness",
    f"{selected_row['Correctness']:.2f}"
)
