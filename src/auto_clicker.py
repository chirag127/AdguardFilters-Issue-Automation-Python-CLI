
import pyautogui
from time import sleep
import keyboard

def auto_click_and_tab() -> None:
    """
    Automates a sequence of enter and tab presses.
    """
    while True:
        pyautogui.press("enter")
        sleep(1)
        pyautogui.press("tab")
        if keyboard.is_pressed("q"):
            break

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("tab"):
            auto_click_and_tab()
