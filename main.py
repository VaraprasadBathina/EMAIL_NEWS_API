import requests

api_key = "f5ce3e24f5db42e69b8e411e784e675a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-04-12&sortBy=publishedAt&apiKey=f5ce3e24f5db42e69b8e411e784e675a"

request = requests.get(url)
content = request.text
print(content)