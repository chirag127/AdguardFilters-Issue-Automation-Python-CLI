import pyautogui
from time import sleep

# Physical: {X=312,Y=335}
# Physical: {X=352,Y=558}

def click_selection_button():
    pyautogui.click(x=300 , y=335)

# fill problem as annoyance
def click_annoyance():
    
        pyautogui.click(x=352, y=558)
    
        sleep(0.01)
    

def fill_problem_as_annoyance():
    
    click_selection_button()
    
    sleep(0.01)
    
    click_annoyance()

    sleep(0.01)

    click_selection_button()

