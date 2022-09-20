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
