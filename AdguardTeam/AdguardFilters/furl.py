import pyautogui
import keyboard
from time import sleep



def click_url_box():

    sleep(1)

    # urlabovetextcoordinates = pyautogui.locateOnScreen('url.png')
# 
    # urlabovetextcoordinates = pyautogui.center(urlabovetextcoordinates)
# 
    # pyautogui.click(x=urlabovetextcoordinates[0], y=urlabovetextcoordinates[1])
# 

    pyautogui.click(x=400, y=600)

    sleep(1)
    

if __name__ == '__main__':

    while True:

        if keyboard.is_pressed('ctrl+shift+u'):

            click_url_box()

            sleep(1)
