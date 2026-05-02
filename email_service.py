 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "qrcodeprojectphishing@gmail.com"
SENDER_PASSWORD = "ztfmybzuqrdycykr"
ADMIN_EMAIL = "qrcodeprojectphishing@gmail.com"

def send_email_notification(to_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to: {to_email}")
        return True
    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")
        return False

def notify_admin(event_type, user_email, user_name):
    subject = f"👑 Admin Alert: User {event_type}"
    message = f"""
🔔 User Activity Alert

Event: {event_type}
User Email: {user_email}
User Name: {user_name}
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

This is an automated notification from AI QR Shield.
    """
    send_email_notification(ADMIN_EMAIL, subject, message)