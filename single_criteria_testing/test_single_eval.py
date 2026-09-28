from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase


test_case = LLMTestCase(
    input="What do penguins eat?",
    actual_output=(
        "Penguins primarily feed on marine animals. "
        "Smaller species often eat krill and tiny fish, "
        "while larger penguins may eat bigger fish and squid."
    )
)

metric = AnswerRelevancyMetric(
    threshold=0.7
)

metric.measure(test_case)

print("Score:", metric.score)
print("Reason:", metric.reason)
print("Passed:", metric.is_successful())