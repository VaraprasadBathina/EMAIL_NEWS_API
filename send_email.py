import smtplib
import ssl
import os
from email.message import EmailMessage

def send_email(subject, message_body):
    host = "smtp.gmail.com"
    port = 465

    username = "vidhyalakshmivaraprasadbathina@gmail.com"
    password = os.getenv("PROTIFOLIO_PASSWORD")
    receiver = "vidhyalakshmivaraprasadbathina@gmail.com"

    # Construct the email using EmailMessage
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = username
    msg["To"] = receiver
    msg.set_content(message_body)

    # Secure connection and send
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)
