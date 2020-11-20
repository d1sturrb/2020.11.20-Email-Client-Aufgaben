"""
Modifizieren sie die Passwortabfrage insofern, dass Sie im Skript das Passwort mittels einer Abfrage eingeben müssen.
"""

import smtplib
from email.message import EmailMessage


zugang = "https://mail.cock.li/"
email = "dasisteineemail@cock.li"
password = input("Bitte gib hier dein Password ein: ")
