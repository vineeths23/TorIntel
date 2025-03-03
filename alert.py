import smtplib
from email.mime.text import MIMEText
from config import EMAIL_CONFIG

def send_alert(found_data):
    sender = EMAIL_CONFIG["sender email"]
    password = EMAIL_CONFIG["app pasword"]
    receiver = EMAIL_CONFIG["receiver email"]

    subject = "Dark Web Alert: Sensitive Data Found"
    body = f"Warning! We found the following data:\n\n{found_data}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("✅ Alert sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
