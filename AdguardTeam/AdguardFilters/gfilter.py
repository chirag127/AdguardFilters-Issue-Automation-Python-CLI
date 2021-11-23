# Physical: {X=317,Y=792}
# Physical: {X=293,Y=845}

# Physical: {X=316,Y=792}
# Physical: {X=306,Y=845}

import pyautogui
from time import sleep


# Physical: {X=408,Y=881}
# Physical: {X=409,Y=892}

def click_filter_selection_button():

    pyautogui.click(x=300, y=792)


def click_adgurad_filter_box():

    pyautogui.click(x=308, y=845)


# define to click the Adguard Base filter box
def click_Adguard_Base_filter_box():

    pyautogui.click(x=308, y=880)

# define to click the Adguard social filter box


def click_Adguard_social_filter_box():

    pyautogui.click(x=308, y=850)

# define to click the Adguard Annoyance filter box


def click_Adguard_Annoyance_filter_box():

    pyautogui.click(x=308, y=900)


def fill_filter():

    click_filter_selection_button()

    sleep(0.01)

    click_adgurad_filter_box()

    click_Adguard_Base_filter_box()

    # press page down

    pyautogui.press('pagedown')

    sleep(0.01)

    click_Adguard_social_filter_box()

    sleep(0.01)

    click_Adguard_Annoyance_filter_box()

    sleep(0.01)

    click_filter_selection_button()

    sleep(0.1)
