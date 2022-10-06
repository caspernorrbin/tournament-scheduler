from copy import deepcopy
from math import sqrt
from classes import GameState, Piece
from board_functions import contains_standing_piece, is_board_full, count_topmost_lying_pieces, is_stack_moveable
from piece_functions import generate_piece
from player_functions import is_out_of_pieces, player_decrement_pieces


def can_place_piece(game_state: GameState):
    '''Checks if a player can place a piece.

    Parameters: a game state containing a board and two players
    Returns: True if a piece can be placed, otherwise False'''
    return not any([is_board_full(game_state.board), is_out_of_pieces(game_state.player_1), is_out_of_pieces(game_state.player_2)])


def determine_winner(game_state: GameState):
    '''Determine who wins when no player can make any moves.

    Parameters: a game state containing a board and two players
    Returns: The player who won (None if no one wins)'''
    if not can_place_piece(game_state):
        white_pieces, black_pieces = count_topmost_lying_pieces(
            game_state.board)
        if white_pieces == black_pieces:
            return None
        return game_state.player_2 if black_pieces > white_pieces else game_state.player_1


def _visit_neighbours(start_nodes, goal_nodes, board_2d, board_width):
    '''Check if the neighbouring nodes (up, down, left, right) are part of a valid path.

    Parameters: start_nodes, the first nodes to check
                goal_nodes, check if goal nodes have been reached
                board_2d, a 2d representation of board in the form of a 2d list
                board_width, an int
    Returns: True if path was found and the colour that owns the path, otherwise false'''
    to_visit = start_nodes
    visited = []
    while to_visit:
        current_node = to_visit.pop(-1)
        visited.append(current_node)

        for x_neighbour in [(current_node[0][0], current_node[0][1] - 1), (current_node[0][0], current_node[0][1] + 1)]:
            if x_neighbour[1] >= board_width or x_neighbour[1] < 0:
                continue

            piece = board_2d[x_neighbour[0]][x_neighbour[1]]

            if piece == current_node[1]:
                if (x_neighbour, piece) in visited or piece.standing:
                    continue
                if x_neighbour in goal_nodes:
                    return True, piece.colour
                to_visit.append((x_neighbour, piece))

        for y_neighbour in [(current_node[0][0] + 1, current_node[0][1]), (current_node[0][0] - 1, current_node[0][1])]:
            if y_neighbour[0] >= board_width or y_neighbour[0] < 0:
                continue

            piece = board_2d[y_neighbour[0]][y_neighbour[1]]

            if piece == current_node[1]:
                if (y_neighbour, piece) in visited or piece.standing:
                    continue
                if y_neighbour in goal_nodes:
                    return True, piece.colour
                to_visit.append((y_neighbour, piece))
    return False, None


def _df_search(board_2d: list, board_width: int):
    '''Search the board for paths from one side to another. 

    Parameters: board_2d, a 2d representation of board in the form of a 2d list
                board_width, an int
    Returns: True if path was found and the colour that owns the path, otherwise false'''
    x_goal = [(board_width - 1, y) for y in range(0, board_width)]
    y_goal = [(x, board_width - 1) for x in range(0, board_width)]

    x_start = [((0, x), board_2d[0][x])
               for x in range(0, board_width) if not board_2d[0][x].standing]
    y_start = [((y, 0), board_2d[y][0])
               for y in range(0, board_width) if not board_2d[y][0].standing]

    win, colour = _visit_neighbours(x_start, x_goal, board_2d, board_width)
    if win:
        return win, colour
    win, colour = _visit_neighbours(y_start, y_goal, board_2d, board_width)
    return win, colour


def check_for_connections(game_state: GameState):
    '''Check for connections between all sides of the board.

    Parameters: a game state containing a board and two players
    Returns: True if there is a connection and the player that owns the connection, otherwise False'''
    row_length = int(sqrt(game_state.board.size))
    board_2d = []
    if not game_state.board.state.keys():
        return False, None

    for row in range(0, game_state.board.size, row_length):
        row_buf = []
        for col in range(1, row_length + 1):
            if game_state.board.state[col + row]:
                row_buf.append(game_state.board.state[col + row][-1])
            else:
                row_buf.append(Piece('pink', True))

        board_2d.append(row_buf)

    path_exists, colour = _df_search(board_2d, row_length)

    path_owner = game_state.current_player
    if game_state.player_1.colour == colour:
        path_owner = game_state.player_1
    elif game_state.player_2.colour == colour:
        path_owner = game_state.player_2

    return path_exists, path_owner


def place_piece(game_state: GameState, board_square: int, is_standing: bool):
    '''Checks is there is a standing piece in the stack then generates a new standing or 
    laying piece belonging the current_player if the player has pieces left, 
    on the specified square on the board. 

    Parameters: game_state: current GameState
                board_square: integer where on board to place piece
                is_standing: Boolean if piece should stand or lay. 
    Returns: True if successfully placed a new piece is generated on the board, else False'''

    # make sure there is not a standing piece at board_square and the player can place piece.
    if not contains_standing_piece(game_state.board, board_square) and can_place_piece(game_state):
        new_piece = generate_piece(game_state.current_player, is_standing)
        game_state.board.state[board_square].append(new_piece)  # place piece

        # update so that the game_state knows that the current player played their piece.
        if game_state.current_player.colour == game_state.player_1.colour:
            # decrease a player's pieces
            player_decrement_pieces(game_state.player_1)
        else:
            player_decrement_pieces(game_state.player_2)
            print(game_state.player_2.pieces)
        return True  # if successfully placed
    else:
        return False  # if failed to place


def alternate_players(game_state: GameState):
    '''Switch the current player with the other player.

    Parameters: a game state containing a board and two players'''
    if game_state.current_player.colour == game_state.player_1.colour:
        game_state.current_player = game_state.player_2
    else:
        game_state.current_player = game_state.player_1


def horizontal_formula(start_pos: int, end_pos: int):
    '''Determines if a potential move is horizontal on the board.
    Parameters: start_pos a value from 1 to 16 and is the square to move from, 
    end_pos a value from 1 to 16 and is the square to move to.
    Returns: True if it is a move horizontally on the board, otherwise False. '''
    
    # board squares needs to be in the format of [0, 15] instead of [1, 16] which is necessary
    # for the formula
    start_index = start_pos-1
    end_index = end_pos-1

    # a move needs to be on the board or if both indicate the same square (not a move)
    if start_index < 0 or start_index > 15:
        return False
    if end_index < 0 or end_index > 15:
        return False
    if start_index == end_index:
        return False

    # check if they are on the same row of the board
    lower_bound = start_index - (start_index % 4)
    upper_bound = start_index + (4 - (start_index % 4))
    if end_index >= lower_bound and end_index < upper_bound:
        return True
    else:
        return False


def vertical_formula(start_pos: int, end_pos: int):
    '''Determines if a potential move is vertical on the board.
    Parameters: start_pos a value from 1 to 16 and is the square to move from, 
    end_pos a value from 1 to 16 and is the square to move to.
    
    Returns: True if it is a move vertically on the board, otherwise False. '''

    # board squares needs to be in the format of [0, 15] instead of [1, 16] which is 
    # necessary for the formula
    start_index = start_pos-1
    end_index = end_pos-1

    # a move needs to be on the board or if both indicate the same square (not a move)
    if start_index < 0 or start_index > 15:
        return False
    if end_index < 0 or end_index > 15:
        return False
    if start_index == end_index:
        return False

    # check if they are on the same row of the board
    if end_index % 4 == start_index % 4:
        return True
    else:
        return False


def check_if_stack_can_move(game_state: GameState, start_pos: int, end_pos: int):
    '''A function that checks if all the squares between start_pos and end_pos
    is moveable

    Parameters: start_pos is the start position of stack, end_pos is the wanted 
    square to move the stack
    Returns: True if the move can be done, else False'''
    row_length = int(sqrt(game_state.board.size))

    if not is_stack_moveable(game_state, start_pos):
        return False

    i = 0
    current_pos = start_pos
    if horizontal_formula(start_pos, end_pos):
        if len(game_state.board.state[start_pos]) <= abs(start_pos - end_pos) - 1:
            return False
        if start_pos-end_pos < 0: # if we move right on the board
            i = 1
            while current_pos < end_pos:  # as long as we have positions between current and end pos
                current_pos = current_pos + i
                # check square to move to
                if contains_standing_piece(game_state.board, current_pos):
                    return False  # if not movable, False
            return True  # if all positions are moveable return True
        else:
            i = -1 # if we move to the left on the board
            while current_pos > end_pos: # flipped sign since we move left
                current_pos = current_pos + i
                if contains_standing_piece(game_state.board, current_pos):
                    return False
            return True

    elif vertical_formula(start_pos, end_pos):
        if len(game_state.board.state[start_pos]) <= (abs(start_pos - end_pos) // row_length) - row_length:
            return False
        if start_pos-end_pos < 0: # if we move down on the board
            i = 4 # i = 4 since up and down one square is 4 positions on the board
            while current_pos < end_pos: # as long as we have positions between current and end pos
                current_pos = current_pos + i
                # check square to move to
                if contains_standing_piece(game_state.board, current_pos):
                    return False  # if not movable, False
            return True  # if all positions are moveable return True
        else:
            i = -4 # if we move up on the board
            while current_pos > end_pos: # flipped sign since we move right
                current_pos = current_pos + i
                if contains_standing_piece(game_state.board, current_pos):
                    return False
            return True
    else:
        return False


def move_stack(game_state: GameState, start_position: int, destination: int, pieces_moved: list):
    '''Move a stack from a given position to another given position. For every square moved, leave behind a specified number of pieces.
    At least one piece must be placed on every square passed except the start position.

    Ex. For moving a stack containing 5 pieces 3 steps to the right, pieces_moved can be for example [1, 2, 1, 1] or [0, 1, 2, 1].
    Only the start position can be given 0 (leave 0 pieces on the start position.)

    Parameters: a game state
                the position of the stack you want to move
                the position where you want the stack to be moved
                a list of how many pieces should be placed on each square
    Returns: True if the stack is moved successfully, otherwise False'''
    if not check_if_stack_can_move(game_state, start_position, destination):
        return False

    row_length = int(sqrt(game_state.board.size))
    stack_size = len(game_state.board.state[start_position])
    distance = destination - start_position
    direction = distance // abs(distance)
    start_stack = deepcopy(game_state.board.state[start_position])

    if abs(distance) < row_length:
        path = range(start_position, destination + direction, direction)
    else:
        path = range(start_position, destination + direction * row_length,
                     direction * row_length)

    if pieces_moved == []:
        pieces_moved = (len(path) - 1) * [1] + \
            [len(start_stack) - (len(path) - 1)]

    if len(pieces_moved) != len(path) or sum(pieces_moved) != stack_size or any(map(lambda x: x == 0, pieces_moved[1:])):
        return False

    game_state.board.state[start_position] = []
    for square, pieces_left_behind in zip(path, pieces_moved):
        bottom_pieces = []
        for _ in range(1, pieces_left_behind + 1):
            bottom_pieces.append(start_stack.pop(0))
        game_state.board.state[square] += bottom_pieces

    if start_stack != []:
        game_state.board.state[destination] += start_stack

    return True
