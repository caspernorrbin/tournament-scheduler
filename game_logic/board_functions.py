from classes import Board, GameState


def is_board_full(board: Board):
    '''Count the number of occupied squares on the board and if all squares are occupied then the board is full (the game is finished)

    Parameters: a board
    Returns: True if the board is full, otherwise False'''
    for stack in board.state.values():
        if not stack:
            return False
    return len(board.state.values()) == board.size


def count_all_pieces(board: Board):
    '''Count all pieces on the board

    Parameters: a game board
    Returns: Number of white pieces, Number of black pieces, Total number of pieces'''
    num_white = 0
    num_black = 0

    condition_w = (lambda x: x.colour == 'white')
    condition_b = (lambda x: x.colour == 'black')

    for key in board.state.keys():
        num_white += len(list(filter(condition_w, board.state[key])))
        num_black += len(list(filter(condition_b, board.state[key])))

    return num_white, num_black, num_white + num_black


def count_topmost_lying_pieces(board: Board):
    '''Count all the topmost pieces that are in a laying position

    Parameters: a game board
    Returns: Number of white topmost lying pieces, Number of black topmost lying pieces'''
    num_white = 0
    num_black = 0

    keys = board.state.keys()

    for key in keys:
        pieces = board.state[key]
        if pieces:
            if not pieces[-1].standing:
                if pieces[-1].colour == 'white':
                    num_white += 1
                elif pieces[-1].colour == 'black':
                    num_black += 1
    return num_white, num_black


def is_stack_moveable(game_state: GameState, square_to_check):
    '''Check if stack is moveable by looking if it contains a standing piece, if it does it cannot be moved

    Parameters: a game state and the square to check for moveable stack
    Returns: True if the stack is moveable, False if not'''
    return is_colour_in_square(game_state.board, square_to_check, game_state.current_player.colour)


def contains_standing_piece(board, square_to_check):
    '''Check if stack contains a standing piece

    Parameters: a game board and the square to check for moveable stack
    Returns: True if the stack contains a standing piece, False if not'''
    stack = board.state[square_to_check]

    if stack == []:
        return False

    top_piece = stack[-1]

    return top_piece.standing


def is_colour_in_square(board: Board, square: int, colour: str):
    '''Check if any pieces in the stack on a certain square has the colour given.

    Parameters: a board
                a square
                a colour (white or black)'''
    stack = board.state[square]
    return any(piece.colour == colour for piece in stack)


def convert_input_to_square(row, col):
    '''Converts input in the form of rows and columns to the correlating square (1-16)
    
    Parameters: row is the row on the board. col is the column on the board. 
    Returns: The square that is at row 'row' and column 'col' '''
    rowdic = {1: [1, 2, 3, 4], 2: [5, 6, 7, 8],
              3: [9, 10, 11, 12], 4: [13, 14, 15, 16]}

    chosen_square = rowdic.get(row)[col - 1]
    return int(chosen_square)


def convert_input_to_coord(square):
    '''Converts input in the form of square (1-16) to the correlating rows and columns

    Parameters: square (1-16)
    Returns: row and column of the given square
    '''
    row = (square - 1) // 4 + 1
    col = (square - 1) % 4 + 1
    return row, col


def is_destination_valid(board, row, col):
    '''Check if input from user is a valid destination (for placing a piece)

    Parameters: a game board, a row, a column and a position for a piece (L for laying, S for standing)
    Returns: True if the destination is valid, 
    False, "Can not place piece on another standing piece" if the destination has a standing piece on it
    False, "Not a valid row/column/position" if the row/column/position is invalid. '''
    if not valid_coordinate('Useless', row, col)[0]:
        return False, "Invalid coordinate."
    else:
        chosen_square = convert_input_to_square(row, col)
        piece_standing = contains_standing_piece(board, chosen_square)

        if piece_standing:
            return False, "Invalid move, there is a standing piece on the square"

        else:
            return True, "OK"


def valid_coordinate(_, row, col):
    ''' Check if input from user is a valid destination (for moving a stack)

    Parameters: a row, a column and a position for a piece (L for laying, S for standing)
    Returns: True if the destination is valid,
    False, "Not a valid row/column/position" if the row/column/position is invalid. '''
    if (0 > row or row > 4) and (0 > col or col > 4):
        return False, "row {} and column {} are not valid".format(row, col)
    elif 0 > row or row > 4:
        return False, "row {} is not a valid row".format(row)
    elif 0 > col or col > 4:
        return False, "column {} is not a valid column".format(col)
    else:
        return True, "OK"
