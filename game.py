from tournament import Tournament, Player

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


def number_of_players():
    """
    asks user to input how many players will be playing, and the names of the players
    :return: list of player names
    """
    answer = ""
    while True:
        answer = input("How many players are playing today? ")
        if answer.isdigit():
            answer = int(answer)
            if 3 <= answer <= 8:
                break
            else:
                print("Please type in a number between 3 and 8")

    answer = int(answer)

    player_list = []
    for i in range(answer):
        player_list.append(input(f"Please type in player {i+1}'s name! "))
    return player_list


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
