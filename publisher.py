# publisher.py

import requests

class BlogPublisher:
    def __init__(self, api_endpoint, api_key):
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def publish(self, title, content):
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}
        data = {'title': title, 'content': content}
        response = requests.post(self.api_endpoint, json=data, headers=headers)
        if response.status_code == 201:
            print("Article published successfully.")
        else:
            print(f"Failed to publish article: {response.status_code}")
