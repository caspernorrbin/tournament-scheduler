from classes import Piece, Player


# A function that generates a piece belonging to a player that is standing or lying.
# Parameters: a player and True if the piece should be standing.
# Returns: a new piece of the player's colour that is standing or not.
def generate_piece(player: Player, is_standing: bool):
    new_piece = Piece(player.colour, is_standing)
    return new_piece


# A function that returns the colour of a piece.
# Parameters: a piece
# Returns: the colour of a piece in the form of a string.
def piece_colour(piece: Piece):
    return piece.colour


# A function that returns if a given piece is standing or not.
# Parameters: a piece
# Returns: true if the piece is standing, otherwise returns false.
def piece_is_standing(piece: Piece):
    return piece.standing
