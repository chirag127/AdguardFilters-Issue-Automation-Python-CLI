import pyautogui
from bproduct import fill_product
from ebrowser_device import fill_browser_and_device
from furl import click_url_box
from gfilter import fill_filter
from time import sleep
from urllib.parse import urlparse
from azfunctions import *
import dproblem
import keyboard
import webbrowser
import pyperclip


def open_create_issue_page(Create_new_issue_template, Create_new_issue_Account, site_domain):

    if "NSFW" in Create_new_issue_template:

        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(
            "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))

        webbrowser.get('edge').open("https://github.com/" + Create_new_issue_Account +
                                    "/issues/new?template=" + Create_new_issue_template + "&title=" + site_domain)

    else:

        webbrowser.open("https://github.com/" + Create_new_issue_Account +
                        "/issues/new?template=" + Create_new_issue_template + "&title=" + site_domain)


def create_issue(Create_new_issue_template, Create_new_issue_Account):

    pyautogui.hotkey('ctrl', 'prtsc')

    sleep(0.1)

    pyautogui.moveTo(x=500, y=500)

    sleep(0.1)

    pyautogui.click()

    # wait sometime before I  keyup the shortcut keys
    sleep(1)

    # selecte the url of the current webpage
    pyautogui.hotkey('alt', 'd')

    # copy the selected url to the clipboard
    pyautogui.hotkey('ctrl', 'c')

    # get the url of the website by using the clipboard
    site_url = pyperclip.paste()

    # parse the url to get the domain name
    site_domain = urlparse(site_url).netloc

    close_tab()

    open_create_issue_page(Create_new_issue_template,
                           Create_new_issue_Account, site_domain)

    sleep(3)

    fill_product(Create_new_issue_template)

    dproblem.fill_problem_as_annoyance()

    fill_browser_and_device()

    click_url_box()

    while True:

        image_url = pyperclip.paste()

        if "imgur" not in image_url:

            sleep(1)

            print("waiting for the image to be uploaded")

        else:

            break

    pyperclip.copy(site_url)

    paste_text()

    sleep(0.1)

    fill_filter()

    move_down_one_page()

    # define the fuction to click screenshot body
    def screenshot_body():

        pyautogui.click(393, 500)

    screenshot_body()

    pyautogui.hotkey('ctrl', 'a')

    pyperclip.copy(f"""<details><summary>Screenshots:</summary>




[screenshot]({image_url})




</details><br/>""")

    paste_text()

    # take focus out of the screenshot body

    pyautogui.click(x=100, y=500)

    sleep(0.01)

    press_end()

    sleep(0.1)

    # click on submit new issue
    pyautogui.click(x=1240, y=745)

    sleep(0.01)

    print("done")

    open_last_closed_tab()

    sleep(0.1)

    close_tab()

    print("loop completed")


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
