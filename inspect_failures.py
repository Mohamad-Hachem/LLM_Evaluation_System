import json


with open("evaluated_results.jsonl", "r", encoding="utf-8") as file:
    results = [json.loads(line) for line in file]


threshold = 0.7


print("\n===== CONTEXT RELEVANCY FAILURES =====\n")


for i, result in enumerate(results, start=1):

    if result["context_relevancy"] < threshold:

        print(f"--- Test {i} ---")

        print("\nQuestion:")
        print(result["question"])

        print("\nRetrieved Context:")
        print(result["context"])

        print("\nActual Answer:")
        print(result["actual_answer"])

        print("\nContext Relevancy Score:")
        print(result["context_relevancy"])

        print("\n" + "=" * 60 + "\n")