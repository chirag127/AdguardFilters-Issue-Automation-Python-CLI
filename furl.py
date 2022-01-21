import pyautogui
import keyboard
from urllib.parse import urlparse


def click_url_box():

    pyautogui.click(x=400, y=600)


def extract_domain(url):
    """
    extract domain from url.
    """
    domain = urlparse(url).netloc

    if domain.startswith("www."):

        domain = domain[4:]

    elif domain.startswith("m."):

        domain = domain[2:]

    elif domain.startswith("mobile."):

        domain = domain[7:]

    return domain
