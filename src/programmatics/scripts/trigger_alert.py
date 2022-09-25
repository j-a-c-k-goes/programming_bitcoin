# imports
import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

# define a message
msg = """ reply if you can see this. """
subject = "test based trials go viral"

# environment variables
print("making environment variables available")
load_dotenv()

# function to send email
def trigger_email(msg, subject):
	email_password = os.getenv('EMAIL_PW')
	email_user = os.getenv('EMAIL_USER')
	email_to = ["jack@flnpb.com", "flnbp@icloud.com", "jlester@student.gptc.edu", "jlester8@student.gsu.edu"]
	__msg =  EmailMessage()
	__msg.set_content(msg)
	__msg['Subject'] = "test based trials go viral"
	__msg['From'] = email_user
	__msg['To'] = email_to
	smtp_server = os.getenv('SMTP_SERVER')
	smtp_port = os.getenv('SMTP_PORT')
	smtp_encryption_method = "STARTTLS"

	# login to the email server
	server = smtplib.SMTP(smtp_server, smtp_port)
	print(smtp_encryption_method)
	server.starttls()
	print("logging into server")
	server.login(email_user, email_password)

	# send email
	for recipient in email_to:
		print("sending email to:", recipient )
		server.send_message(__msg)
	print(f"messages sent to { len(email_to) } recipients. quitting server")
	server.quit()

if __name__ == "__main__":
	send_email = trigger_email(msg, subject)
