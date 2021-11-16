from zfunctions import *
from aprerequisites import click_on_all_prerequisites_checkboxes
from bproduct import fill_product
from cversion import fill_product_version
import dproblem
from ebrowser_device import fill_browser_and_device
from furl import click_url_box
from gfilter import fill_filter
from hscreenshot import fill_screenshot
from iprivacy import click_privacy

page_down = 816


# create issue on the
#  https://github.com/AdguardTeam/AdguardFilters/issues/new?assignees=&template=bug_report.yml

def main():

    sleep(1)

    pyautogui.hotkey('alt', 'd')

    copyselectedtext()

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc

    pyautogui.hotkey('ctrl', 'w')

    webbrowser.open("https://github.com/AdguardTeam/AdguardFilters/issues/new?assignees=&template=bug_report.yml")

    sleep(3)

    pyautogui.typewrite(domain)

    click_on_all_prerequisites_checkboxes()
    

    fill_product()

    move_down_one_page()


    fill_product_version()


    dproblem.fill_problem_as_annoyance()

    fill_browser_and_device()

    click_url_box()

    pyautogui.typewrite(f"`{url}`")

    fill_filter()

    move_down_one_page()

    sleep(0.5)

    fill_screenshot()

    click_privacy()

    sleep(0.1)

    pyautogui.press('end')

    open_last_closed_tab()

    close_tab()


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):
            main()

        else:
            sleep(0.1)
