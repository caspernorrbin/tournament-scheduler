## Takes a list of players and returns a selected player or None if selection is cancelled
def select_player(players):
    players.insert(0, "[Go back]")
    while True:
        for i in range(len(players)):
            print(f"{i+1}. {players[i]}")
        selection = input("Selection: ")
        if selection == "1":
            return None
        elif selection.isdigit() and int(selection) <= len(players) and int(selection) > 0:
            return players[int(selection)-1]
        else:
            print("Invalid selection")

## Takes a list of players and the players of the upcoming match.
## Returns a list of players who want to quit before the upcoming match.
def between_matches(players, player1, player2):
    quitters = []
    while True:
        #print("Leaderboard TODO")
        print(f"Next match: {player1} vs {player2}")
        print("1. Continue")
        print("2. A player wants to quit")
        selection = input("Selection: ")
        if selection == "1":
            return quitters
        elif selection == "2":
            quitter = select_player(players)
            if quitter != None:
                quitters.append(quitter)
            if quitter == player1 or quitter == player2:
                return quitters

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
    print("Tournament")


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
