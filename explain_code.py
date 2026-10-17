from llm import ask_llm 

def explain_code(user_query,history=None):

    prompt = f""" 
            You are an AI coding assistant that explains code clearly.
            Explain the code step by step in simple language.

            User request:
            {user_query}
        """

    response = ask_llm(prompt,history)
    return response.strip()
    