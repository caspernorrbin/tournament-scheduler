from enum import Enum

class MatchResult(Enum):
    WHITE_WIN = 1
    BLACK_WIN = 2
    WHITE_QUIT = 3
    BLACK_QUIT = 4

def play_match(player1, player2):
    """
    Simulates a match between two players
    :param player1: the first player
    :param player2: the second player
    :return: 
    """
    print("Playing match...")
    print("White: " + player1.name)
    print("Black: " + player2.name)

    return MatchResult.WHITE_WIN
