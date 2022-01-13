import pyautogui
from time import sleep
import webbrowser
from urllib.parse import urlparse


def press_enter():

    pyautogui.press('enter')


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
    url = url.replace("\"", "%22")
    url = url.replace("\\", "%5C")
    url = url.replace("]", "%5D")
    url = url.replace("^", "%5E")
    url = url.replace("_", "%5F")
    url = url.replace("`", "%60")
    url = url.replace("{", "%7B")
    url = url.replace("|", "%7C")
    url = url.replace("}", "%7D")
    url = url.replace("~", "%7E")

    issue_url = f"https://reports.adguard.com/en/new_issue.html?product_type=Win&product_version=7.9%20nightly%204&url={url}&referrer=&user_agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F97.0.4692.71%20Safari%2F537.36&filters=101.118.122.123.227.11.14.16.17.1.224.2.3.4.5.6.7.9&userscripts=https%3A%2F%2Fkillme.org%2Fbeta%2Fadguard-extra%2F1.0%2Fadguard-extra.user.js%2Chttps%3A%2F%2Fuserscripts.adtidy.org%2Fbeta%2Fpopup-blocker%2F2.5%2Fpopupblocker.user.js&win.wfp=true&stealth.enabled=true&stealth.hide_search_queries=true&stealth.DNT=true&stealth.x_client=true&stealth.third_party_cookies=180&stealth.disable_third_party_cache=false&stealth.webrtc=false&stealth.push=false&stealth.location=false&stealth.disable_windows_telemetry=true&stealth.turn_off_advertising_id=true&stealth.disable_windows_defender=false&stealth.disable_wap_push_message_routing_service=false&stealth.flash=false&stealth.java=false&stealth.strip_url=true&stealth.block_third_party_auth=false&dns.enabled=true&dns.timeout=5000&dns.fallback_mode=System&dns.custom_fallback=&dns.servers=https%3A%2F%2Fdns.adguard.com%2Fdns-query&dns.filters_enabled=true&dns.filters=https%3A%2F%2Ffilters.adtidy.org%2Fwindows%2Ffilters%2F15.txt%2CUser%20rules&parental_control.enabled=true&parental_control.sensitivity=EarlyChildhood&parental_control.safe_search=true&parental_control.block_exe=false&browsing_security.enabled=true&browsing_security.statistics_enabled=false"
    webbrowser.open(issue_url)

    sleep(6)


def fill_product():

    sleep(0.5)

    press_enter()


def fill_Problem():

    pyautogui.click(x=738, y=440)

    sleep(0.1)

    pyautogui.click(x=599, y=661)

    sleep(0.1)

    pyautogui.click(x=523, y=619)

    sleep(0.1)

    pyautogui.click(x=517, y=709)

    sleep(1)

    pyautogui.press('enter')


def fill_url():

    sleep(2.5)

    pyautogui.press('enter')


def fill_filter():

    sleep(0.5)

    pyautogui.press('enter')


def fill_screenshot():

    sleep(0.5)

    # Physical: {X=848,Y=720};
    # Physical: {X=1389,Y=702};
    pyautogui.click(x=848, y=720)

    sleep(0.1)

    pyautogui.hotkey('ctrl', 'v')

    sleep(2.5)

    pyautogui.click(x=1389, y=702)

    sleep(5)

    pyautogui.press('enter')


def fill_comment():

    sleep(0.5)

    pyautogui.press('enter')


def fill_check():

    sleep(0.5)

    press_end()


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


# define a function that will open the last closed tab
# open last closed tab
def open_last_closed_tab():

    pyautogui.hotkey('ctrl', 'shift', 't')


# define a function that will close tab
def close_tab():

    pyautogui.hotkey('ctrl', 'w')

# define a function that will go to next tab using pyautogui.hotkey('ctrl', 'tab')


def go_to_next_tab():

    pyautogui.hotkey('ctrl', 'tab')


# define a function that will copy the url from the url bar using the pyautogui library by pressing the "ctrl" key + "c"
def copyselectedtext():

    pyautogui.hotkey('ctrl', 'c')


# define a function that will move down one page
def move_down_one_page():

    pyautogui.hotkey('pagedown')


def paste_text():

    pyautogui.hotkey('ctrl', 'v')


def press_end():

    pyautogui.press('end')
