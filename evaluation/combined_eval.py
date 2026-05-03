from deepeval import evaluate
from deepeval.test_case import LLMTestCase

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

        results.append({
            "input": input_text,
            "promptfoo": promptfoo_result,
            "deepeval_input": deepeval_case
        })

    return results