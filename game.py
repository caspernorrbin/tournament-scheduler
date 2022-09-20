from tournament import Tournament, Player
## Takes a list of players and returns a selected player or None if selection is cancelled
def select_player(players):
    options = ["[Go back]", *players]
    while True:
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        selection = input("Selection: ")
        if selection == "1":
            return None
        elif selection.isdigit() and int(selection) <= len(options) and int(selection) > 0:
            return players[int(selection)-1]
        else:
            print("Invalid selection")

def startmenu():
    print('''Welcome to the game!
[S]tart game]
[T]ournament]
[Q]uit]''')
    choice = ""
    while choice not in ["S", "T", "Q"]:
        choice = input("Option: ").upper()
    return choice


def game():
    print("Game")


def tournament():
    tournament = Tournament()
    tournament.begin_tournament()


def main():
    a = startmenu()

    if a == "S":
        game()
    elif a == "T":
        tournament()
    elif a == "Q":
        quit()


if __name__ == "__main__":
    main()
