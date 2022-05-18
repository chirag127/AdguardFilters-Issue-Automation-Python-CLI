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

    # open the url
    webbrowser.open(url)

    # wait for the page to load

    # copy the roll number
    pyperclip.copy(roll_number)

    sleep(2)

    # click on the dropdown menu
    pyautogui.click(x=562, y=448)

    sleep(0.1)

    # click on the dropdown menu option
    pyautogui.click(x=618, y=724)

    sleep(0.1)

    # click on the text box
    pyautogui.click(x=516, y=493)

    sleep(0.1)

    # paste the roll number
    pyautogui.hotkey('ctrl', 'v')

    sleep(0.1)

    # press enter
    pyautogui.press('enter')

    sleep(1)

    # right click on the result
    pyautogui.rightClick(x=850, y=739)

    sleep(0.1)

    # click on the download as csv
    pyautogui.click(x=923, y=614)

    sleep(0.2)

    # paste the roll number
    pyautogui.hotkey('ctrl', "v")

    sleep(0.1)

    # press enter
    pyautogui.press('enter')

    sleep(0.1)

    # close the tab
    close_tab()


if __name__ == "__main__":

    for i in range(219001, 219241):
        main(i)
