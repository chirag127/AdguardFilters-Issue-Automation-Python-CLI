from time import sleep

import keyboard
import pyautogui


def remove_extension() -> None:
    """
    Automates the removal of a browser extension.
    """
    try:
        # Right-click at the extension icon's coordinates
        pyautogui.rightClick(x=1704, y=54)
        sleep(0.5)

        # Click on the "Remove extensions" option
        pyautogui.click(x=1669, y=232)
        sleep(0.5)

        # Press enter to confirm the removal
        pyautogui.press("enter")
        sleep(0.5)
    except pyautogui.PyAutoGUIException as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to remove multiple extensions.
    """
    for _ in range(5):
        remove_extension()


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("ctrl + q"):
            main()
