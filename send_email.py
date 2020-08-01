import smtplib
import ssl
import json

port = 465

with open('emailcreds.json') as f:
    data = json.load(f)
    email = data['email']
    password = data['password']

sender_email = email

receiver_email = email
message = """\
Subject: Test Message

Hello World
"""
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login(email, password)

    server.sendmail(sender_email, receiver_email, message)
