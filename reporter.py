
import webbrowser
from time import sleep

import pyautogui
import pyperclip

import os


def press_enter():

    pyautogui.press("enter")


# define a function that will click the next button if  the image in the file named "AdguardFilters\images\adguard_next.png" is present on the screen


def if_next_button_is_present():

    # Physical: {X=856,Y=660}
    # Physical: {X=1116,Y=606}
    # Physical: {X=921,Y=500}
    # Physical: {X=944,Y=1009}
    while True:
        try:
            adguard_next_button_png_path = "adguard_add_url.png"
            # adguard_next_button_png_path = os.path.join(os.path.dirname(__file__), adguard_next_button_png_path)

            if (
                pyautogui.locateOnScreen(adguard_next_button_png_path,
                                         region=(850, 500, 300, 500), confidence=0.8)) != None:
                print("next button is present")
                break
            else:
                print("next button is not present")
                sleep(1)
        except Exception as e:

            sleep(10)

    press_enter()


def click_add_url_button_if_it_is_present():

    # adguard_next.png
    while True:

        try:
            adguard_add_url_button_png_path = "adguard_add_url.png"

            # adguard_add_url_button_png_path = os.path.join(os.path.dirname(__file__), adguard_add_url_button_png_path)

            image_coords = pyautogui.locateOnScreen(adguard_add_url_button_png_path,
                                                    region=(1330, 680, 160, 80))
            image_coords = pyautogui.center(image_coords)
            pyautogui.click(image_coords)
            print("add url button is present")
            break
        except:
            print("add url button is not present")
            sleep_for_a_1_s()


def open_create_issue_page(url):
    url = url.replace(" ", "%20")
    url = url.replace("!", "%21")
    url = url.replace("#", "%23")
    url = url.replace("$", "%24")
    url = url.replace("%", "%25")
    url = url.replace("&", "%26")
    url = url.replace("*", "%2A")
    url = url.replace("+", "%2B")
    url = url.replace("-", "%2D")
    url = url.replace(".", "%2E")
    url = url.replace("/", "%2F")
    url = url.replace(":", "%3A")
    url = url.replace(";", "%3B")
    url = url.replace("<", "%3C")
    url = url.replace("=", "%3D")
    url = url.replace(">", "%3E")
    url = url.replace("?", "%3F")
    url = url.replace("@", "%40")
    url = url.replace("[", "%5B")
    url = url.replace('"', "%22")
    url = url.replace("\\", "%5C")
    url = url.replace("]", "%5D")
    url = url.replace("^", "%5E")
    url = url.replace("_", "%5F")
    url = url.replace("`", "%60")
    url = url.replace("{", "%7B")
    url = url.replace("|", "%7C")
    url = url.replace("}", "%7D")
    url = url.replace("~", "%7E")

    issue_url = f"https://reports.adguard.com/en/new_issue.html?product_type=Win&product_version=7.9%20nightly%204&url={url}&referrer=&user_agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F97.0.4692.71%20Safari%2F537.36&filters=101.118.122.123.227.11.14.16.17.1.224.2.3.4.5.6.7.9&userscripts=https%3A%2F%2Fkilll.org%2Fbeta%2Fadguard-extra%2F1.0%2Fadguard-extra.user.js%2Chttps%3A%2F%2Fuserscripts.adtidy.org%2Fbeta%2Fpopup-blocker%2F2.5%2Fpopupblocker.user.js&win.wfp=true&stealth.enabled=true&stealth.hide_search_queries=true&stealth.DNT=true&stealth.x_client=true&stealth.third_party_cookies=180&stealth.disable_third_party_cache=false&stealth.webrtc=false&stealth.push=false&stealth.location=false&stealth.disable_windows_telemetry=true&stealth.turn_off_advertising_id=true&stealth.disable_windows_defender=false&stealth.disable_wap_push_message_routing_service=false&stealth.flash=false&stealth.java=false&stealth.strip_url=true&stealth.block_third_party_auth=false&dns.enabled=true&dns.timeout=5000&dns.fallback_mode=System&dns.custom_fallback=&dns.servers=https%3A%2F%2Fdns.adguard.com%2Fdns-query&dns.filters_enabled=true&dns.filters=https%3A%2F%2Ffilters.adtidy.org%2Fwindows%2Ffilters%2F15.txt%2CUser%20rules&parental_control.enabled=true&parental_control.sensitivity=EarlyChildhood&parental_control.safe_search=true&parental_control.block_exe=false&browsing_security.enabled=true&browsing_security.statistics_enabled=false"
    webbrowser.open(issue_url)

    sleep(3)


def sleep_for_a_1_s():

    sleep(1)


def sleep_for_a_01_s():

    sleep(0.1)


def sleep_for_a_001_s():

    sleep(0.01)


def sleep_for_a_0001_s():

    sleep(0.001)


def fill_product():

    if_next_button_is_present()


def fill_Problem():

    pyautogui.click(x=738, y=440)

    sleep_for_a_001_s

    pyautogui.click(x=599, y=661)

    sleep_for_a_001_s

    pyautogui.click(x=523, y=619)

    sleep_for_a_001_s

    pyautogui.click(x=517, y=709)

    if_next_button_is_present()


def fill_url():

    if_next_button_is_present()


def fill_filter():

    sleep_for_a_01_s()

    press_enter()


def fill_screenshot():

    sleep_for_a_01_s()

    # Physical: {X=848,Y=720};
    # Physical: {X=1389,Y=702};
    pyautogui.click(x=848, y=720)

    sleep_for_a_01_s()

    pyautogui.hotkey("ctrl", "v")

    sleep(1)

    click_add_url_button_if_it_is_present()

    sleep(2)

    press_end()

    if_next_button_is_present()


def fill_comment():

    sleep(0.1)

    press_enter()


def fill_check():

    sleep(0.1)

    press_end()


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


def press_end():

    pyautogui.press("end")

    print("Pressed end")


def main():

    # wait sometime before I  keyup the shortcut keys
    sleep(1)

    pyautogui.hotkey("ctrl", "prtsc")

    sleep(0.1)

    pyautogui.moveTo(x=500, y=500)

    sleep(0.1)

    pyautogui.click()

    # select the url of the current webpage
    pyautogui.hotkey("alt", "d")

    copyselectedtext()

    # get the url of the website by using the clipboard
    site_url = pyperclip.paste()

    close_tab()

    open_create_issue_page(site_url)

    fill_product()

    fill_Problem()

    fill_url()

    fill_filter()

    while True:

        image_url = pyperclip.paste()

        if "imgur" not in image_url:

            print("waiting for the image to be uploaded")

            sleep(1)

        else:

            break

    sleep(0.1)

    fill_screenshot()

    fill_comment()

    fill_check()

    open_last_closed_tab()

    close_tab()


if __name__ == "__main__":

    print("Press ctrl + q to make new issue for a Non-NSFW website")

    print("Press alt + x to make new issue for a NSFW website")

    while True:

        import keyboard

        if keyboard.is_pressed("alt + q"):

            main()

        else:

            sleep(0.1)
