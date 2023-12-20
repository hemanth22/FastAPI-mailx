from fastapi import FastAPI
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = FastAPI()

@app.post("/send_email")
def send_email(receiver_email: str, subject: str, bodyhtml: str):
    API_KEY_HELPER = os.environ.get('API_KEY_HELPER')
    SMTP_URL_FINAL = os.environ.get('SMTP_URL_FINAL')
    SMTP_PORT = os.environ.get('SMTP_PORT')

    sender_email = "hemanthbitraece@gmail.com"
    #receiver_email = "hemanthbitra@live.com"
    message = MIMEMultipart("alternative")

    #message["Subject"] = "[LV] Report"
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = ",".join(receiver_email)

    text = bodyhtml
    html = bodyhtml

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP(SMTP_URL_FINAL, SMTP_PORT) as server:
        server.starttls()
        server.login(sender_email, API_KEY_HELPER)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
        server.quit()
        print("Connection Closed")
    return {"message": "Email sent successfully."}
