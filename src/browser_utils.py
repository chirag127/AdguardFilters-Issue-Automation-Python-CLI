import webbrowser
from time import sleep
from urllib.parse import urlparse

import pyautogui
import pyperclip


def open_url(url: str) -> None:
    """Opens a URL in the default web browser."""
    webbrowser.open(url)


def extract_domain(url: str) -> str:
    """Extracts the domain from a URL."""
    domain = urlparse(url).netloc
    if domain.startswith("www."):
        domain = domain[4:]
    elif domain.startswith("m."):
        domain = domain[2:]
    elif domain.startswith("mobile."):
        domain = domain[7:]
    return domain


def get_current_url_and_domain() -> tuple[str, str]:
    """Gets the current URL and domain from the browser's address bar."""
    pyautogui.hotkey("alt", "d")
    pyautogui.hotkey("ctrl", "c")
    sleep(0.1)  # Allow clipboard to update
    site_url = pyperclip.paste()
    site_domain = extract_domain(site_url)
    return site_url, site_domain


def open_last_closed_tab() -> None:
    """Opens the last closed tab in the browser."""
    pyautogui.hotkey("ctrl", "shift", "t")
    print("Opened last closed tab")


def close_tab() -> None:
    """Closes the current tab in the browser."""
    pyautogui.hotkey("ctrl", "w")
    print("Closed tab")


def go_to_next_tab() -> None:
    """Switches to the next tab in the browser."""
    pyautogui.hotkey("ctrl", "tab")
    print("Moved to next tab")


def open_url_in_edge(issue_url: str) -> None:
    """Opens a URL specifically in Microsoft Edge."""
    try:
        webbrowser.register(
            "edge",
            None,
            webbrowser.BackgroundBrowser(
                "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            ),
        )
        webbrowser.get("edge").open(issue_url)
    except webbrowser.Error:
        print("Could not open URL in Edge. Is it installed at the default location?")
