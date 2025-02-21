# retriever.py

import requests
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

class NewsRetriever:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def fetch_article(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('h1').get_text()
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text() for p in paragraphs])
            return title, content
        else:
            raise Exception(f"Failed to fetch article: {response.status_code}")

    def embed_article(self, content):
        return self.model.encode(content, convert_to_tensor=True)
