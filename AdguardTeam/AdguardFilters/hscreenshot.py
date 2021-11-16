# Physical: {X=393,Y=500}
# Physical: {X=362,Y=635}

import pyautogui
from time import sleep


# define the fuction to click screenshot body
def screenshot_body():
    pyautogui.click(393, 500)


def fill_screenshot():

    screenshot_body()

    pyautogui.hotkey('ctrl', 'a')

    pyautogui.typewrite("""<details><summary>Screenshot :</summary>


</details>""")

    pyautogui.click(362, 635)

    pyautogui.hotkey('win', 'num2')


    sleep(0.5)

    

