import random
from time import sleep

import pyautogui
import pyperclip

from .automation_utils import paste_text, select_all, wait_for_imgur_url
from .browser_utils import (
    close_tab,
    get_current_url_and_domain,
    open_last_closed_tab,
    open_url,
)
from .file_utils import get_image_path


def create_brave_report_content(site_url: str, image_url: str) -> str:
    """Creates the content for a new topic on the Brave Community forum."""
    return f"""
**Description of the issue:** advertising

**Exact URL of the website in question:** `{site_url}`

**Screenshot of the ad as it appears in Brave** {image_url}

**Did the issue present with [default Shields settings](https://support.brave.com/hc/en-us/articles/360023646212-How-do-I-configure-global-and-site-specific-Shields-settings-)? (yes/no)** yes

**Does the site function as expected when Shields are turned off?** yes

**Is there a specific Shields configuration that causes the site to break? If so, tell us that configuration. (yes/no):** yes

**Does the site work as expected when using Chrome?** yes
"""


def report_ad_on_brave_community() -> None:
    """Automates the process of reporting an ad on the Brave Community forum."""
    site_url, site_domain = get_current_url_and_domain()
    close_tab()

    url = "https://community.brave.com/c/support-and-troubleshooting/ad-blocking/78"
    open_url(url)
    sleep(3)

    new_topic_button_path = get_image_path(
        "assets/brave_new_topic_button.png", "https://i.imgur.com/NioS1tY.png"
    )
    if not new_topic_button_path:
        return

    while True:
        try:
            new_topic_button = pyautogui.locateCenterOnScreen(
                new_topic_button_path, confidence=0.8
            )
            if new_topic_button:
                pyautogui.click(new_topic_button)
                break
        except pyautogui.PyAutoGUIException:
            print("Could not find the 'New Topic' button.")
        sleep(1)

    sleep(1)
    image_url = wait_for_imgur_url()

    pyperclip.copy(f"ad on {site_domain} {random.randint(1, 100000)}")
    paste_text()

    content = create_brave_report_content(site_url, image_url)
    pyperclip.copy(content)
    pyautogui.click(200, 800)  # Click on the text area
    select_all()
    paste_text()
    sleep(0.1)

    create_topic_button_path = get_image_path(
        "assets/brave_create_topic_button.png", "https://i.imgur.com/RCGyZgT.png"
    )
    if not create_topic_button_path:
        return

    try:
        create_topic_button = pyautogui.locateCenterOnScreen(
            create_topic_button_path, confidence=0.8
        )
        if create_topic_button:
            pyautogui.click(create_topic_button)
    except pyautogui.PyAutoGUIException:
        print("Could not find the 'Create Topic' button.")

    open_last_closed_tab()
    close_tab()
