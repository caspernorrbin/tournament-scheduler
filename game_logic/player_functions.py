from classes import Player


# A function that creates a new player with the given colour and 15 starting pieces.
# Parameters: the colour of the wanted player.
# Returns: a Player with the given colour and 15 pieces. (see class_definitions)
def generate_new_player(colour):
    new_player = Player(colour, 15)
    return new_player


# A function that returns a given player's colour.
# Parameters: a player
# Returns: the player's colour as a string.
def player_colour(player: Player):
    return player.colour


# A function that returns how many pieces a player has.
# Parameters: a player
# Returns: the player's current amount of pieces.
def player_pieces_left(player: Player):
    return player.pieces


# A function that decreases the pieces of a player by one. Changes directly in player.
# Parameters: a player
# Returns: Nothing, Changes the value of player.pieces by one.
def player_decrement_pieces(player: Player):
    player.pieces -= 1


def is_out_of_pieces(player: Player):
    '''Check if a player is out of pieces

    Parameters: a player
    Return: True if the player is out of pieces, otherwise False'''
    return player.pieces == 0
