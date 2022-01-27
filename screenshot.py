import pyautogui
import pyperclip
from time import sleep

# take a screenshot and paste it to the clipboard
image = pyautogui.screenshot(region=(0,88,1920,932))

# save the image to the downloads folder
# image.save("D:\\Downloads\\screenshot.png") 

image.save("screenshot.png")