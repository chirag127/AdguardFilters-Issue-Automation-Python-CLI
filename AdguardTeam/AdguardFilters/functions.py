from time import sleep
from urllib.parse import urlparse
import clipboard
import keyboard
import pyautogui
import pyautogui
import webbrowser


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


# define a function that will click on all prerequisites checkboxes
def click_on_all_prerequisites_checkboxes():

    # click on the checkbox "This site DOES NOT contains sexually explicit material, otherwise use NSFW-specific form"
    pyautogui.click(x=289, y=651)

    # click on the checkbox "Filters were updated before reproduced an issue"
    pyautogui.click(x=289, y=689)

    # click on the checkbox "AdGuard product version is up-to-date"
    pyautogui.click(x=289, y=726)

    # click on the checkbox "Browser version is up-to-date"
    pyautogui.click(x=289, y=761)

    # click on the checkbox "If the site or app is broken, disabling AdGuard protection resolves an issue."
    pyautogui.click(x=289, y=800)


