from tournament import Tournament
from player import Player
from match import MatchResult, play_match

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
    name1 = input("Please type in the name of the first player: ")
    name2 = input("Please type in the name of the second player: ")

    player1 = Player(name1, 0)
    player2 = Player(name2, 1)

    result = play_match(player1, player2)

    if result == MatchResult.P1_WIN or result == MatchResult.P2_QUIT:
        print(f"Congratulations {player1.name}!")

    else:
        print(f"Congratulations {player2.name}!")


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
