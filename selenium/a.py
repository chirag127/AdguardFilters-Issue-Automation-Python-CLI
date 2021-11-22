from selenium import webdriver
from zfunctions import *

def main():

    # create a browser instance

    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    w = webdriver.Chrome(executable_path=".\chromedriver.exe", chrome_options=options)

    sleep(1)

    pyautogui.hotkey('alt', 'd')

    copyselectedtext()

    # get the url of the website by using the clipboard
    url = clipboard.paste()

    # parse the url to get the domain name
    domain = urlparse(url).netloc


    w.get(
        'https://github.com/chirag127/test/issues/new?assignees=&template=bug_report.yml')

    w.find_element_by_id('issue_title').send_keys(domain)

if __name__ == '__main__':

    while True:

        if keyboard.is_pressed('ctrl + q'):
            main()

        else:
            sleep(0.1)


