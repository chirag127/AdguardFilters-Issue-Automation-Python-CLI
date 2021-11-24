
# Physical: {X=307,Y=886};
# Physical: {X=302,Y=933};

# What product do you use?
# AdGuard version
from time import sleep
import pyautogui

# define a function to click the selections button


def click_product_selection():

    pyautogui.click(x=320, y=886)


# define a function to click the adguard browser extension
def click_adguard_browser_extension():

    pyautogui.click(x=320, y=933)

# define a function to fill the selection of the product


def fill_product():

    click_product_selection()

    click_adguard_browser_extension()

    click_product_selection()
