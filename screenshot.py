import pyautogui

from io import BytesIO
import win32clipboard

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

# take a screenshot and paste it to the clipboard
image = pyautogui.screenshot(region=(0,88,1920,932))

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)
