from llm import ask_llm 
from rag import retrieve_context
from evaluate_relevance import evaluate_relevance
import re

def generate_code(user_query,history=None):
    
    context = retrieve_context(user_query)
    print("Retrieved context:", context)
    relevance = evaluate_relevance(user_query,context)

    print("context relevance:",relevance)

    if relevance != "Relevant":
        return "The retrieved examples are not relevant enough. Please provide a useful example or correct solution so I can help you better."


    prompt = f"""
    When modifying previous code, identify the function from the most recent relevant code-generation exchange. Ignore unrelated functions from older examples or retrieved context. Preserve the original function's name and purpose unless the user explicitly requests a change.
    Use the following examples as reference to generate a Python function that solves the user's query.
    {context}
    
    User request:
    {user_query}
    
    
    Generate a complete, executable Python function that solves the user's request.

    Return exactly one Python code block in this format:

    ```python
    def example():
    pass
   ```

   After the code block, write a short explanation.
   Include a simple test call after the function that prints its result.
   Keep the test call inside the Python code block.

   """

    response = ask_llm(prompt, history)

    match = re.search(r"```python\s*(.*?)```", response, re.DOTALL)

    if match:
     return match.group(1).strip()

    return ""

def extract_python_code(response):
    match = re.search(
        r"```(?:python)?\s*(.*?)```",
        response,
        re.DOTALL | re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    if response.strip().startswith(("def ", "async def ")):
        return response.strip()

    return ""