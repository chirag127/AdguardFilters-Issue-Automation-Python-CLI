from f import *
import pyperclip


def main():

    # wait sometime before I  keyup the shortcut keys
    sleep(1)

    pyautogui.hotkey('ctrl', 'prtsc')

    sleep(0.1)

    pyautogui.moveTo(x=500, y=500)

    sleep(0.1)

    pyautogui.click()

    # select the url of the current webpage
    pyautogui.hotkey('alt', 'd')

    # copy the selected url to the clipboard
    pyautogui.hotkey('ctrl', 'c')

    # get the url of the website by using the clipboard
    site_url = pyperclip.paste()

    close_tab()

    open_create_issue_page(site_url)

    fill_product()

    fill_Problem()

    fill_url()

    fill_filter()

    while True:

        image_url = pyperclip.paste()

        if "imgur" not in image_url:

            print("waiting for the image to be uploaded")

            sleep(1)

        else:

            break

    sleep(0.1)

    fill_screenshot()

    fill_comment()

    fill_check()

    open_last_closed_tab()

    close_tab()
    

if __name__ == "__main__":

    print("Press ctrl + q to make new issue for a Non-NSFW website")
    
    print("Press alt + x to make new issue for a NSFW website")

    while True:

        import keyboard

        if keyboard.is_pressed('ctrl + q'):

            main()

        else:

            sleep(0.1)
