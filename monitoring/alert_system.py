
def send_email_alert(signal, email_address):
    """
    Send an email alert for critical trading signals.
    
    Parameters:
    - signal: The trading signal for which an alert is to be sent
    - email_address: The email address to which the alert will be sent
    
    Returns:
    - None
    """
    # Validate input parameters
    if not isinstance(signal, str) or not signal:
        raise ValueError("Trading signal must be a non-empty string.")
    if not isinstance(email_address, str) or not email_address:
        raise ValueError("Email address must be a non-empty string.")
    
    # Prepare email subject and body
    subject = f'Trading Signal Alert: {signal}'
    body = f'A new trading signal has been generated: {signal}'
    
    # Send the email
    try:
        send_email(subject, body, email_address)
    except Exception as e:
        raise Exception(f"Failed to send email alert: {e}")
