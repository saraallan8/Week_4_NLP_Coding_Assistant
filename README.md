# AI Coding Assistant

An AI-powered coding assistant built with Python and Streamlit that helps users understand existing code and generate Python code. The project uses an LLM for code-related tasks, ChromaDB for retrieval-augmented generation (RAG), and Docker for isolated code execution.

## Features

- **Code Explanation:** Explains existing code in a clear and understandable way.
- **Code Generation:** Generates Python code based on user requests.
- **Intent Classification:** Classifies user requests and routes them to the appropriate workflow.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant coding examples from a ChromaDB collection to support code generation.
- **Relevance Evaluation:** Evaluates retrieved examples and provides a fallback response when they are not sufficiently relevant.
- **Human Feedback:** Stores user-provided corrections in ChromaDB to support future retrieval.
- **Conversation History:** Maintains conversation history during the current Streamlit session.
- **Code Execution:** Runs generated Python code inside Docker containers with execution timeouts and resource restrictions.
- **Error Handling:** Captures program output and Python errors and displays them in the interface.

## Technologies Used

- Python
- Streamlit
- OpenRouter API
- OpenAI Python client
- ChromaDB
- Sentence Transformers / embedding functions provided by the ChromaDB configuration
- Docker
- Hugging Face Datasets

## Project Structure

```text
NLP_Coding_Assistant/
├── app.py
├── classifier.py
├── code_runner.py
├── evaluate_relevance.py
├── explain_code.py
├── generate_code.py
├── llm.py
├── rag.py
├── router.py
├── test_llm.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd NLP_Coding_Assistant
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=your_available_openrouter_model
```

Replace the placeholder values with your own valid API key and a model available to your account.

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Install and start Docker Desktop

Install Docker Desktop and make sure the Docker engine is running.

Verify the installation:

```bash
docker --version
docker run --rm hello-world
```

The code runner uses a Python Docker image. If required, download it with:

```bash
docker pull python:3.12-alpine
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## How It Works

1. The user submits a coding request through the Streamlit interface.
2. The intent classifier identifies the type of request.
3. The router directs the request to the code explanation or code generation workflow.
4. For code generation, the RAG component retrieves relevant examples from ChromaDB.
5. The relevance evaluator checks whether the retrieved context is useful.
6. The LLM generates a response using the appropriate workflow.
7. Users can provide feedback and execute generated Python code through the Docker-based runner.

## Testing

Run the following command to check the syntax of the main project files:

```bash
python -m py_compile app.py code_runner.py generate_code.py router.py
```

Run the LLM-related test file with:

```bash
python test_llm.py
```

The LLM test may require a valid API key, network access, and available API quota.

## Security Notes

- API keys and other secrets must be stored in environment variables and excluded from version control.
- Generated code is executed in Docker containers rather than directly in the Streamlit application process.
- Container restrictions and timeouts help reduce execution risks, but Docker is not a perfect security boundary. Do not run untrusted code without appropriate additional isolation and security controls.

## Limitations

- Code generation depends on LLM availability, model capabilities, and API quotas.
- Retrieval quality depends on the coding examples available in ChromaDB.
- Conversation history is maintained within the current Streamlit session and is not guaranteed to persist across sessions.
- Docker Desktop must be installed and running for code execution.

## Future Improvements

- Improve intent classification and code generation accuracy.
- Expand the coding knowledge base.
- Add persistent conversation storage.
- Improve automated testing and retrieval evaluation.
- Strengthen isolation and resource controls for code execution.

## Author

Developed as an NLP and AI coding assistant project.
