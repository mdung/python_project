import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the MIME
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server (for Gmail, use 'smtp.gmail.com')
    smtp_server = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
    smtp_port = 587  # Replace with the appropriate port for your email provider
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Log in to your email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())

    # Disconnect from the server
    server.quit()

# Example usage
sender_email = 'nguyen.manhdung33@gmail.com'
sender_password = 'your_email_password'
recipient_email = 'nguyen.manhdung33@gmail.com'
subject = 'Test Email'
message = 'This is a test email sent using Python.'

send_email(sender_email, sender_password, recipient_email, subject, message)
