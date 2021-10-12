
# Import necessary libraries
import smtplib

def send_alert(email, subject, message):
    """
    Send an email alert for unusual activity or performance drops.
    """
    # Note: This is a simplified example. You'd use your actual email settings here.
    server = smtplib.SMTP('smtp.example.com', 587)
    server.login('your_email@example.com', 'your_password')
    server.sendmail('your_email@example.com', email, f'Subject: {subject}\n{message}')

# Simulate sending an alert
send_alert('recipient@example.com', 'Performance Alert', 'The accuracy has dropped below the threshold.')
