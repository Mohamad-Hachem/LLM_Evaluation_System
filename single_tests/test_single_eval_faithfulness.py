from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="Where do penguins live?",
    actual_output="Penguins live in a variety of environments in the Southern Hemisphere. They are commonly associated with the icy coasts of Antarctica, but they also inhabit the cool shores of South America, southern Africa, and even the Galapagos Islands near the equator.",
    retrieval_context=["Penguins are flightless seabirds that are specially adapted for life in the Southern Hemisphere. Although people often associate them only with Antarctica, penguins live in a wide range of environments, including the icy coasts of Antarctica, the cool shores of South America and southern Africa, and even the Galapagos Islands near the equator. Their upright posture, compact bodies, and distinctive black-and-white coloring make them among the most recognizable birds in the world."]
)


metric = FaithfulnessMetric(threshold=0.7)

metric.measure(test_case)


print("Score: ", metric.score)
print("Reason: ", metric.reason)
print("Passed: ", metric.is_successful())