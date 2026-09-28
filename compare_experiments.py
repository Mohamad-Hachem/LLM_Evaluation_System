import json


with open("baseline2.json", "r", encoding="utf-8") as file:
    baseline = json.load(file)

with open("experiment_v3.json", "r", encoding="utf-8") as file:
    experiment = json.load(file)


print("\n========== EXPERIMENT COMPARISON ==========\n")

print(f"{'Metric':<22} {'Baseline k=3':<15} {'Experiment k=1':<15} {'Change':<10}")
print("-" * 65)

for metric in baseline["metrics"]:

    baseline_score = baseline["metrics"][metric]
    experiment_score = experiment["metrics"][metric]

    change = experiment_score - baseline_score

    print(
        f"{metric.replace('_', ' ').title():<22} "
        f"{baseline_score:<15.2f} "
        f"{experiment_score:<15.2f} "
        f"{change:+.2f}"
    )