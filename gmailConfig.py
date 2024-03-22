import smtplib

#  Gmail account details to send the email from.
sender_email = 'your-gmail@gmail.com'
server = smtplib.SMTP('smtp.gmail.com')
server.starttls()
server.login("<EMAIL>", "<PASSWORD>")

server.sendmail("<EMAIL>", "<EMAIL>")
server.quit()