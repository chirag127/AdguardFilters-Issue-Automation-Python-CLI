import pyautogui
from time import sleep
import keyboard

# tab and enter

if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('tab'):

            while True:

                pyautogui.press('enter')

                sleep(1)


                pyautogui.press('tab')


                if keyboard.is_pressed('q'):

                    break


