import smtplib
import ssl
import json

port = 465


def send_email(message):
    with open('emailcreds.json') as f:
        data = json.load(f)
        email = data['email']
        password = data['password']

    sender_email = email
    message = message

    receiver_email = email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login(email, password)

        server.sendmail(sender_email, receiver_email, message)
