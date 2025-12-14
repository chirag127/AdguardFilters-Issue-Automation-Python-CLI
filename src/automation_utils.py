
import pyautogui
from time import sleep
import pyperclip

def take_screenshot_with_sharex() -> None:
    """Takes a screenshot using ShareX hotkey."""
    sleep(1)
    pyautogui.hotkey("ctrl", "prtsc")
    sleep(0.1)
    pyautogui.click()

def wait_for_imgur_url() -> str:
    """Waits for an imgur URL to appear in the clipboard and returns it."""
    while True:
        image_url = pyperclip.paste()
        if "imgur" in image_url:
            return image_url
        print("waiting for the image to be uploaded")
        sleep(1)

def copy_selected_text() -> None:
    """Copies the selected text to the clipboard."""
    pyautogui.hotkey("ctrl", "c")
    print("Copied text")

def paste_text() -> None:
    """Pastes text from the clipboard."""
    pyautogui.hotkey("ctrl", "v")
    print("Pasted text")

def select_all() -> None:
    """Selects all text in the current context."""
    pyautogui.hotkey("ctrl", "a")
    print("Selected all")

def press_end() -> None:
    """Presses the 'end' key."""
    pyautogui.press("end")
    print("Pressed end")

def press_enter() -> None:
    """Presses the 'enter' key."""
    pyautogui.press("enter")
    print("enter pressed")

def move_down_one_page() -> None:
    """Presses the 'pagedown' key."""
    pyautogui.hotkey("pagedown")
    print("Moved down one page")
