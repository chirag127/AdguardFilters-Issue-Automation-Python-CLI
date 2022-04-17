from f import *
import keyboard
import random


def main():

    site_url, site_domain = ss_url_domain_closetab()

    url = "https://community.brave.com/c/support-and-troubleshooting/ad-blocking/78"

    open_url_in_edge(url)

    sleep(3)

    while True:
        brave_new_topic_button = pyautogui.locateOnScreen('brave_new_topic_button.png', confidence=0.8)

        if brave_new_topic_button is not None:
            brave_new_topic_button = pyautogui.center(brave_new_topic_button)

            pyautogui.click(brave_new_topic_button)
            break

        else:

            sleep(1)

    sleep(1)

    check_if_image_uploaded()

    image_url = pyperclip.paste()

    pyperclip.copy(f"ad on {site_domain} {random.randint(1, 100000)}")

    paste_text()

    content = f"""
**Description of the issue:** advertising 

**Exact URL of the website in question:** `{site_url}`

**Screenshot of the ad as it appears in Brave** {image_url}

**Did the issue present with [default Shields settings](https://support.brave.com/hc/en-us/articles/360023646212-How-do-I-configure-global-and-site-specific-Shields-settings-)? (yes/no)** yes

**Does the site function as expected when Shields are turned off?** yes

**Is there a specific Shields configuration that causes the site to break? If so, tell us that configuration. (yes/no):** yes

**Does the site work as expected when using Chrome?** yes

"""

    pyautogui.click(200, 800)

    pyperclip.copy(content)

    select_all()

    paste_text()

    sleep(0.1)

    pyautogui.click(pyautogui.locateCenterOnScreen('create_topic.png', confidence=0.8))

    oandc()


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed("alt + q"):
            main()

        else:

            sleep(0.1)
