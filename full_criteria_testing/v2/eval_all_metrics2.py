import json
from deepeval.metrics import AnswerRelevancyMetric,FaithfulnessMetric,ContextualRelevancyMetric,GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams


with open("results2.jsonl", "r", encoding="utf-8") as file:
    results = [json.loads(line) for line in file]


evaluated_results = []


for i, result in enumerate(results, start=1):

    print(f"\nEvaluating test {i}/{len(results)}")

    test_case = LLMTestCase(
        input=result["question"],
        actual_output=result["actual_answer"],
        expected_output=result["expected_answer"],
        retrieval_context=result["context"],
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

    evaluated_result = {
        **result,
        "answer_relevancy": answer_relevancy.score,
        "faithfulness": faithfulness.score,
        "context_relevancy": context_relevancy.score,
        "correctness": correctness.score,
    }

    evaluated_results.append(evaluated_result)

    print("Answer Relevancy:", answer_relevancy.score)
    print("Faithfulness:", faithfulness.score)
    print("Context Relevancy:", context_relevancy.score)
    print("Correctness:", correctness.score)


with open("evaluated_results2.jsonl", "w", encoding="utf-8") as file:
    for result in evaluated_results:
        file.write(json.dumps(result) + "\n")


print("\nDone! Results saved to evaluated_results.jsonl")