import pyautogui

# Physical: {X=314,Y=214}


def click_selection_button():

    pyautogui.click(x=314, y=214)


# define a function to fill the version of the product
def fill_product_version():

    click_selection_button()

    pyautogui.typewrite('3.6.14')
