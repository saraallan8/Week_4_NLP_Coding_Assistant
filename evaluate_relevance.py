from llm import ask_llm 

def evaluate_relevance(user_query, context):

    prompt = f"""

    You are evaluating retrieved examples for a coding assistant.

    User request:
    {user_query}

    Retrieved examples:
    {context}

    Judge relevance by the main task, not just shared words.
    Related topics are not enough; the examples must help solve the requested task.
    Return RELEVANT if at least one retrieved example provides a useful Python technique that can help solve the user's request, even if it solves a different problem.    Return NOT_RELEVANT only if none of the retrieved examples provides useful help.
    Return exactly one label: RELEVANT or NOT_RELEVANT.
    Do not include explanations or any other text.
"""

    response = ask_llm(prompt).strip().upper()
    print("Raw evaluator response:", repr(response))

    
    if "RELEVANT" in response and "NOT_RELEVANT" not in response:
      return "Relevant"
    elif response == "NOT_RELEVANT":
      return "Not Relevant"
    else:
      return "Not Relevant"
      