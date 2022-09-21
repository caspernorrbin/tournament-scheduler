from enum import Enum

class MatchResult(Enum):
    P1_WIN = 1
    P2_WIN = 2
    P1_QUIT = 3
    P2_QUIT = 4

def play_match(player1, player2):
    """
    Simulates a match between two players
    :param player1: the first player
    :param player2: the second player
    :return: 
    """
    print("Playing match...")
    print("Player 1: " + player1.name)
    print("Player 2: " + player2.name)

    return MatchResult.P1_WIN
