import webbrowser
from time import sleep

import pyautogui
import pyperclip

from f import *

# define a function that will click the next button if  the image in the file named "AdguardFilters\images\adguard_next.png" is present on the screen


def if_next_button_is_present():
    i = 0
    while i < 20:
        path = return_image_path(
            "AdGuard_Reporter_next_button.png", "https://i.imgur.com/90UaP5H.png"
        )

        if (
            pyautogui.locateOnScreen(path, region=(850, 500, 300, 500), confidence=0.8)
            is None
        ):
            print("next button is not present")
            sleep(1)
            i += 1

        else:
            print("next button is present")
            break
    press_enter()


def open_create_issue_page(url, is_chrome):
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

    # issue_url = f"https://reports.adguard.com/en/new_issue.html?product_type=Win&product_version=7.11&url={url}&referrer=&user_agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F97.0.4692.71%20Safari%2F537.36&filters=101.118.122.123.227.11.14.16.17.1.224.2.3.4.5.6.7.9&userscripts=https%3A%2F%2Fkill.org%2Fbeta%2Fadguard-extra%2F1.0%2Fadguard-extra.user.js%2Chttps%3A%2F%2Fuserscripts.adtidy.org%2Fbeta%2Fpopup-blocker%2F2.5%2Fpopupblocker.user.js&win.wfp=true&stealth.enabled=true&stealth.hide_search_queries=true&stealth.DNT=true&stealth.x_client=true&stealth.third_party_cookies=180&stealth.disable_third_party_cache=false&stealth.webrtc=false&stealth.push=false&stealth.location=false&stealth.disable_windows_telemetry=true&stealth.turn_off_advertising_id=true&stealth.disable_windows_defender=false&stealth.disable_wap_push_message_routing_service=false&stealth.flash=false&stealth.java=false&stealth.strip_url=true&stealth.block_third_party_auth=false&dns.enabled=true&dns.timeout=5000&dns.fallback_mode=System&dns.custom_fallback=&dns.servers=https%3A%2F%2Fdns.adguard.com%2Fdns-query&dns.filters_enabled=true&dns.filters=https%3A%2F%2Ffilters.adtidy.org%2Fwindows%2Ffilters%2F15.txt%2CUser%20rules&parental_control.enabled=true&parental_control.sensitivity=EarlyChildhood&parental_control.safe_search=true&parental_control.block_exe=false&browsing_security.enabled=true&browsing_security.statistics_enabled=false"

    issue_url = f"https://reports.adguard.com/en/new_issue.html?browser=Other&browser_detail=EdgeChromium&browsing_security.enabled=false&filters=1003.1004.1001.1002.1000.14.17.2.3.4.11&product_type=Ext&product_version=4.1.53&stealth.DNT=true&stealth.enabled=true&stealth.hide_search_queries=true&stealth.strip_url=true&url={url}"

    if is_chrome:
        webbrowser.open(issue_url)

    else:
        open_url_in_edge(issue_url)

    sleep(3)


def fill_product():
    if_next_button_is_present()


def fill_Problem(isad):
    # Physical: {X=546,Y=476}; Scaled: {X=436,Y=380}; Relative: {X=-952,Y=-155}; Dpi: 120; Raw Dpi: 141; Dpi Ratio: 0.85; Screen Resolution: {Width=1920, Height=1080}; Pixel Color: #FFFFFF
    # Physical: {X=585,Y=521}; Scaled: {X=468,Y=416}; Relative: {X=585,Y=521}; Dpi: 120; Raw Dpi: 141; Dpi Ratio: 0.85; Screen Resolution: {Width=1920, Height=1080}; Pixel Color: #EBF5FF
    # Physical: {X=511,Y=661}; Scaled: {X=408,Y=528}; Relative: {X=511,Y=661}; Dpi: 120; Raw Dpi: 141; Dpi Ratio: 0.85; Screen Resolution: {Width=1920, Height=1080}; Pixel Color: #DFDFDF
    # Physical: {X=514,Y=746}; Scaled: {X=411,Y=596}; Relative: {X=514,Y=746}; Dpi: 120; Raw Dpi: 141; Dpi Ratio: 0.85; Screen Resolution: {Width=1920, Height=1080}; Pixel Color: #DFDFDF

    pyautogui.click(x=546, y=476, clicks=1, interval=0.0, button="left")
    if isad:
        pyautogui.click(x=585, y=521, clicks=1, interval=0.0, button="left")

    else:
        pyautogui.click(x=800, y=650)

    pyautogui.click(x=511, y=661, clicks=1, interval=0.0, button="left")

    pyautogui.click(x=514, y=746, clicks=1, interval=0.0, button="left")

    if_next_button_is_present()


def fill_url():
    sleep(0.5)

    pyautogui.click(x=498, y=574, clicks=1, interval=0.0, button="left")

    if_next_button_is_present()


def fill_filter():
    press_enter()


def fill_screenshot():
    pyautogui.click(x=848, y=720)

    pyautogui.hotkey("ctrl", "v")

    pyautogui.click(200, 200)

    sleep(3)

    press_end()

    if_next_button_is_present()


def fill_comment():
    pyautogui.press("home")

    sleep(0.1)

    # Physical: {X=607,Y=589}

    pyautogui.click(x=607, y=589, clicks=1, interval=0.0, button="left")

    sleep(0.1)

    text = """Hello, I am using Adguard for Windows and I have found an annoyance/ad on this website.
Please fix it. Thank you.
can you please tell the user filter if this annoyance don't follow the rules of the filter list."""

    pyperclip.copy(text)

    pyautogui.hotkey("ctrl", "v")

    pyautogui.click(x=429, y=696, clicks=1, interval=0.0, button="left")

    sleep(0.1)

    pyautogui.click(x=457, y=804, clicks=1, interval=0.0, button="left")

    pyautogui.write("neer9")

    sleep(0.1)
    # Physical: {X=438,Y=851}

    pyautogui.click(x=438, y=851, clicks=1, interval=0.0, button="left")

    press_end()

    press_enter()


def fill_check():
    sleep(0.01)

    press_end()


def mi_by_ag_re(isad=True, is_chrome=True):
    # wait sometime before I  keyup the shortcut keys
    sleep(1)

    # take a screenshot and paste it to the clipboard
    image = pyautogui.screenshot(region=(0, 88, 1920, 932))

    from io import BytesIO

    import win32clipboard

    def send_to_clipboard(clip_type, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(clip_type, data)
        win32clipboard.CloseClipboard()

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    sleep(0.1)

    # select the url of the current webpage
    pyautogui.hotkey("alt", "d")

    copy_selected_text()

    # get the url of the website by using the clipboard
    site_url = pyperclip.paste()

    close_tab()

    open_create_issue_page(site_url, is_chrome)

    send_to_clipboard(win32clipboard.CF_DIB, data)

    fill_product()

    fill_Problem(isad)

    fill_url()

    fill_filter()

    fill_screenshot()

    fill_comment()

    fill_check()

    open_last_closed_tab()

    close_tab()


if __name__ == "__main__":
    print("Press ctrl + q to make new issue for annoyance on a Non-NSFW website")

    print("Press alt + q to make new issue for advertisement on Non-NSFW  website")

    print("Press alt + x to make new issue for a NSFW website")

    while True:
        import keyboard

        if keyboard.is_pressed("ctrl + q"):
            mi_by_ag_re()

        elif keyboard.is_pressed("alt + q"):
            mi_by_ag_re(True, True)

        else:
            sleep(0.1)
