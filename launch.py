from higherLower import HigherLower
from utils import clear_terminal


def launch():
    valid_game = True
    game = HigherLower()

    while valid_game:
        valid_game = game.round()

    while True:
        print("Do you want to play another game? [Yes/No]")
        new_game = input("> ").lower()

        if new_game == 'yes':
            launch()
            break
        elif new_game == 'no':
            break
        else:
            print("Invalid input. Try again!\n")
