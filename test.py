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

## Takes a list of players and the players of the upcoming match.
## Prints the players of the upcoming match.
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

while True:
    a = between_matches(["a", "b", "c"], "a", "b")
    print(a)
