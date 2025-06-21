from fastapi import FastAPI, Query
from pydantic import BaseModel
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import uvicorn

# Load your saved files
vectorizer = joblib.load("./models/tfidf_vectorizer.pkl")
sentences = joblib.load("./models/all_sentences.pkl")  # list of (text, source)

X = joblib.load("./data/tfidf_matrix.pkl")  # tf-idf sparse matrix

app = FastAPI()

@app.get("/chat")
def get_answer(query: str = Query(..., description="User legal question")):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, X)
    best_idx = scores.argmax()

    best_sentence, source = sentences[best_idx]
    return {
        "query": query,
        "best_match": best_sentence,
        "source": source
    }

# For running locally
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, reload=True)
    