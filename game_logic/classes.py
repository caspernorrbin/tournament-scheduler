import random
from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict


# The definition of a game piece. The piece has the colour 'white' or 'black'.
# A piece can be standing or laying (True or False)
# Note: there is no check if the colour of the Piece is ('black' or 'white')
@dataclass
class Piece:
    def __init__(self, colour, standing):
        self.colour = colour
        self.standing = standing
    
    def __eq__(self, __o: object) -> bool:
        return self.colour == __o.colour and self.standing == __o.standing

    def __str__(self):
        if self.standing:
            return f'Standing {self.colour} piece'
        return f'Lying {self.colour} piece'


# The definition of a player of the game. The player plays as colour 'black' or 'white'
# A player has a max amount of 15 pieces (the starting amount of pieces is 15).
# Note: there is no check in the definition that (0 <= pieces <= 15) and that colour of the Player
# is ('black' or 'white')
@dataclass
class Player:
    def __init__(self, colour, pieces, name = ''):
        self.colour = colour
        self.pieces = pieces
        self.name = name


@dataclass
class Board():
    '''Represents the game board

    Example:
    Board.state = {1 (board position): [game_piece],
                   2                 : [game_piece],
                   3                 : [game_piece],
                   4                 : [game_piece],
                   ...}'''
    size: int
    state: DefaultDict

    def __init__(self):
        '''Initialise a 4x4 game board'''
        self.size = 16
        self.state = defaultdict(list)


def randomise_colours(player1: Player, player2: Player):
    '''Randomise colours for two players
    
    Parameters: a player
                a player
    '''
    colours = ['white', 'black']

    ran_colour_index = random.getrandbits(1)
    colour1 = colours[ran_colour_index]
    colour2 = colours[not ran_colour_index]

    player1.colour = colour1
    player2.colour = colour2


def black_starts_game(player1: Player, player2: Player):
    '''Decides that the black player is the one to start the game
    
    Parameters: the two players
    Returns: the player that is black and will start'''

    if player1.colour == "black":
        return player1
    else:
        return player2

@dataclass
class GameState():
    '''An object that contains the board and the current two players in the game.'''
    def __init__(self, name1 = '', name2 = ''):
        '''Initiate board and two players with 15 pieces each.'''
        self.board = Board()

        self.player_1 = Player('white', 15, name1)
        self.player_2 = Player('black', 15, name2)

        self.current_player = black_starts_game(self.player_1, self.player_2)
        