import json


files = [
    "baseline2.json",
    "experiment_v3.json",
    "experiment_v4.json",
]


experiments = []

for filename in files:
    with open(filename, "r", encoding="utf-8") as file:
        experiments.append(json.load(file))


with open("experiments_summary.json", "w", encoding="utf-8") as file:
    json.dump(experiments, file, indent=4)


print("Saved experiments_summary.json")
