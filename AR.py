import webbrowser
from time import sleep

import keyboard
import pyautogui
import pyperclip

from aRE import mi_by_ag_re
from easy_list_mail import mi_to_mel
from f import (
    check_if_image_uploaded_and_return_url,
    close_tab,
    move_down_one_page,
    open_last_closed_tab,
    open_url_in_edge,
    paste_text,
    press_end,
    ss_url_domain_close_tab,
)
from reporter_on_brave import mi_on_bc

click_product_selection_x = 320
click_product_selection_y_normal = 886
click_product_selection_y_nsfw = 856


def click_fill_product_button_normal():
    """
    click_fill_product_button_normal Clicks on the product button with the given x y position.
    """
    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_normal)


def click_fill_product_button_nsfw():

    """
    click_fill_product_button_nsfw click_product_button_nsfw click_fill_product_button_nsfw
    """
    pyautogui.click(x=click_product_selection_x, y=click_product_selection_y_nsfw)


def fill_product(Create_new_issue_template):

    """
    param Create_new_issue_template the new issue template
    """
    if Create_new_issue_template == "bug_report.yml":

        click_fill_product_button_normal()

        pyautogui.click(
            x=click_product_selection_x, y=click_product_selection_y_normal + 47
        )

        click_fill_product_button_normal()

        pyautogui.press("pagedown")

    elif Create_new_issue_template == "bug_report_NSFW.yml":

        click_fill_product_button_nsfw()

        pyautogui.click(
            x=click_product_selection_x, y=click_product_selection_y_nsfw + 47
        )

        click_fill_product_button_nsfw()

        pyautogui.press("pagedown")

        pyautogui.scroll(36)


# product


def click_selection_button():

    """
    clicks on the selection button
    """
    pyautogui.click(x=300, y=335)


# fill problem as annoyance


def click_annoyance():

    """
    click_annoyance is called by pyautogui when clicking on a button
    """
    pyautogui.click(x=352, y=558)


def fill_problem_as_annoyance():

    """
    Fill problem as annoyance.
    """
    click_selection_button()

    click_annoyance()

    click_selection_button()


# browser


def click_browser_selection_button():

    """
    click_browser_selection_button is called when the user clicks the selection button
    """
    pyautogui.click(x=316, y=430)


def select_browser():

    """
    click on the screen.
    """
    pyautogui.click(x=322, y=524)


def click_device_selection_button():

    """
    clicks on the device selection button
    """
    pyautogui.click(x=320, y=534)


def select_device():

    """
    clicks on the device and sets the click event
    """

    pyautogui.click(x=311, y=581)


def fill_browser_and_device():

    """
    Fill the browser and device selection buttons.
    """

    click_browser_selection_button()

    # sleep(0.001)

    select_browser()

    # sleep(0.001)

    click_browser_selection_button()

    # sleep(0.001)

    click_device_selection_button()

    # sleep(0.001)

    select_device()

    # sleep(0.001)


# url


def click_url_box():

    """
    click_url_box click_url_box click_url_box
    """

    pyautogui.click(x=400, y=600)


# filter


def click_filter_selection_button():
    """
    clicks on the filter button
    """
    pyautogui.click(x=300, y=792)


def click_Adguard_Base_filter_box():

    pyautogui.click(x=300, y=826)


def click_Adguard_social_filter_box():

    pyautogui.click(x=300, y=826)


def click_Adguard_Annoyance_filter_box():

    pyautogui.click(x=300, y=842)


def fill_filter(Create_new_issue_template):
    """"""

    if Create_new_issue_template == "bug_report.yml":

        click_filter_selection_button()

        click_Adguard_Base_filter_box()

        pyautogui.press("pagedown")

        click_Adguard_social_filter_box()

        click_Adguard_Annoyance_filter_box()

        click_filter_selection_button()

    elif Create_new_issue_template == "bug_report_NSFW.yml":
        # Physical: {X=335,Y=791}
        # Physical: {X=313,Y=841}
        # Physical: {X=313,Y=829}
        # Physical: {X=316,Y=856}

        pyautogui.click(x=335, y=791)

        pyautogui.click(x=313, y=841)

        move_down_one_page()

        pyautogui.click(x=313, y=829)

        pyautogui.click(x=316, y=856)

        pyautogui.click(x=335, y=791)


def click_privacy():

    # pyautogui.click(x=287, y=973)

    pyautogui.click(x=285, y=672)


# submit issue


def click_on_submit_new_issue():

    pyautogui.click(750, 1240)


def open_create_issue_page(
    Create_new_issue_template, Create_new_issue_Account, site_domain
):

    """
    This function opens the create issue page and fills the fields with the data provided.
    :param Create_new_issue_template: The template to use for the issue.
    :param Create_new_issue_Account: The account to use for the issue.
    :param site_domain: The domain of the site to use for the issue.
    :return:   None
    """

    url = f"https://github.com/{Create_new_issue_Account}/issues/new?template={Create_new_issue_template}&title={site_domain}"

    if "NSFW" in Create_new_issue_template:

        open_url_in_edge(url)

    else:

        webbrowser.open(url)


def create_issue_on_gh_ag(Create_new_issue_template, Create_new_issue_Account):

    site_url, site_domain = ss_url_domain_close_tab()

    open_create_issue_page(
        Create_new_issue_template, Create_new_issue_Account, site_domain
    )

    sleep(5)

    fill_product(Create_new_issue_template)

    fill_problem_as_annoyance()

    fill_browser_and_device()

    click_url_box()

    image_url = check_if_image_uploaded_and_return_url()

    pyperclip.copy(site_url)

    paste_text()

    sleep(0.1)

    fill_filter(Create_new_issue_template)

    move_down_one_page()

    def screenshot_body():

        pyautogui.click(393, 500)

    screenshot_body()

    pyautogui.hotkey("ctrl", "a")

    pyperclip.copy(
        f"""<details><summary>Screenshots:</summary>



[screenshot]({image_url})



</details><br/>"""
    )

    paste_text()

    # take focus out of the screenshot body

    pyautogui.click(x=100, y=500)

    sleep(0.01)

    press_end()

    sleep(0.1)

    # click on submit new issue
    pyautogui.click(x=1240, y=745)

    print("done")

    open_last_closed_tab()

    close_tab()

    print("loop completed")

    mi_to_mel(site_url, site_domain, image_url)


Create_new_issue_Account = "AdguardTeam/AdguardFilters"

# Create_new_issue_Account = "chirag127/test"


if __name__ == "__main__":

    print("Press ctrl + q to make new issue for a Non-NSFW website")
    print("Press alt + x to make new issue for a NSFW website")
    print("Press alt + q to make new issue on adguard.com")
    print("Press alt + b to make new issue on brave.com")

    while True:

        if keyboard.is_pressed("q"):

            mi_by_ag_re()

        elif keyboard.is_pressed("alt + x"):

            mi_by_ag_re(is_chrome=False)

        elif keyboard.is_pressed("alt + q"):

            create_issue_on_gh_ag("bug_report.yml", Create_new_issue_Account)

        elif keyboard.is_pressed("alt + b"):

            mi_on_bc()

        else:

            sleep(0.1)
