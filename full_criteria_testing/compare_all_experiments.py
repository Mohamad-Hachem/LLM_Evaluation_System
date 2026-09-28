import json


with open("baseline2.json", "r", encoding="utf-8") as file:
    k3 = json.load(file)

with open("experiment_v4.json", "r", encoding="utf-8") as file:
    k2 = json.load(file)

with open("experiment_v3.json", "r", encoding="utf-8") as file:
    k1 = json.load(file)


print("\n========== ALL EXPERIMENTS ==========\n")

print(
    f"{'Metric':<22} "
    f"{'k=3':<10} "
    f"{'k=2':<10} "
    f"{'k=1':<10}"
)

print("-" * 55)


for metric in k3["metrics"]:

    score_k3 = k3["metrics"][metric]
    score_k2 = k2["metrics"][metric]
    score_k1 = k1["metrics"][metric]

    print(
        f"{metric.replace('_', ' ').title():<22} "
        f"{score_k3:<10.2f} "
        f"{score_k2:<10.2f} "
        f"{score_k1:<10.2f}"
    )
