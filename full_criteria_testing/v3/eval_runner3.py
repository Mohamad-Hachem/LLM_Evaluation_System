from RAG3.agent import ask
import json

with open("eval_dataset.jsonl", "r", encoding="utf-8") as file:
    test_cases = [json.loads(line) for line in file]

    results = []

    for test_case in test_cases:

        question = test_case["question"]
        expected_answer = test_case["expected_answer"]

        print(f"\nQuestion: {question}")

        rag_result = ask(question)
        #rag_result = json.loads(rag_result)
        #print(f"this is rag result \n {rag_result}")
        
        result = {
            "question": question,
            "expected_answer": expected_answer,
            "actual_answer": rag_result["answer"],
            "context": rag_result["retrieval_context"]
        }

        results.append(result)

        print(f"Answer: {rag_result['answer']}")


with open("results3.jsonl", "w", encoding="utf-8") as file:
    for result in results:
        file.write(json.dumps(result) + "\n")


print("\nDone! Results saved to results.jsonl")