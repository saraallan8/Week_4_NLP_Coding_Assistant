from llm import ask_llm 

def classify_intent(user_query):

    prompt = f"""
        Classify the user's request into exactly one category:
            1. Code Explanation: The user wants to understand or explain existing code.
            2. Code Generation: The user wants to create, write, or generate code.
            3. Out of Scope: The request is unrelated to explaining or generating code.
        Return only one category: Code Explanation, Code Generation, or Out of Scope.
        
        User request: {user_query}
    """

    response = ask_llm(prompt)
    
    return response.strip()
