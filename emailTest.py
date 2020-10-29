import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Email Stuff
smtp_server = "smtp.gmail.com"
sender_email = "michaelemailbot@gmail.com"  # Enter your address
receiver_email = "jfangonil@gmail.com"  # Enter receiver address
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
