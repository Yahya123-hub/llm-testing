
JUDGE_PROMPT = """
You are an expert AI QA evaluator.

Evaluate the chatbot response based on the following criteria:

1. Relevance: Does it answer the user query properly?
2. Helpfulness: Does it guide the user clearly?
3. Career Guidance Quality: Does it suggest realistic options and ask clarifying questions when needed?
4. Grounding: Is it consistent with provided context?

Score each from 1 to 5.

Return JSON only:
{
"relevance": score,
"helpfulness": score,
"career_guidance": score,
"grounding": score,
"overall": average
}
"""