import requests

s = requests.Session()
response = s.get(url="https://jsonplaceholder.typicode.com/posts")
data = response.json()

