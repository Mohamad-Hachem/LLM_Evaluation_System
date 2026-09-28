import json
from statistics import mean


with open("evaluated_results2.jsonl", "r", encoding="utf-8") as file:
    results = [json.loads(line) for line in file]


metrics = [
    "answer_relevancy",
    "faithfulness",
    "context_relevancy",
    "correctness",
]

threshold = 0.7


print("\n========== RAG EVALUATION SUMMARY ==========\n")


for metric in metrics:

    scores = [result[metric] for result in results]

    average_score = mean(scores)

    passed = sum(score >= threshold for score in scores)
    failed = len(scores) - passed

    pass_rate = passed / len(scores) * 100

    print(metric.replace("_", " ").title())
    print(f"Average Score : {average_score:.2f}")
    print(f"Passed        : {passed}/{len(scores)}")
    print(f"Failed        : {failed}/{len(scores)}")
    print(f"Pass Rate     : {pass_rate:.1f}%")
    print()