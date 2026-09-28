import json
from deepeval.metrics import AnswerRelevancyMetric,FaithfulnessMetric,ContextualRelevancyMetric,GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams


# Load only the first result
with open("results.jsonl", "r", encoding="utf-8") as file:
    first_result = json.loads(file.readline())


test_case = LLMTestCase(
    input=first_result["question"],
    actual_output=first_result["actual_answer"],
    expected_output=first_result["expected_answer"],
    retrieval_context=[first_result["context"]]
)


answer_relevancy = AnswerRelevancyMetric(threshold=0.7)
faithfulness = FaithfulnessMetric(threshold=0.7)
context_relevancy = ContextualRelevancyMetric(threshold=0.7)
correctness = GEval(
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


answer_relevancy.measure(test_case)
faithfulness.measure(test_case)
context_relevancy.measure(test_case)
correctness.measure(test_case)


print("\nQuestion:")
print(first_result["question"])

print("\nAnswer Relevancy:", answer_relevancy.score)
print("Faithfulness:", faithfulness.score)
print("Context Relevancy:", context_relevancy.score)
print("Correctness:", correctness.score)