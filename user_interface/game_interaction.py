import __init__
import os
from classes import GameState
from rules_functions import check_if_stack_can_move, determine_winner, can_place_piece, alternate_players, place_piece, check_for_connections, move_stack
from menus import print_rules, print_toolbar
from board_functions import convert_input_to_square, is_destination_valid, is_stack_moveable
from visualisation import print_game_state


def start_game(name1, name2):
    ''' Starts the game loop '''
    return game_loop(GameState(name1, name2))


def toolbar_answer():
    '''
    Will print the toolbar and will return valid input
    This will loop until a valid input is entered

    Returns: Returns the valid input from user  
    '''
    while True:
        print_toolbar()
        answer = input().lower()
        if answer == "p" or answer == "m" or answer == "r" or answer == "q":
            return answer
        else:
            print('Invalid input. Press enter to try again, \'R/r\' to return')
            inp = input().lower()
            if inp == 'r':
                break
            else:
                continue


def choose_coordinate(board, str):
    ''' Will receive input from terminal and will only return if input is a number between 0-15
        otherwise it will loops until valid input is read 

        Parameters: board   - A representation of the game board  
                    str     - The question to be asked
        Return: Returns a valid square, represented in an internal way
        '''
    while True:
        print(f"{str} Please choose which square (row column)\n> ", end="")
        try:
            row, col = input().split()
            row, col = int(row), int(col)
        except:
            print('Please input a valid coordinate in the form of \'row column\'.')
            print('Press enter to try again, \'R/r\' to return')
            inp = input().lower()
            if inp == 'r':
                return
            else:
                continue

        valid, msg = is_destination_valid(board, row, col)
        if valid:
            square = convert_input_to_square(row, col)
            return square
        else:
            print(msg)
            continue


def put_piece(state_of_game: GameState):
    ''' Will place a piece on the board, decrement the number of pieces for that player
        and change the active player.

    Parameters: a game state containing a board and two players
    Returns:    True    - If the coordinate is valid
                False   - If the coordinate isn't valid
    '''
    standing = False

    while True:
        square = choose_coordinate(state_of_game.board, "Place a piece.")
        if square is not None:
            print(
                "Place the piece [s]tanding or [l]ying down? (Default: lying down)\n> ", end="")
            answer = input().lower()
            if answer == "s":
                standing = True

            success = place_piece(state_of_game, square, standing)
            if success == False:
                print("Cannot place a piece on square '",
                      square, "'.\nThere is a standing piece.")
                print('Press enter to try again, \'R/r\' to return')
                inp = input().lower()
                if inp == 'r':
                    return False
                else:
                    continue
            else:
                alternate_players(state_of_game)
                return True
        else:
            return False


def move_a_stack(state_of_game: GameState):
    ''' Will move a stack from one square to another, leaving pieces on every square on the way

        Parameters: state_of_game - is the state of the game
    '''
    while True:
        start = choose_coordinate(
            state_of_game.board, "Which stack do you want to move?")
        if start is None:
            break

        if not is_stack_moveable(state_of_game, start):
            print('You are not allowed to move this stack.')
            print('Press enter to try again, \'R/r\' to return')
            inp = input().lower()
            if inp == 'r':
                break
            else:
                continue
        else:
            end = choose_coordinate(
                state_of_game.board, "Where to place the stack.")
            if end is None:
                break
            if not check_if_stack_can_move(state_of_game, start, end):
                print('Illegal move. Press enter to try again, \'R/r\' to return')
                inp = input().lower()
                if inp == 'r':
                    break
                else:
                    continue

            while True:
                print(
                    'How many pieces do you want to leave behind in each step (comma separated, ex. 1, 2)?')
                print(
                    'Default: Leave one piece on each square. The remainder is left at the destination.')
                inp = input().replace(' ', '')
                if inp == '':
                    pieces_to_leave = []
                    break
                else:
                    try:
                        inp = inp.split(',')
                        pieces_to_leave = list(map(int, inp))
                        if move_stack(state_of_game, start, end, pieces_to_leave):
                            alternate_players(state_of_game)
                            break
                        else:
                            print(
                                'Invalid move. Press enter to try again, \'R/r\' to return')
                            inp = input().lower()
                            if inp == 'r':
                                break
                            else:
                                continue
                    except:
                        print(
                            'Invalid input. Press enter to try again, \'R/r\' to return')
                        inp = input().lower()
                        if inp == 'r':
                            break
            break


def first_put(state_of_game: GameState):
    ''' The first move of the game, where each player will put one piece of there opponets colour on the board

        Parameters: state_of_game is the internal representation of the game state
    '''
    alternate_players(state_of_game)

    done = False
    while not done:
        print_game_state(state_of_game)
        print(f"{state_of_game.player_2.name} who is playing black starts by placing one white piece.")
        done = put_piece(state_of_game)

    done = False
    while not done:
        print_game_state(state_of_game)
        print(f"{state_of_game.player_1.name} who is playing white starts by placing one black piece.")
        done = put_piece(state_of_game)

    alternate_players(state_of_game)


def game_loop(state_of_game: GameState):
    ''' This is where the magic happens
        The game loop, will loop until the current game has either ended or a player has resigned

        Parameters: state_of_game is the internal representation of the game state
    '''
    first_put(state_of_game)

    player_won = False
    winner = None

    while can_place_piece(state_of_game) and player_won == False:
        print_game_state(state_of_game)

        if state_of_game.current_player.colour == state_of_game.player_1.colour:
            print(f"It's {state_of_game.player_1.name}'s turn")
        else:
            print(f"It's {state_of_game.player_2.name}'s turn")

        answer = toolbar_answer()
        if answer == "p":
            put_piece(state_of_game)
        elif answer == "m":
            move_a_stack(state_of_game)
        elif answer == "r":
            print_rules()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            if state_of_game.current_player.colour == state_of_game.player_1.colour:
                print("The winner, by resignation, is player 2 (",
                      state_of_game.player_2.colour, ")")
                return 2
            else:
                print("The winner, by resignation, is player 1 (",
                      state_of_game.player_1.colour, ")")
                return 1
            return
        player_won, winner = check_for_connections(state_of_game)

    os.system('cls' if os.name == 'nt' else 'clear')
    if not player_won:
        winner = determine_winner(state_of_game)
        if winner == None:
            print(
                f"The players have an equal amount of points but as it is player {state_of_game.current_player.colour}'s turn, they win!")
            if state_of_game.current_player.colour == 'black':
                return 2
            else:
                return 1
        elif winner.colour == state_of_game.player_1.colour:
            print("The winner, by majority, is player 1 (",
                  state_of_game.player_1.colour, ")")
            return 1
        else:
            print("The winner, by majority, is player 2 (",
                  state_of_game.player_2.colour, ")")
            return 2
    else:
        print_game_state(state_of_game)
        if winner.colour == state_of_game.player_1.colour:
            print("The winner, by connection, is player 1 (",
                  state_of_game.player_1.colour, ")")
            return 1
        else:
            print("The winner, by connection, is player 2 (",
                  state_of_game.player_2.colour, ")")
            return 2
