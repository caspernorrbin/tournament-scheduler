import uuid 

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

# created a function to start the tournament (we did not user the first function in case anyone is working on tht one)
def tournament_test():
    # get all the players in a list, the players are obbjects in the Player class
    player_list = get_player_list()
    # start tournament with the player_list
    tournament = Tournament(player_list)
    
def get_player_list():
    player_list = []
    # gets the names as an array from the function get_player_names
    names = get_player_names()

    for name in names:
        # assing each player a unique id with the uuid4 function
        player_id = uuid.uuid4().hex
        # create a new Player object for each player with their names and UUID
        player = Player(name, player_id)
        player_list.append(player)
    return player_list



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
