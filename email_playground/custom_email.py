import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = "Shashikamal R C"
email['to'] = "shashikamal54@gmail.com"
email['subject'] = "You won 1,00,00,000 rupees!"

email.set_content(html.substitute({"name" : "TinTin"}), 'html')

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # security protocal
    smtp.login("shashikamalrc567@gmail.com", "Sha$hikamal.rc06")
    smtp.send_message(email)
    print("Message sent boss!")