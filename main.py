import smtplib
import socket

sender_email = "sender@gmail.com"
receiver_email = "reciver@gmail.com"
password = "password"

message = """

Hi This is a samble message

"""
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Email sent successfully")
except (socket.gaierror, ConnectionRefusedError):
    print("Failed to connect to the server")
except smtplib.SMTPException as error:
    print("Error: unable to send email:", error)
finally:
    server.quit()
