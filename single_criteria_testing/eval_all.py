import json

from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


with open("results.jsonl", "r", encoding="utf-8") as file:
    results = [json.loads(line) for line in file]


    for i, result in enumerate(results, start=1):

        test_case = LLMTestCase(
            input=result["question"],
            actual_output=result["actual_answer"]
        )

        metric = AnswerRelevancyMetric(
            threshold=0.7
        )

        metric.measure(test_case)

        print(f"\n--- Test {i} ---")
        print("Question:", result["question"])
        print("Answer:", result["actual_answer"])
        print("Score:", metric.score)
        print("Passed:", metric.is_successful())
        print("Reason:", metric.reason)