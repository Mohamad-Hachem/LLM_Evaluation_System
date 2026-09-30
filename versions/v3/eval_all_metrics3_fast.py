import json
from deepeval.metrics import AnswerRelevancyMetric,FaithfulnessMetric,ContextualRelevancyMetric,GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.evaluate import CacheConfig
from deepeval import evaluate

with open("results3.jsonl", "r", encoding="utf-8") as file:
    results = [json.loads(line) for line in file]

questions_tests = []

for i, result in enumerate(results, start=1):
    print(f"\nEvaluating test {i}/{len(results)}")

    context = result["context"]

    if isinstance(context,str):
        retrieval_context  = [context]
    else:
        retrieval_context = context

    test_case = LLMTestCase(
            input=result["question"],
            actual_output=result["actual_answer"],
            expected_output=result["expected_answer"],
            retrieval_context=retrieval_context
        )

    questions_tests.append(test_case)

answer_relevancy = AnswerRelevancyMetric(threshold=0.7)
faithfulness = FaithfulnessMetric(threshold=0.7)
context_relevancy= ContextualRelevancyMetric(threshold=0.7)
correctness = GEval(
            name="Correctness",
            criteria=(
                "Determine whether the actual output is factually correct based on the expect output"
            ),
            evaluation_params=[
                SingleTurnParams.ACTUAL_OUTPUT,
                SingleTurnParams.EXPECTED_OUTPUT
            ],
            threshold=0.7
            )

evaluation_results = evaluate(
    test_cases=questions_tests,
    metrics=[
        answer_relevancy,
        faithfulness,
        context_relevancy,
        correctness
    ],
    cache_config=CacheConfig(
        use_cache=False,
        write_cache=False
    )
)

evaluated_results = []

for i, (orginal_result, test_result) in enumerate(
    zip(results, evaluation_results.test_results),start=1
):
    answer_relevancy_score = None
    faithfulness_score = None
    context_relevancy_score = None
    correctness_score = None

    print("\nMetrics:")

    for metric in test_result.metrics_data or []:
        metric_name = metric.name.strip().lower()

        if metric_name == "answer relevancy":
            answer_relevancy_score = metric.score
        elif metric_name == "faithfulness":
            faithfulness_score = metric.score
        elif metric_name == "contextual relevancy":
            context_relevancy_score = metric.score
        elif metric_name.startswith("correctness"):
            correctness_score = metric.score

    evaluated_result = {
            **orginal_result,
            "answer_relevancy": answer_relevancy_score,
            "faithfulness": faithfulness_score,
            "context_relevancy": context_relevancy_score,
            "correctness": correctness_score
        }

    evaluated_results.append(evaluated_result)

with open("evaluated_results3.jsonl", "w", encoding="utf-8") as file:
    for result in evaluated_results:
        file.write(json.dumps(result,ensure_ascii=False)+"\n")

print("\nDone! Results saved to evaluated_results3.jsonl")