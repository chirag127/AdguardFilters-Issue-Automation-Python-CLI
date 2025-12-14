
import os
from dotenv import load_dotenv

load_dotenv()

def get_email_credentials() -> tuple[str, str, str]:
    """
    Retrieves email credentials from environment variables.
    """
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    if not all([sender_email, password, receiver_email]):
        raise ValueError("Missing one or more email environment variables (SENDER_EMAIL, EMAIL_PASSWORD, RECEIVER_EMAIL)")

    return sender_email, password, receiver_email
