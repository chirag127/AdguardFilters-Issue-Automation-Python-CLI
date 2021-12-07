import AdguardFilters.Annoyances
import keyboard
from time import sleep


if __name__ == "__main__":

    while True:

        if keyboard.is_pressed('ctrl + q'):
            AdguardFilters.Annoyances.main()

        else:
            sleep(0.1)
