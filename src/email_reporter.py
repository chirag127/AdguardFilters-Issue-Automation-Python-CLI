
import smtplib
import ssl
from .browser_utils import get_current_url_and_domain, close_tab
from .automation_utils import wait_for_imgur_url
from .config import get_email_credentials

def send_secure_email(message: str) -> None:
    """Sends an email using a secure SSL connection."""
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email, password, receiver_email = get_email_credentials()
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Email sent successfully")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

def format_ad_report(site_url: str, site_domain: str, image_url: str) -> str:
    """Formats the ad report email."""
    subject = f"Report advertisement on {site_domain}"
    body = f"""Hi,

    Issue_url: {site_url}
    Issue : advertisement
    Screenshot:  {image_url}
    System configuration: https://user-images.githubusercontent.com/76880977/126797496-0434116b-fc94-42c9-8139-fba02a985cf2.png

    Please resolve the issue as soon as possible.

    Thanks,
    """
    return f"Subject: {subject}\n\n{body}"

def create_and_send_ad_report() -> None:
    """Gathers information, creates, and sends an ad report."""
    site_url, site_domain = get_current_url_and_domain()
    close_tab()
    image_url = wait_for_imgur_url()
    message = format_ad_report(site_url, site_domain, image_url)
    send_secure_email(message)
