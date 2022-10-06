import __init__, os
from enum import Enum
from game_interaction import start_game

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
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{player1.name} is playing with the colour white.')
    print(f'{player2.name} is playing with the colour black.')
    return MatchResult(start_game(player1.name, player2.name))
