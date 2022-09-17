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

    def __init__(self, player_list):
        self.player_list = player_list

    def leaderboard(self):
        """
        prints the leaderboard
        """
        self.player_list.sort(reverse=True)
        print("Leaderboard\n-----------------------")
        for player in self.player_list:
            print(player)

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
        :return: list of players with the same (highest) score if more than one player, else return empty list
        """
        self.player_list.sort(reverse=True)

        tiebreak_list = []
        for player in self.player_list:
            if player.score < self.player_list[0].score:
                break
            tiebreak_list.append(player)
        return tiebreak_list if len(tiebreak_list) > 1 else []
