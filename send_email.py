import smtplib, ssl
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465

    username = 'stevenmtikas@gmail.com'
    password = 'wjkf yyha zgyi tkvt'
    password1 = os.getenv('PASSWORD1')
    print(password1)

    receiver = 'stevenmtikas@gmail.com'
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)