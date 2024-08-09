import requests

class APIClient:
    BASE_URL = 'https://api.countrylayer.com/v2'
    
    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}?access_key={self.api_key}"
        response = requests.get(url)
        return response

    def post(self, endpoint, data):
        url = f"{self.BASE_URL}/{endpoint}?access_key={self.api_key}"
        response = requests.post(url, json=data)
        return response