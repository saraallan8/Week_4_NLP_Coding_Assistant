import streamlit as st 
from router import route_request
from rag import save_feedback
from code_runner import run_code
from generate_code import extract_python_code

if "messages" not in st.session_state:
    st.session_state.messages = []

if "generated_code" not in st.session_state:
    st.session_state.generated_code = ""

st.set_page_config(page_title="AI Coding Assistant")

st.title("AI Coding Assistant")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.write("Welcome to the AI Coding Assistant! I'm here to help you with coding tasks. You can ask questions about code or request new code.")

user_query = st.text_area("Enter your coding question or request:")

if st.button("Submit"):
    if user_query.strip():
        
        history = st.session_state.messages.copy()

        response = route_request(user_query, history)
        st.session_state.generated_code = extract_python_code(response)

        st.session_state.messages.append({
        "role": "user",
        "content": user_query
        })
        st.session_state.messages.append({
            "role":"assistant",
            "content": response
        })

        st.rerun()

st.subheader("Human Feedback")
correct_solution = st.text_area("Provide a correct solution:")

if st.button("Save Feedback"):
    if user_query.strip() and correct_solution.strip():
        save_feedback(user_query, correct_solution)
        st.success("Correct solution saved to chroma!")
    else:
        st.warning("Please enter both the coding request and the correct solution. ")    

st.subheader("Code Execution")

if st.session_state.generated_code:
    if st.button("Run Code"):
        output, error = run_code(st.session_state.generated_code)

        if output:
            st.text_area("Output", output, height=150)

        if error:
            st.text_area("Error", error, height=200)

        if not output and not error:
            st.info("Code executed successfully, but produced no output.")    
else:
    st.info("Generate Python code first to run it.")        