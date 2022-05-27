import pyautogui
from time import sleep
import pyperclip
import keyboard

# Physical: {X=374,Y=611}
# Physical: {X=1213,Y=747}
# auto comment same thing on many tabs


def main():
    pyautogui.press("end")

    sleep(0.2)

    pyperclip.copy("Why Invalid tag is added to this issue?")

    sleep(0.2)

    pyautogui.click(x=374, y=611)

    sleep(0.2)

    pyautogui.hotkey("ctrl", "v")

    sleep(0.2)

    # click on comment button
    pyautogui.click(x=1213, y=747)

    sleep(0.2)

    # go to next tab

    pyautogui.hotkey("ctrl", "tab")

    sleep(0.2)


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed("ctrl + v"):

            for _ in range(10):
                main()
                sleep(1)
        else:
            sleep(0.1)
