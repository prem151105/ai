# vector_db.py

import faiss
import numpy as np

class VectorDB:
    def __init__(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.articles = []

    def add_article(self, title, embedding):
        self.index.add(np.array([embedding]))
        self.articles.append(title)

    def search(self, query_embedding, top_k=5):
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        results = [(self.articles[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
        return results
