import smtplib, ssl


port = 465
smtp_server = "smtp.gmail.com"
sender_email = input("Enter the senders email addreess: ")
reciever_email = input("Enter the receivers email address: ")
password = input("Enter the senders email address password: ")
message = """\
Subject : Python plain e-mail attachment

amkaa mzee
"""


context = ssl.create_default_context()
with smtplib.SSL(smtp_server, port)as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message )
    server.quit()