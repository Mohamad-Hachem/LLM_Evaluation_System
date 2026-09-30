import json
from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
EXPERIMENT_FILES = [
    PROJECT_ROOT / "experiment_v1.jsonl",
    PROJECT_ROOT / "experiment_v2.jsonl",
    PROJECT_ROOT / "experiment_v3.jsonl",
]

METRIC_COLUMNS = [
    "Answer Relevancy",
    "Faithfulness",
    "Context Relevancy",
    "Correctness",
]


def load_experiment(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_dataframe(experiments: list[dict]) -> pd.DataFrame:
    rows = []

    for experiment in experiments:
        metrics = experiment["metrics"]

        rows.append(
            {
                "Run": experiment["experiment"],
                "Retriever k": experiment["retriever_k"],
                "Test Cases": experiment["number_of_test_cases"],
                "Answer Relevancy": metrics["answer_relevancy"],
                "Faithfulness": metrics["faithfulness"],
                "Context Relevancy": metrics["context_relevancy"],
                "Correctness": metrics["correctness"],
            }
        )

    return pd.DataFrame(rows)


st.set_page_config(
    page_title="LLM Evaluation Dashboard",
    layout="wide",
)

st.title("LLM Evaluation Dashboard")
st.caption("Three saved evaluation runs for the single RAG1 pipeline.")

missing_files = [path.name for path in EXPERIMENT_FILES if not path.exists()]

if missing_files:
    st.error(f"Missing experiment summary file(s): {', '.join(missing_files)}")
    st.stop()

experiments = [load_experiment(path) for path in EXPERIMENT_FILES]
df = build_dataframe(experiments)

st.subheader("Saved Evaluation Runs")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Answer Relevancy": st.column_config.NumberColumn(format="%.3f"),
        "Faithfulness": st.column_config.NumberColumn(format="%.3f"),
        "Context Relevancy": st.column_config.NumberColumn(format="%.3f"),
        "Correctness": st.column_config.NumberColumn(format="%.3f"),
    },
)

st.subheader("Metric Comparison")

chart_df = df.set_index("Run")[METRIC_COLUMNS]
st.bar_chart(chart_df, use_container_width=True)

st.subheader("Inspect Run")

selected_run = st.selectbox(
    "Choose a run",
    df["Run"],
)

selected_row = df[df["Run"] == selected_run].iloc[0]

summary_cols = st.columns(2)
summary_cols[0].metric("Retriever k", int(selected_row["Retriever k"]))
summary_cols[1].metric("Test Cases", int(selected_row["Test Cases"]))

metric_cols = st.columns(4)

for column, metric_name in zip(metric_cols, METRIC_COLUMNS):
    column.metric(metric_name, f"{selected_row[metric_name]:.3f}")

st.subheader("Best Score By Metric")

best_rows = []

for metric_name in METRIC_COLUMNS:
    best_index = df[metric_name].idxmax()
    best_rows.append(
        {
            "Metric": metric_name,
            "Best Run": df.loc[best_index, "Run"],
            "Score": df.loc[best_index, metric_name],
        }
    )

st.dataframe(
    pd.DataFrame(best_rows),
    use_container_width=True,
    hide_index=True,
    column_config={
        "Score": st.column_config.NumberColumn(format="%.3f"),
    },
)
