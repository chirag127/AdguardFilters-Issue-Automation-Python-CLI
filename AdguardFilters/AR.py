from bproduct import fill_product_normal
from ebrowser_device import fill_browser_and_device
from furl import click_url_box
from gfilter import fill_filter
from time import sleep
from urllib.parse import urlparse
from zfunctions import *
import dproblem
import keyboard
import webbrowser
import pyperclip

page_down = 816

Create_new_issue_template = "bug_report.yml"
# Create_new_issue_template = "bug_report_NSFW.yml"
# Create_new_issue_Account = "chirag127/test"
Create_new_issue_Account = "AdguardTeam/AdguardFilters"


def main():

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

    pyautogui.hotkey('ctrl', 'w')

    webbrowser.open("https://github.com/" + Create_new_issue_Account +
                    "/issues/new?template=" + Create_new_issue_template + "&title=" + site_domain)

    sleep(3)

    fill_product_normal()

    move_down_one_page()

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

    pyautogui.hotkey('ctrl', 'v')

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

    pyautogui.hotkey('ctrl', 'v')

    # take focus out of the screenshot body

    pyautogui.click(x=100, y=500)

    sleep(0.01)

    pyautogui.press('end')

    sleep(0.1)

    # click on submit new issue
    pyautogui.click(x=1240, y=745)

    sleep(0.01)

    print("done")

    open_last_closed_tab()

    sleep(0.1)

    pyautogui.hotkey('ctrl', 'w')

    print("loop completed")


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):
            main()

        else:
            sleep(0.1)
