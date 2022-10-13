import os
import __init__
import math
from board_functions import is_colour_in_square
from classes import Board, GameState, Player


def pad_low_num(num):
    '''Pad numbers smaller than 10 (so all numbers take up the same amount of space)'''
    if num > 9:
        return str(num)
    else:
        return str(num) + ' '


def shorten_colour(colour):
    '''Convert black or white to the letter B or W

    Parameters: a colour written as a string
    Returns: B or W depending on the colour given'''
    if colour == 'black':
        return 'B'
    elif colour == 'white':
        return 'W'


def colour_str(board, square, colour):
    '''Convert colour on top and in a stack to string form.

    Parameters: a colour written as a string
    Returns: B or W, or B (W) or W (B)'''
    other_colour = ''
    ans_str = ''

    if colour == 'black':
        other_colour = 'white'
    elif colour == 'white':
        other_colour = 'black'

    if is_colour_in_square(board, square, other_colour):
        ans_str += f'  {shorten_colour(colour)} ({shorten_colour(other_colour)})   '
    else:
        ans_str += f'    {shorten_colour(colour)}     '
    return ans_str


def standing_str(is_standing):
    '''Convert the standing status of a piece to string'''
    if is_standing is None:
        return "        "
    return "Standing" if is_standing else " Lying  "


def draw_square(num_pieces, colour, orientation):
    '''Draw one square'''
    return [f" Stack: {pad_low_num(num_pieces)}|",
            f"{colour}|",
            f" {standing_str(orientation)} |",
            f"----------+"]


def draw_row(board, row_stacks, row_sizes, row_pieces):
    '''Draw a row of the board'''
    buf = ["|", "|", "|", "+"]

    for pos, size, piece in zip(row_stacks, row_sizes, row_pieces):
        square = draw_square(
            size, colour_str(board, pos, piece.colour), piece.standing) if piece is not None else draw_square(size, "          ", None)
        for i in range(len(buf)):
            buf[i] += square[i]

    return '\n'.join(buf) + '\n'


def draw_top(num_column):
    '''Draw the top line of the board'''
    return "+" + "----------+" * num_column + "\n"


def board_to_str(board: Board):
    '''Show the current board state as a string

    Parameters: a board
    Returns: the board represented as a string'''
    stack_sizes = [0] * board.size
    stack_content = [None] * board.size
    stack_pos = list(range(1, board.size + 1))

    num_row = int(math.sqrt(board.size))
    occupied_squares = board.state.keys()
    stacks = [(pos, board.state[pos]) for pos in occupied_squares]
    for stack in stacks:
        if stack[1]:
            stack_pos[stack[0] - 1] = stack[0]
            stack_sizes[stack[0] - 1] = len(stack[1])
            stack_content[stack[0] - 1] = stack[1][-1]

    board_str = draw_top(num_row)

    for i in range(num_row):
        board_str += draw_row(board,
                              stack_pos[num_row*i: num_row*(i+1)],
                              stack_sizes[num_row*i:num_row*(i+1)],
                              stack_content[num_row*i:num_row*(i+1)])

    return board_str


def players_to_str(player1: Player, player2: Player):
    '''Show the number of pieces that both players has.

    Parameters: a player
                a player
    Returns: A string representation of how many pieces each player has left'''
    return f'''{player1.name:<25}{player2.name:<25}
{'Colour: ' + player1.colour:<25}{'Colour: ' + player2.colour:<25}
{'Pieces remaining: ' + str(player1.pieces):<25}{'Pieces remaining: ' + str(player2.pieces):<25}
'''


def game_state_to_str(game_state: GameState):
    '''Show the current game state.

    Parameters: a game state
    Returns: game state as string'''
    game_state_str = ''
    game_state_str += board_to_str(game_state.board)
    game_state_str += '\n'
    game_state_str += players_to_str(game_state.player_1, game_state.player_2)

    return game_state_str


def print_game_state(game_state: GameState):
    '''Clear terminal and print the game state.

    Parameters: a game state'''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(game_state_to_str(game_state))


def stack_to_str(game_state: GameState, square: int):
    stack = game_state.board.state[square]
    if not stack:
        return None
    stack = list(map(str, stack))
    return stack
