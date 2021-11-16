from time import sleep
import pyautogui

# Physical: {X=314,Y=214}


def click_selection_button():
    pyautogui.click(x=314, y=214)


# define a function to fill the version of the product
def fill_product_version():

    click_selection_button()

    sleep(0.01)

    pyautogui.typewrite('3.6.14')
