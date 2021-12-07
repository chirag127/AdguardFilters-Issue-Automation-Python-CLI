import pyautogui
import keyboard


def click_url_box():

    pyautogui.click(x=400, y=600)



if __name__ == '__main__':

    while True:

        if keyboard.is_pressed('ctrl+shift+u'):

            click_url_box()

