from dataclasses import dataclass, field

@dataclass
class Player:
    """
    This class scores a player's name, their id and their score.
    :param name: name of the player
    :param player_id: player_id of the player
    """
    name: str
    player_id: int
    score: int = field(default=0, init=False)
    active: bool = field(default=True, init=False)
    whiteplays: int = field(default=0, init=False)
    blackplays: int = field(default = 0, init=False)
    
    def __str__(self):
        return self.name
    


class Tournament:
    """
    Represents a tournament.
    """
    def __init__(self, player_list):
        self.player_list = player_list

    def leaderboard(self):
        """
        prints the leaderboard
        """
        tuple_list = [(player.name, player.score) for player in self.player_list]
        tuple_list.sort(key=lambda tup: tup[1], reverse=True)
        print("Leaderboard\n-----------------------")
        for element in tuple_list:
            print(f"{element[0]}: {element[1]}")

    # NB: we don't know in what kind of format the game component outputs
    # the score after each match, right now we assume winner_id
    def update_leaderboard(self, winner_id):
        """
        updates the leaderboard
        :param winner_id: the id of the player who one the last match
        """
        for player in self.player_list:
            if player.player_id == winner_id:
                player.score += 1

    def check_for_tiebreak(self):
        """
        check if there is a tiebreak
        :return: list of players with the same (highest) score if more than one player, else return False
        """
        tuple_list = [(player.name, player.score, player.player_id) for player in self.player_list]
        tuple_list.sort(key=lambda tup: tup[1], reverse=True)
        tiebreak_list = []

        for i in range(len(tuple_list)):
            if tuple_list[0][1] == tuple_list[i][1]:
                tiebreak_list.append(tuple_list[i][2])
        if len(tiebreak_list) > 1:
            return tiebreak_list

        else:
            return False




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



def get_player_names():
    """
    asks user to input how many players will be playing, and the names of the players
    :return: list of player names
    """
    how_many = input("How many players are playing today? ")
    if how_many.isdigit():
        how_many = int(how_many)
        if 3 <= how_many <= 8:
            name_list = []
            for name in range(how_many):
                next_name = input(f"Please type in player {name+1}'s name! ")
                name_list.append(next_name)

            return name_list
        else:
            print("Please type in a number between 3 and 8")
            return get_player_names()

    else:
        print("Please type in a number! ")
        return get_player_names()


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
