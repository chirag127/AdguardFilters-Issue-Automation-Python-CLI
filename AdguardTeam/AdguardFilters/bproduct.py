
# Physical: {X=307,Y=886};
# Physical: {X=302,Y=933};

# What product do you use?
# AdGuard version
from time import sleep
import pyautogui

from AdguardTeam.AdguardFilters.ebrowser_device import select_browser

# Physical: {X=349,Y=856};
# Physical: {X=365,Y=907};

# define a function to click the selections button

click_product_selection_x = 320
click_product_selection_y_normal = 886
click_product_selection_y_nsfw = 856 

def fill_product_normal():

    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_normal)

    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_normal + 47)  

    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_normal ) 


def fill_product_nsfw():

    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_nsfw)

    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_nsfw + 47)  

    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_nsfw )
