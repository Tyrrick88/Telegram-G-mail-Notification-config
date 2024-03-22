import smtplib, ssl

port = 465
password = input("Please Enter your Gmail password: ")

# Create a context 

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
    server.login = ("Your Email address", password)
