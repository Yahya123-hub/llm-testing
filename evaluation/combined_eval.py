from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric, ToxicityMetric

from chatbot.app import get_response
from rag.retriever import retrieve_context

import subprocess
import json


def run_promptfoo(input_text, output_text):

    payload = {
        "input": input_text,
        "output": output_text
    }

    with open("temp_promptfoo.json", "w") as f:
        json.dump(payload, f)

    result = subprocess.run(
        ["npx", "promptfoo", "eval", "--config", "promptfooconfig.yaml"],
        capture_output=True,
        text=True
    )

    return result.stdout


def run_combined_eval(test_cases):

    results = []
    deepeval_cases = []   

    for tc in test_cases:

        input_text = tc["input"]

        context = retrieve_context(input_text)
        output = get_response(input_text)

        promptfoo_result = run_promptfoo(input_text, output)

        deepeval_case = LLMTestCase(
            input=input_text,
            actual_output=output,
            expected_output=tc.get("expected_output", ""),
            retrieval_context=context
        )

        deepeval_cases.append(deepeval_case)

        results.append({
            "input": input_text,
            "output": output,
            "promptfoo": promptfoo_result
        })

    metrics = [
        AnswerRelevancyMetric(threshold=0.7),
        FaithfulnessMetric(threshold=0.7),
        ToxicityMetric(threshold=0.0)
    ]

    deepeval_results = evaluate(
        test_cases=deepeval_cases,
        metrics=metrics
    )

    return results, deepeval_results