import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'YOUR email'
email_password = "Type here 16 digit password (You need generate in Two-step verification menu on google account settings)"
email_receiver = 'email TO WHICH the mail will be sent'

subject = input('Type here email subject: ')
body = input('Type here email body: ')

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smpt:
    smpt.login(email_sender, email_password)
    smpt.sendmail(email_sender, email_receiver, em.as_string())