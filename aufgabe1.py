import smtplib,ssl
from email.message import EmailMessage

""" Attributes """
sender_email = "testmail@dreampeak.de"
sender_password = "qg9xfKeuue5jIlDXbe5V"
receiver_email = "d1sturrb@outlook.com"

message = """\
Subject: Hi there

This message is sent from Python."""

mailserver = smtplib.SMTP("smtp.strato.de",587)
mailserver.ehlo()
mailserver.starttls()
mailserver.login(sender_email, sender_password)
mailserver.sendmail(sender_email,receiver_email, str(message))
mailserver.quit()

#context = ssl.create_default_context()


""" Message 
print("Message")

message = EmailMessage()
message.set_content("Wohooooo")
message["To"] = receiver_email
message["From"] = sender_email
message["Subject"] = f"The contents of this {sender_email}-Email"
"""