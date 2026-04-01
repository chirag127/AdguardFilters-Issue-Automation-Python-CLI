from io import BytesIO

import pyautogui
import win32clipboard


def take_screenshot(region: tuple[int, int, int, int] | None = None) -> None:
    """
    Takes a screenshot of the specified region and copies it to the clipboard.
    If no region is specified, it captures the entire screen.
    """
    try:
        image = pyautogui.screenshot(region=region)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        print("Screenshot copied to clipboard.")
    except (pyautogui.PyAutoGUIException, OSError) as e:
        print(f"Failed to take screenshot: {e}")


if __name__ == "__main__":
    # Example usage: take a screenshot of a specific region
    take_screenshot(region=(0, 88, 1920, 932))
