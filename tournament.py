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
    blackplays: int = field(default=0, init=False)

    def __str__(self):
        return f"{self.name}: {self.score}"

    def __lt__(self, other):
        return self.score < other.score


class Tournament:
    """
    Represents a tournament.
    """

    def __init__(self):
        self.player_list = []

    def leaderboard(self):
        """
        prints the leaderboard
        """
        sorted = self.player_list.copy()
        sorted.sort(reverse=True)
        print("Leaderboard\n-----------------------")
        for player in sorted:
            print(player)

    # NB: we don't know in what kind of format the game component outputs
    # the score after each match, right now we assume winner_id
    def update_leaderboard(self, winner_id):
        """
        updates the leaderboard
        :param winner_id: the id of the player who one the last match
        """
        if 0 <= winner_id < len(self.player_list):
            self.player_list[winner_id].score += 1

    def check_for_tiebreak(self):
        """
        check if there is a tiebreak
        :return: list of players with the same (highest) score if more than one player, else return empty list
        """
        sorted = self.player_list.copy()
        sorted.sort(reverse=True)

        tiebreak_list = []
        for player in sorted:
            if player.score < sorted[0].score:
                break
            tiebreak_list.append(player)
        return tiebreak_list if len(tiebreak_list) > 1 else []
    
    def initialize_players(self):
        """
        asks user to input how many players will be playing, and the names of the players
        saves the players in the tournament
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

        self.player_list = []
        for i in range(answer):
            name = input(f"Please type in player {i+1}'s name! ")
            self.player_list.append(Player(name, i))