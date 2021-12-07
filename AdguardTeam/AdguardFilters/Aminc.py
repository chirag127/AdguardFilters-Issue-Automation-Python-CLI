from Annoyances import main
import keyboard
from time import sleep


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):
            main()

        else:
            sleep(0.1)
