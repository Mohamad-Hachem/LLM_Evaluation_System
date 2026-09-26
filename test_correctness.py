from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams
import json

with open("results.jsonl", "r") as f:
    line = f.readline()
    data = json.loads(line)


test_case = LLMTestCase(
        input = data["question"],
        actual_output = data["actual_answer"],
        expected_output= data["expected_answer"]
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

print("Score:", correctness_metric.score)
print("Reason:", correctness_metric.reason)