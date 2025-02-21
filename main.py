# main.py

from retriever import NewsRetriever
from vector_db import VectorDB
from generator import SummaryGenerator
from optimizer import ContentOptimizer
from publisher import BlogPublisher
from config import API_ENDPOINT, API_KEY, TARGET_KEYWORDS

def main():
    retriever = NewsRetriever()
    vector_db = VectorDB(embedding_dim=384)  # Embedding dimension of 'all-MiniLM-L6-v2'
    generator = SummaryGenerator()
    optimizer = ContentOptimizer(target_keywords=TARGET_KEYWORDS)
    publisher = BlogPublisher(api_endpoint=API_ENDPOINT, api_key=API_KEY)

    # Example URL
    url = 'https://example.com/news_article'
    title, content = retriever.fetch_article(url)
    embedding = retriever.embed_article(content)
    vector_db.add_article(title, embedding)

    summary = generator.summarize(content)
    optimized_title, optimized_content = optimizer.optimize_content(title, summary)
    publisher.publish(optimized_title, optimized_content)

if __name__ == "__main__":
    main()
