
import pyautogui


# define a function that will click on all prerequisites checkboxes
def click_on_all_prerequisites_checkboxes():

    # click on the checkbox "This site DOES NOT contains sexually explicit material, otherwise use NSFW-specific form"
    pyautogui.click(x=289, y=651)

    # click on the checkbox "Filters were updated before reproduced an issue"
    pyautogui.click(x=289, y=689)

    # click on the checkbox "AdGuard product version is up-to-date"
    pyautogui.click(x=289, y=726)

    # click on the checkbox "Browser version is up-to-date"
    pyautogui.click(x=289, y=761)

    # click on the checkbox "If the site or app is broken, disabling AdGuard protection resolves an issue."
    pyautogui.click(x=289, y=800)
