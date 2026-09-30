import json
from statistics import mean

with open("evaluated_results3.jsonl", "r", encoding="utf-8")as file:
    results = [json.loads(line) for line in file]

experiment = {
    "experiment": "experiment_v3_k3",
    "retriever_k": 3,
    "number_of_test_cases" : len(results),

    "metrics":{
        "answer_relevancy": mean(r["answer_relevancy"] for r in results),
        "faithfulness":mean(r["faithfulness"] for r in results),
        "context_relevancy":mean(r["context_relevancy"] for r in results),
        "correctness":mean(r["correctness"] for r in results),
    }
}

with open("experiment_v3.jsonl", "w", encoding="utf-8") as file:
    json.dump(experiment, file, indent=4)

print("experiment saved to experiment_v3.jsonl")