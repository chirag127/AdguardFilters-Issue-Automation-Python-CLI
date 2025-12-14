
import argparse
import keyboard
from time import sleep
from .email_reporter import create_and_send_ad_report
from .brave_reporter import report_ad_on_brave_community
from .comment_placer import main as post_comments
from .auto_clicker import auto_click_and_tab
from .extension_remover import main as remove_extensions
from .screenshot import take_screenshot

def main():
    """
    Main function to run the specified automation task.
    """
    parser = argparse.ArgumentParser(description="AdguardFilters Issue Automation CLI")
    parser.add_argument(
        "task",
        choices=[
            "report-email",
            "report-brave",
            "post-comments",
            "auto-click",
            "remove-extensions",
            "screenshot",
        ],
        help="The automation task to run.",
    )
    args = parser.parse_args()

    print(f"Running task: {args.task}")

    if args.task == "report-email":
        print("Press 'ctrl + q' to create and send an ad report.")
        while True:
            if keyboard.is_pressed("ctrl + q"):
                create_and_send_ad_report()
            else:
                sleep(0.1)
    elif args.task == "report-brave":
        print("Press 'alt + q' to report an ad on Brave Community.")
        while True:
            if keyboard.is_pressed("alt + q"):
                report_ad_on_brave_community()
            else:
                sleep(0.1)
    elif args.task == "post-comments":
        print("Press 'ctrl + v' to post comments.")
        while True:
            if keyboard.is_pressed("ctrl + v"):
                post_comments()
            else:
                sleep(0.1)
    elif args.task == "auto-click":
        print("Press 'tab' to start auto-clicking.")
        while True:
            if keyboard.is_pressed("tab"):
                auto_click_and_tab()
            else:
                sleep(0.1)
    elif args.task == "remove-extensions":
        print("Press 'ctrl + q' to remove extensions.")
        while True:
            if keyboard.is_pressed("ctrl + q"):
                remove_extensions()
            else:
                sleep(0.1)
    elif args.task == "screenshot":
        take_screenshot()

if __name__ == "__main__":
    main()
