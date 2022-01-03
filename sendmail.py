import smtplib
import mimetypes
from email.message import EmailMessage
import config

def send_message():
    message = EmailMessage()
    config.x
    config.y
    message['From'] = config.x
    message['To'] = config.y
    message['Subject'] = 'log.0x6C'
    body = "Hello!"
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type('something.pdf')
    mime_type, mime_subtype = mime_type.split('/')
    with open('log.txt', 'rb') as file:
        message.add_attachment(file.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename='log.txt')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(0) # for developers = 1
    mail_server.login(config.z, config.c)
    mail_server.send_message(message)
    mail_server.quit()
x = send_message()
print(x)