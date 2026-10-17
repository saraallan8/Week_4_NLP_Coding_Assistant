import chromadb 
from datasets import load_dataset

dataset = load_dataset("openai/openai_humaneval", split="test")

print("Number of HumanEval problems:", len(dataset))

client = chromadb.PersistentClient(path = "./chroma_db")

collection = client.get_or_create_collection(name="coding_knowledge")

documents = [
    row["prompt"] + row["canonical_solution"] 
    for row in dataset
]

ids = [row["task_id"] for row in dataset]

collection.upsert(
    ids = ids,
    documents = documents
)

def retrieve_context(user_query):
    results = collection.query(
        query_texts=[user_query],
        n_results=5
    )

    documents = results['documents'][0]

    feedback = collection.query(
    query_texts=[user_query],
    n_results=2,
    where={
    "$and": [
        {"source": "human_feedback"},
        {"user_query": user_query}
    ]
}
)

    context = "\n".join(documents)

    feedback_documents = feedback["documents"][0]

    if feedback_documents:
       context += "\n" + "\n".join(feedback_documents)

    return context

def save_feedback(user_query, correct_solution):
    collection.upsert(
        ids = [f"feedback_{hash(user_query)}"],
        documents = [f"User request:{user_query}\nCorrect solution:\n{correct_solution}"],
        metadatas=[{"source": "human_feedback", "user_query": user_query}]
    )

