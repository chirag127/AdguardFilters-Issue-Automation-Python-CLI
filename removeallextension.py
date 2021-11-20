import pyautogui
import keyboard
from time import sleep
# Physical: {X=1704,Y=54}; 
# Physical: {X=1669,Y=232}; 

# right click at the extension
def right_click_at_the_extension():

    pyautogui.rightClick(x=1704, y=54)

    sleep(0.5)


# define the function to click on the "Remove  extensions" option
def click_on_the_remove_extensions_option():
    
        pyautogui.click(x=1669, y=232)
    
        sleep(0.5)


# define the function to click press enter to remove the extension
def click_press_enter_to_remove_the_extension():
    
        pyautogui.press('enter')
    
        sleep(0.5)

def main():

        right_click_at_the_extension()

        click_on_the_remove_extensions_option()

        click_press_enter_to_remove_the_extension()


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):


            for i in range(1, 5):


                main()

