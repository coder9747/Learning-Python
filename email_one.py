from email.message import EmailMessage
import ssl
import smtplib


email_sender = "dailyshorts5299@gmail.com"
email_password = "hsnpfbhgktjurtnb"

email_reciver = "mallickcyber@gmail.com"

email_subject = "This is for Testting purpose Gmail"

email_body = "Nothing"


em = EmailMessage();

em["from"] = email_sender
em["to"] = email_reciver
em['subject'] = email_subject
em.set_content(email_body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    for i in range(100):
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciver,em.as_string())