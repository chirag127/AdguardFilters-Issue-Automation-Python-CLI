
from azfunctions import *

Create_new_issue_template = "bug_report_NSFW.yml"
# Create_new_issue_Account = "chirag127/test"
Create_new_issue_Account = "AdguardTeam/AdguardFilters"


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):
            create_issue(Create_new_issue_template, Create_new_issue_Account)

        else:
            sleep(0.1)
