import json

from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams


with open("results.jsonl", "r", encoding="utf-8") as file:
    results = [json.loads(line) for line in file]


for i, result in enumerate(results, start=1):

    test_case = LLMTestCase(
        input=result["question"],
        actual_output=result["actual_answer"],
        expected_output=result["expected_answer"]
    )

    correctness_metric = GEval(
        name="Correctness",
        criteria=(
            "Determine whether the actual output is factually correct "
            "based on the expected output."
        ),
        evaluation_params=[
            SingleTurnParams.ACTUAL_OUTPUT,
            SingleTurnParams.EXPECTED_OUTPUT,
        ],
    )

    correctness_metric.measure(test_case)

    print(f"\n--- Test {i} ---")
    print("Question:", result["question"])
    print("Expected:", result["expected_answer"])
    print("Actual:", result["actual_answer"])
    print("Score:", correctness_metric.score)
    print("Reason:", correctness_metric.reason)