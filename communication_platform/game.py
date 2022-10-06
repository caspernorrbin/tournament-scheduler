import os
import __init__
from random import getrandbits
from menus import print_rules
from tournament import Tournament
from player import Player
from match import MatchResult, play_match


def startmenu():
    print('''Welcome to the game!
[S]tart game
[T]ournament
[R]ules
[Q]uit''')
    choice = ""
    while choice not in ["S", "T", "R", "Q"]:
        choice = input("Option: ").upper()
    return choice


def game():
    name1 = input("Please type in the name of the first player: ")
    name2 = input("Please type in the name of the second player: ")

    white = Player(name1, 0)
    black = Player(name2, 1)

    if getrandbits(1):
        white, black = black, white

    result = play_match(white, black)

    if result == MatchResult.WHITE_WIN or result == MatchResult.BLACK_QUIT:
        print(f"Congratulations {white.name}!")

    else:
        print(f"Congratulations {black.name}!")
    input('Press enter to continue to main menu.')


def tournament():
    tournament = Tournament()
    tournament.begin_tournament()
    input('Press enter to continue to main menu.')


def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        a = startmenu()

        if a == "S":
            game()
        elif a == "T":
            tournament()
        elif a == "R":
            print_rules()
        elif a == "Q":
            quit()


if __name__ == "__main__":
    main()
