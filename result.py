import pyautogui
from time import sleep
import webbrowser
import pyperclip

# Physical: {X=562,Y=448};
# Physical: {X=618,Y=724};
# Physical: {X=516,Y=493};
# Physical: {X=850,Y=739};
# Physical: {X=923,Y=614};

def close_tab():
    pyautogui.press('ctrl', 'w')

def main(roll_number):

    url = "http://jabinresults.eadminaargees.com/"

    webbrowser.open(url)

    pyperclip.copy(roll_number)

    sleep(2)

    pyautogui.click(x=562, y=448)

    sleep(0.1)

    pyautogui.click(x=618, y=724)

    sleep(0.1)

    pyautogui.click(x=516, y=493)

    sleep(0.1)

    pyautogui.hotkey('ctrl', 'v')

    sleep(0.1)

    pyautogui.press('enter')

    sleep(1)

    pyautogui.rightClick(x=850, y=739)

    sleep(0.1)

    pyautogui.click(x=923, y=614)

    sleep(0.2)

    pyautogui.hotkey('ctrl', "v")

    sleep(0.1)

    pyautogui.press('enter')

    sleep(0.1)

    close_tab()

if __name__ == "__main__":

    for i in range(219001,219241):
        main(i)
