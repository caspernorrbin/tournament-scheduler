from enum import Enum

class MatchResult(Enum):
    WHITE_WIN = 1
    BLACK_WIN = 2
    WHITE_QUIT = 3
    BLACK_QUIT = 4

def play_match(white, black):
    """
    Simulates a match between two players
    :param player1: the first player
    :param player2: the second player
    :return: 
    """
    print("Playing match...")
    print("White: " + white.name)
    print("Black: " + black.name)
    # Quit means quitting the tournament, not the match
    choice = input("Who won? (1/2) quit(3/4): ")
    return MatchResult(int(choice))
