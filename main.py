import requests
from send_email import send_email

api_key = "f5ce3e24f5db42e69b8e411e784e675a"
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-04-12&sortBy=publishedAt&apiKey=f5ce3e24f5db42e69b8e411e784e675a"

request = requests.get(url)   #Make Request
content = request.json()      #get a dictionary with data

body = ""

for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message = body)

