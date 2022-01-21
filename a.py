import pyautogui

try:    

    if pyautogui.locateOnScreen("adguard_next.png",  confidence=0.9) != None:
        
        print("done")
        
except Exception as e:
    print(e)
    
