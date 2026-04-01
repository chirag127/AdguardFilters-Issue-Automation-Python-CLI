from time import sleep

import keyboard
import pyautogui
import pyperclip


def post_comment(
    comment: str, x: int, y: int, comment_button_x: int, comment_button_y: int
) -> None:
    """
    Automates posting a comment on a webpage.
    """
    pyautogui.press("end")
    sleep(0.2)
    pyperclip.copy(comment)
    sleep(0.2)
    pyautogui.click(x=x, y=y)
    sleep(0.2)
    pyautogui.hotkey("ctrl", "v")
    sleep(0.2)
    pyautogui.click(x=comment_button_x, y=comment_button_y)
    sleep(0.2)
    pyautogui.hotkey("ctrl", "tab")
    sleep(0.2)


def main():
    comment_text = "Why is the Invalid tag added to this issue?"
    # Coordinates for the comment box and button
    comment_box_x = 374
    comment_box_y = 611
    comment_button_x = 1213
    comment_button_y = 747

    for _ in range(10):
        post_comment(
            comment_text,
            comment_box_x,
            comment_box_y,
            comment_button_x,
            comment_button_y,
        )
        sleep(1)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("ctrl + v"):
            main()
        else:
            sleep(0.1)
