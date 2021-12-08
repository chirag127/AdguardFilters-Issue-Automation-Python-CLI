
# Physical: {X=307,Y=886};
# Physical: {X=302,Y=933};

# What product do you use?
# AdGuard version
from time import sleep
import pyautogui

# Physical: {X=349,Y=856};
# Physical: {X=365,Y=907};

# define a function to click the selections button

click_product_selection_x = 320
click_product_selection_y_normal = 886
click_product_selection_y_nsfw = 856


def click_fill_product_button_normal():

    pyautogui.click(x=click_product_selection_x,
                    y=click_product_selection_y_normal)


def click_fill_product_button_nsfw():

    pyautogui.click(x=click_product_selection_x,
                    y=click_product_selection_y_nsfw)


def fill_product(Create_new_issue_template):

    if Create_new_issue_template == "bug_report.yml":

        click_fill_product_button_normal()

        pyautogui.click(x=click_product_selection_x,
                        y=click_product_selection_y_normal + 47)

        click_fill_product_button_normal()

        pyautogui.press('pagedown')

    elif Create_new_issue_template == "bug_report_NSFW.yml":

        click_fill_product_button_nsfw()

        pyautogui.click(x=click_product_selection_x,
                        y=click_product_selection_y_nsfw + 47)

        click_fill_product_button_nsfw()

        pyautogui.press('pagedown')

        pyautogui.scroll(36)
