from enum import Enum

class Match_result(Enum):
    P1_WIN = 1
    P2_WIN = 2
    P1_QUIT = 3
    P2_QUIT = 4

def play_match(Player1, Player2):
    """
    Simulates a match between two players
    :param Player1: the first player
    :param Player2: the second player
    :return: 
    """
    print("Playing match...")
    print("Player 1: " + Player1.name)
    print("Player 2: " + Player2.name)

    return Match_result.P1_WIN