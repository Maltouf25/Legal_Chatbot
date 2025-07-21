from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer
from .base_model import BaseModel

class Embedding_Model(BaseModel):
    
    def __init__(self):
        super().__init__()
        self.model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
        # Qdrant connection
        self.qdrant_client = QdrantClient(
            url="https://419699fc-3b6a-4452-9fab-01a2501c9a80.us-east-1-0.aws.cloud.qdrant.io:6333", 
            api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.JjEpBQGwuLo22XSMRsC9fTd48gftHzd7EYI-sci9TVA",
        )
        self.collection_name="legal_articles"


    def answer(self,user_query:str)->str :
        query_vector = self.model.encode(user_query).tolist()

        results = self.qdrant_client.query_points(
            collection_name = self.collection_name,
            query=query_vector,
            limit=1,
            with_payload=True
        )

        if results and results.points:
            best = results.points[0]
            return best.payload.get("text", "No content found.")
        else:
            return "No relevant article found."

    


    
