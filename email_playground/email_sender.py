import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "Shashikamal R C"
email['to'] = "shashikamal54@gmail.com"
email['subject'] = "You won 1,00,00,000 rupees!"

email.set_content("I am a python Master!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() # security protocal
    smtp.login("shashikamalrc567@gmail.com", "Sha$hikamal.rc06")
    smtp.send_message(email)
    print("Message sent boss!")