import pyautogui


# define a function that will open the last closed tab
# open last closed tab
def open_last_closed_tab():

    pyautogui.hotkey('ctrl', 'shift', 't')


# define a function that will close tab
def close_tab():

    pyautogui.hotkey('ctrl', 'w')

# define a function that will go to next tab using pyautogui.hotkey('ctrl', 'tab')


def go_to_next_tab():

    pyautogui.hotkey('ctrl', 'tab')


# define a function that will copy the url from the url bar using the pyautogui library by pressing the "ctrl" key + "c"
def copyselectedtext():

    pyautogui.hotkey('ctrl', 'c')


# define a function that will move down one page
def move_down_one_page():

    pyautogui.hotkey('pagedown')
