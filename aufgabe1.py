"""
Inwiefern kann dieses Skript angewendet werden?
- Wenn man Drittanbietern nicht traut und einen eigenen E-Mail-Client haben möchte
- Wenn man seine E-Mails durch ein Script generieren will, z.B: täglichen Kalender in eine am morgen versendete E-Mail druckt

Inwiefern könnte das Passwort besser geschützt werden?
- Passwort verschlüsseln

Haben Sie noch weitere Ansätze, Ihr Skript zu verbessern?
- Absender verschlüsseln (wenn in betrieblichem Umfeld)
"""



""" Imports """
import email, smtplib,ssl
from pathlib import Path
from email.message import EmailMessage
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

""" Attributes """
sender_email = "sender@domain.com"
sender_password = None
body = "Do you like the picture in the attachment?"
subject = f"Python-Email | from {sender_email}"
receiver_email = "receiver@domain.com"

#Create PW-File
data_folder = Path("D:/Programme/Microsoft Visual Studio Code/Projects/Python/- DHBW/Semester 1/2020.11.20-Email-Client-Aufgaben")
file_to_open = data_folder / "password.txt"
file = open(file_to_open, "w")

#input password
input_pw = input("Enter password: ")
file.write(input_pw)
file.close()

#read password from file
sender_password = open(file_to_open, "r").read()





# Attachment - Picture
picture_folder = Path("E:/Bilder/Cars/Toyota/Supra/MK4 - A80")
filename = picture_folder / "Screenshot_20191124-161132.jpg"





""" Message """
message = MIMEMultipart()
message["From"]= sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain")) # Add body to email



""" Copy & Paste """
# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

""" Copy & Paste """


# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()







""" Mailserver """
mailserver = smtplib.SMTP("smtp.strato.de",587)
mailserver.ehlo()
mailserver.starttls()
mailserver.login(sender_email, sender_password)
mailserver.sendmail(sender_email,receiver_email, str(text))
mailserver.quit()