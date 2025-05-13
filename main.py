import requests
from send_email import send_email

api_key = "f5ce3e24f5db42e69b8e411e784e675a"
url = (
    "https://newsapi.org/v2/everything?"
    "q=tesla&"
    "from=2025-04-12&"
    "sortBy=publishedAt&"
    f"apiKey={api_key}&"
    "language=en"
)

response = requests.get(url)
content = response.json()

body = ""

for article in content["articles"][:20]:
    if article["title"]:
        body += f"Title: {article['title']}\n"
        body += f"Description: {article.get('description', 'No description')}\n"
        body += f"URL: {article['url']}\n\n"

# Use subject as a separate argument
send_email(subject="Today's News", message_body=body)

