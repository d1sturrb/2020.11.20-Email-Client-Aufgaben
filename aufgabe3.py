"""
Das Passwort soll nun in einer externen Datei stehen, aus es eingelesen wird.
"""

import smtplib, ssl

smtp_server = "SMTP.office365.com"
port = 587  # For starttls
sender_email = "peter123peteristsosuess@hotmail.com"
password = "AMfkxcE48KGV7vd"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 