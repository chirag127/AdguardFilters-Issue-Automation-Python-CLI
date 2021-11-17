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

    pyautogui.typewrite("""<details><summary>Screenshots:</summary>









</details><br/>

<details><summary>System configuration:</summary>

![image](https://user-images.githubusercontent.com/76880977/141497551-099fafbf-933f-44c7-956a-f88fc1bcb5d5.png)

</details><br/>""")

    pyautogui.click(362, 635)

    pyautogui.hotkey('win', 'num2')

    sleep(0.5)


if __name__ == '__main__':

    fill_screenshot()
