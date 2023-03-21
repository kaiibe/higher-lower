from utils import clear_terminal
from dataset import celebrity_dataset
import random


class HigherLower():
    def __init__(self) -> None:
        self.celebrity_data = celebrity_dataset
        self.celebrityA = self.get_celebrity()
        self.celebrityB = self.get_celebrity()

        self.score = 0

    def get_celebrity(self):
        celebrity = random.choice(self.celebrity_data)
        self.celebrity_data.remove(celebrity)
        return celebrity

    def round(self) -> bool:
        clear_terminal()
        print(f"Compare A: {self.celebrityA['name']}")
        print(f"Against B: {self.celebrityB['name']}\n")

        while True:
            print("Who has more followers? [A/B]")
            choice = input("> ").lower()

            if choice == 'a' or choice == 'b':
                break
            else:
                print("Invalid input. Try again!\n")

        if (choice == "A") and (self.celebrityA['followers'] >= self.celebrityB['followers']):
            self.score += 1
            print(f"You are right! Current score: {self.score}")
            self.celebrityB = self.get_celebrity()
            return True
        elif (choice == "B") and (self.celebrityA['followers'] < self.celebrityB['followers']):
            self.score += 1
            print(f"You are right! Current score: {self.score}")
            self.celebrityA = self.get_celebrity()
            return True
        else:
            print(f"You was wrong! Your final score: {self.score}\n")
            return False
