from azfunctions import *
import keyboard


page_down = 816

Create_new_issue_template = "bug_report.yml"
# Create_new_issue_template = "bug_report_NSFW.yml"
#Create_new_issue_Account = "chirag127/test"
Create_new_issue_Account = "AdguardTeam/AdguardFilters"


if __name__ == "__main__":

    print("Press ctrl + q to make new issue for a Non-NSFW website")
    print("Press alt + x to make new issue for a NSFW website")

    while True:

        if keyboard.is_pressed('ctrl + q'):

            create_issue("bug_report.yml", Create_new_issue_Account)

        elif keyboard.is_pressed('alt + x'):

            create_issue("bug_report_NSFW.yml", Create_new_issue_Account)

        else:
            sleep(0.1)
