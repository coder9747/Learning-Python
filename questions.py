from email.message import EmailMessage
import smtplib
import ssl

email_sender = "dailyshorts5299@gmail.com"
email_password = "hsnpfbhgktjurtnb"
email_reciver = "pratyushkarn007@gmail.com"
email_body = "This is test body "
email_subject = "This is Test Subject"
em = EmailMessage();
em['from'] = email_sender
em['to'] = email_reciver
em['subject'] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    for i in range(50):
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciver,em.as_string())
