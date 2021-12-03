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
from jsubmit import click_on_submit_new_issue

page_down = 816


# create issue on the
#  https://github.com/AdguardTeam/AdguardFilters/issues/new?assignees=&template=bug_report.yml
# https://github.com/chirag127/test/issues/new?assignees=&template=bug_report.yml

def main():

    sleep(1)

    pyautogui.hotkey('alt', 'd')

    copyselectedtext()

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc

    pyautogui.hotkey('ctrl', 'w')

    webbrowser.open(
        f"https://github.com/AdguardTeam/AdguardFilters/issues/new?assignees=&template=bug_report.yml&title={domain}")

    sleep(3)

    fill_product()

    move_down_one_page()

    dproblem.fill_problem_as_annoyance()

    fill_browser_and_device()

    click_url_box()

    pyautogui.hotkey('ctrl', 'v')

    sleep(0.1)

    fill_filter()

    move_down_one_page()

    sleep(0.01)

    fill_screenshot()

    pyautogui.click(x=100, y=500)

    sleep(0.01)

    pyautogui.press('end')

    # click_privacy()

    open_last_closed_tab()

    close_tab()


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):
            main()

        else:
            sleep(0.1)
