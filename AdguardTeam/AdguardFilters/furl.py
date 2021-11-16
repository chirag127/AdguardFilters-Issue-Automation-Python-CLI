import pyautogui
import keyboard
from time import sleep

# Physical: {X=308,Y=675}

# Physical: {X=302,Y=671}

def click_url_box():

    pyautogui.moveTo(x=316, y=671,duration=0.1)

    pyautogui.click()

    sleep(0.5)



if __name__ == '__main__':

    while True:

        if keyboard.is_pressed('ctrl+shift+u'):

            click_url_box()

            sleep(1)

    


    