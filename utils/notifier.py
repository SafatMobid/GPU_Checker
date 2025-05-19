import smtplib
from email.mime.text import MIMEText

def send_email_alert(alert_lines, email_settings):
    body = "\n".join(alert_lines)
    msg = MIMEText(body)
    msg["Subject"] = "GPU Monitor - Alert"
    msg["From"] = email_settings["sender"]
    msg["To"] = email_settings["recipient"]

    try:
        with smtplib.SMTP(email_settings["smtp_server"], email_settings["port"]) as server:
            server.starttls()
            server.login(email_settings["username"], email_settings["password"])
            server.send_message(msg)
            print("Alert email sent.")
    except Exception as e:
        print(f"Failed to send email: {e}")
