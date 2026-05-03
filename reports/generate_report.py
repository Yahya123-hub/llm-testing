def generate_report(results):

    total = len(results)

    pass_count = sum(1 for r in results if r["promptfoo"] == "PASS")
    fail_count = total - pass_count

    deepeval_scores = [r["deepeval_score"] for r in results if "deepeval_score" in r]

    avg_score = sum(deepeval_scores) / len(deepeval_scores)

    report = f"""
# 📊 FINAL EVALUATION REPORT

## Metrics
- Total test cases: {total}
- Pass rate: {pass_count / total * 100:.2f}%
- Fail rate: {fail_count / total * 100:.2f}%
- Avg DeepEval score: {avg_score:.2f}

## Observations
- Model struggles with vague queries
- Multi-step reasoning weak
- RAG improves factual grounding but not clarity

## Failure Breakdown
- Clarification failures: high
- Hallucination cases: medium
- Multi-step reasoning: weak

## Improvements Tried
- Prompt tuning
- RAG integration
- Structured output formatting
"""

    with open("reports/final_report.md", "w") as f:
        f.write(report)

    print("Report generated ✔")