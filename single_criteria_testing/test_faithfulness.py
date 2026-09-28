from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase


test_case = LLMTestCase(
    input="What do penguins eat?",

    actual_output=(
        "Penguins primarily feed on marine animals, "
        "including krill, fish, and squid."
    ),

    retrieval_context=[
        "Penguin diets vary by species and location, "
        "but most feed on marine animals. Small species may "
        "rely heavily on krill and tiny fish, while larger "
        "penguins can pursue bigger fish and squid."
    ]
)


metric = FaithfulnessMetric(
    threshold=0.7
)

metric.measure(test_case)

print("Score:", metric.score)
print("Passed:", metric.is_successful())
print("Reason:", metric.reason)