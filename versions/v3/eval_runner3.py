from RAG1.agent import ask
import json

with open("eval_dataset.jsonl", "r", encoding="utf-8") as file:
    test_cases = [json.loads(line) for line in file]

    results = []

    for test_case in test_cases:

        question = test_case["question"]
        expected_answer = test_case["expected_answer"]

        print(f"\n Question: {question}")

        rag_result = ask(question)

        result = {
            "question": question,
            "expected_answer": expected_answer,
            "actual_answer": rag_result["answer"],
            "context": rag_result["context"]
        }

        results.append(result)
        print(f"Answer: {rag_result['answer']}")

with open("results3.jsonl", "w", encoding="utf-8") as file:
    for result in results:
        file.write(json.dumps(result)+"\n")

print("\nDone! results3 saved to results3.jsonl")
