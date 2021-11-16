from functions import *
from prerequisites import click_on_all_prerequisites_checkboxes


# create issue on the https://github.com/AdguardTeam/AdguardFilters/issues/new?assignees=&template=bug_report.yml



def main():

    sleep(1)
    
    pyautogui.hotkey('alt', 'd')

    copyselectedtext()

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc

    webbrowser.open(
        "https://github.com/chirag127/test/issues/new?assignees=&template=bug_report.yml")

    sleep(3)

    pyautogui.typewrite(domain)

    sleep(0.1)

    click_on_all_prerequisites_checkboxes()

    
if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):
            main()

        else:
            sleep(0.1)
