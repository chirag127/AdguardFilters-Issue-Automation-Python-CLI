from email.mime import image
import os
import sys
import webbrowser
from time import sleep
from urllib.parse import urlparse
import pyautogui
import pyperclip
import requests


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


def return_url_and_domain():
    copy_url_from_url_bar()

    # get the url of the website by using the clipboard
    site_url = pyperclip.paste()

    # parse the url to get the domain name
    site_domain = extract_domain(site_url)
    return site_url, site_domain


def copy_url_from_url_bar():
    # selecte the url of the current webpage
    pyautogui.hotkey("alt", "d")

    # copy the selected url to the clipboard
    pyautogui.hotkey("ctrl", "c")


def take_sharex_ss():

    # wait sometime before I  keyup the shortcut keys
    sleep(1)

    pyautogui.hotkey("ctrl", "prtsc")

    sleep(0.1)

    pyautogui.click()


def check_if_image_uploaded():
    while True:
        image_url = pyperclip.paste()

        if "imgur" in image_url:
            break
        print("waiting for the image to be uploaded")

        sleep(1)


def check_if_image_uploaded_and_return_url():

    check_if_image_uploaded()

    return pyperclip.paste()


# define a function that will open the last closed tab
# open last closed tab
def open_last_closed_tab():

    pyautogui.hotkey("ctrl", "shift", "t")

    print("Opened last closed tab")


# define a function that will close tab
def close_tab():

    pyautogui.hotkey("ctrl", "w")

    print("Closed tab")


# define a function that will go to next tab using pyautogui.hotkey('ctrl', 'tab')


def go_to_next_tab():

    pyautogui.hotkey("ctrl", "tab")

    print("Moved to next tab")


# define a function that will copy the url from the url bar using the pyautogui library by pressing the "ctrl" key + "c"
def copyselectedtext():

    pyautogui.hotkey("ctrl", "c")

    print("Copied text")


# define a function that will move down one page
def move_down_one_page():

    pyautogui.hotkey("pagedown")

    print("Moved down one page")


def paste_text():

    pyautogui.hotkey("ctrl", "v")

    print("Pasted text")


def ss_url_domain_closetab():
    take_sharex_ss()

    site_url, site_domain = return_url_and_domain()

    close_tab()
    return site_url, site_domain


def press_end():

    pyautogui.press("end")

    print("Pressed end")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def press_enter():

    pyautogui.press("enter")

    print("enter pressed")


def open_url_in_edge(issue_url):
    webbrowser.register(
        "edge",
        None,
        webbrowser.BackgroundBrowser(
            "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        ),
    )

    webbrowser.get("edge").open(issue_url)


def select_all():
    pyautogui.hotkey("ctrl", "a")

    print("Selected all")


def open_last_closed_tab_and_close_tab():
    open_last_closed_tab()
    close_tab()


def return_image_path(path, url):

    if not bool(os.path.exists(path)):
        print("No image found")

        response = requests.get(url)

        with open(path, "wb") as f:
            f.write(response.content)

    else:
        print("Image found")

    return path
