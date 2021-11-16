import pyautogui
from time import sleep


# Physical: {X=316,Y=430}
# Physical: {X=322,Y=524}
# Physical: {X=320,Y=534}
# Physical: {X=311,Y=581}


def click_browser_selection_button():
    pyautogui.click(x=316, y=430)


def select_browser():
    pyautogui.click(x=322, y=524)


def click_device_selection_button():
    pyautogui.click(x=320, y=534)


def select_device():
    pyautogui.click(x=311, y=581)


def fill_browser_and_device():

    click_browser_selection_button()

    sleep(0.1)

    select_browser()

    sleep(0.1)

    click_browser_selection_button()

    sleep(0.1)

    click_device_selection_button()

    sleep(0.1)

    select_device()

    sleep(0.1)
