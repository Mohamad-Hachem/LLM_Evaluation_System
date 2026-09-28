import json
from statistics import mean


with open("evaluated_results.jsonl", "r", encoding="utf-8") as file:
    results = [json.loads(line) for line in file]


baseline = {
    "experiment": "baseline_v1",

    "number_of_test_cases": len(results),

    "metrics": {
        "answer_relevancy": mean(
            r["answer_relevancy"] for r in results
        ),
        "faithfulness": mean(
            r["faithfulness"] for r in results
        ),
        "context_relevancy": mean(
            r["context_relevancy"] for r in results
        ),
        "correctness": mean(
            r["correctness"] for r in results
        ),
    }
}


with open("baseline.json", "w", encoding="utf-8") as file:
    json.dump(baseline, file, indent=4)


print("Baseline saved to baseline.json")