from classifier import classify_intent 
from explain_code import explain_code
from generate_code import generate_code

def route_request(user_query, history=None):

    category = classify_intent(user_query)

    if category == "Code Explanation":
        return explain_code(user_query,history)
    elif category == "Code Generation":
        return generate_code(user_query,history)      
    else:
        return "I'm designed to explain existing code or generate code. Please ask me a coding-related question."

    