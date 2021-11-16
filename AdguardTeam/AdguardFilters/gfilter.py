# Physical: {X=317,Y=792}
# Physical: {X=293,Y=845}

# Physical: {X=316,Y=792}
# Physical: {X=306,Y=845}

import pyautogui
from time import sleep


def click_filter_selection_button():
    pyautogui.click(x=300, y=792)


def click_adgurad_filter_box():
    pyautogui.click(x=308, y=845)


def fill_filter():
    click_filter_selection_button()
    sleep(0.01)
    click_adgurad_filter_box()
    sleep(0.01)
    click_filter_selection_button()
    sleep(0.01)
