from turtle import clear
import unittest
import __init__
import random
from classes import GameState, Piece
from player_functions import is_out_of_pieces, player_pieces_left
from rules_functions import can_place_piece, determine_winner, move_stack, place_piece, alternate_players, vertical_formula, horizontal_formula, check_if_stack_can_move, check_for_connections


class GameRulesTestCase(unittest.TestCase):
    '''Test the game rules functions'''

    def setUp(self):
        '''Create a board and two players (randomise their colours and who to start) before running tests (is run before every test)'''
        random.seed(42)
        self.game_state = GameState()

    def test_can_place_piece_empty_board(self):
        '''Test checking if a piece can be placed on an empty board.'''
        self.assertTrue(can_place_piece(self.game_state))

    def test_can_place_piece_no_pieces(self):
        '''Test checking if a piece can be placed when one player doesn't have any pieces.'''
        self.game_state.player_2.pieces = 0
        self.assertFalse(can_place_piece(self.game_state))

    def test_can_place_piece_full_board(self):
        '''Test checking if a piece can be placed when all squares on the board are taken by standing pieces.'''
        for square in range(1, self.game_state.board.size + 1):
            self.game_state.board.state[square].append(Piece('black', False))
        self.assertFalse(can_place_piece(self.game_state))

    def test_determine_winner(self):
        '''Test determine white and black player as winner and the draw scenario.'''
        for square in range(1, self.game_state.board.size):
            self.game_state.board.state[square].append(Piece('black', False))
        self.game_state.player_2.pieces = 0
        self.assertEqual(determine_winner(self.game_state),
                         self.game_state.player_2)

        for square in range(1, self.game_state.board.size):
            self.game_state.board.state[square].append(Piece('white', False))
        self.game_state.player_1.pieces = 0
        self.assertEqual(determine_winner(self.game_state),
                         self.game_state.player_1)

        for square in range(1, self.game_state.board.size + 1):
            self.game_state.board.state[square].append(Piece('white', True))
        self.assertEqual(determine_winner(self.game_state), None)

    def test_place_piece_standing(self):
        '''Test place a piece of the current player on the board.

        Checks if the Player can place a Piece on a square. (Not a standing 
        piece on the square and the player has a piece left to play)'''
        # square to put piece on
        square = 1
        self.game_state.player_2.pieces = 1
        self.game_state.current_player = self.game_state.player_2

        # place the last piece of player_2
        self.assertTrue(place_piece(self.game_state, square, False))

        # check that a piece has been placed on square and player_2 has no pieces left
        self.assertTrue(is_out_of_pieces(self.game_state.player_2))

        # check if the piece is correctly in the board
        self.assertEqual(
            self.game_state.board.state[square][0].colour, self.game_state.player_2.colour)
        self.assertEqual(
            self.game_state.board.state[square][0].standing, False)

        # check a player with no pieces can not place piece.
        self.assertFalse(place_piece(self.game_state, square, False))

        # other player can place pieces on square
        self.game_state.current_player = self.game_state.player_1

        # give player 2 pieces so player 1 can place pieces
        self.game_state.player_2.pieces = 15

        self.assertTrue(place_piece(self.game_state, square, False))
        self.assertTrue(place_piece(self.game_state, square, True))

        # these new pieces get put in stack correctly.
        self.assertEqual(
            self.game_state.board.state[square][1].colour, self.game_state.player_1.colour)
        self.assertEqual(
            self.game_state.board.state[square][1].standing, False)
        self.assertEqual(
            self.game_state.board.state[square][2].colour, self.game_state.player_1.colour)
        self.assertEqual(self.game_state.board.state[square][2].standing, True)

        # two pieces has been placed by player_1
        self.assertEqual(player_pieces_left(self.game_state.player_1), 13)

        # player_1 can not place piece on a standing piece
        self.assertFalse(place_piece(self.game_state, square, False))
        self.assertFalse(place_piece(self.game_state, square, True))

        # player_1 has not changed the amount of pieces since they did not place any new pieces on board
        self.assertEqual(player_pieces_left(self.game_state.player_1), 13)

    def test_alternate_players(self):
        '''Test if current player is player 1 then it should switch to player 2 and vise versa.'''
        alternate_players(self.game_state)
        self.assertEqual(self.game_state.current_player,
                         self.game_state.player_2)
        alternate_players(self.game_state)
        self.assertEqual(self.game_state.current_player,
                         self.game_state.player_1)

    def test_check_connections(self):
        '''Test checking for connections in straight lines.

        Test rows, columns and edge cases.'''
        win, _ = check_for_connections(self.game_state)
        self.assertFalse(win)
        self.setUp()

        for square in range(1, 5):
            self.game_state.board.state[square].append(Piece('black', False))

        win, player = check_for_connections(self.game_state)
        self.assertTrue(win)
        self.assertEqual(player.colour, 'black')
        self.setUp()

        for square in [1, 5, 9, 13]:
            self.game_state.board.state[square].append(Piece('black', False))

        win, player = check_for_connections(self.game_state)
        self.assertTrue(win)
        self.assertEqual(player.colour, 'black')
        self.setUp()

        for square in [1, 3, 5, 10]:
            self.game_state.board.state[square].append(Piece('black', False))
        win, _ = check_for_connections(self.game_state)
        self.assertFalse(win)

        for square in [2, 6, 8, 12]:
            self.game_state.board.state[square].append(Piece('white', False))
        win, _ = check_for_connections(self.game_state)
        self.assertFalse(win)
        self.setUp()

        for square in [2, 6, 8, 12]:
            self.game_state.board.state[square].append(Piece('white', False))
        self.game_state.board.state[2].append(Piece('white', True))
        win, _ = check_for_connections(self.game_state)
        self.assertFalse(win)
        self.setUp()

        for square in [1, 3]:
            self.game_state.board.state[square].append(Piece('white', False))
            self.game_state.board.state[square +
                                        1].append(Piece('black', False))
        win, _ = check_for_connections(self.game_state)
        self.assertFalse(win)

    def test_vertical_formula(self):
        '''Tests different start and end positions to be sure that the move is vertical'''
        out_of_bounds_1 = 0
        out_of_bounds_2 = 17
        pos_1 = 1
        pos_2 = 2
        pos_5 = 5
        pos_13 = 13
        pos_4 = 4
        pos_16 = 16

        # Test out of bounds and same square
        self.assertFalse(vertical_formula(pos_1, pos_1))
        self.assertFalse(vertical_formula(pos_1, out_of_bounds_2))
        self.assertFalse(vertical_formula(pos_16, out_of_bounds_1))

        # Test one horizontal move and three different vertical moves, up and down movement.
        self.assertFalse(vertical_formula(pos_1, pos_2))
        self.assertTrue(vertical_formula(pos_1, pos_5))
        self.assertTrue(vertical_formula(pos_13, pos_1))
        self.assertTrue(vertical_formula(pos_4, pos_16))

    def test_horizontal_formula(self):
        '''Tests different start and end positions to be sure that the move is horizontal'''
        out_of_bounds_1 = 0
        out_of_bounds_2 = 17
        pos_1 = 1
        pos_2 = 2
        pos_4 = 4
        pos_12 = 12
        pos_5 = 5
        pos_8 = 8
        pos_13 = 13
        pos_4 = 4
        pos_16 = 16

        # Test out of bounds and same square
        self.assertFalse(horizontal_formula(pos_1, pos_1))
        self.assertFalse(horizontal_formula(pos_1, out_of_bounds_2))
        self.assertFalse(horizontal_formula(pos_16, out_of_bounds_1))

        # Tests to make sure the function returns the right rows
        self.assertFalse(horizontal_formula(pos_1, pos_16))
        self.assertFalse(horizontal_formula(pos_16, pos_1))
        self.assertFalse(horizontal_formula(pos_1, pos_5))
        self.assertFalse(horizontal_formula(pos_4, pos_5))
        self.assertFalse(horizontal_formula(pos_13, pos_12))
        
        self.assertTrue(horizontal_formula(pos_1, pos_2))
        self.assertTrue(horizontal_formula(pos_1, pos_4))
        self.assertTrue(horizontal_formula(pos_4, pos_1))
        self.assertTrue(horizontal_formula(pos_5, pos_8))
        self.assertTrue(horizontal_formula(pos_16, pos_13))

    def test_check_if_stack_can_move(self):
        '''A test to see if a stack is able to be moved, 
        checks if the stack to move does not have a standing piece
        and that it does not move into/onto a stack with a standing piece'''

        start_pos = 3
        end_pos12 = 12
        end_pos16 = 16
        end_pos15 = 15
        end_pos5 = 5
        end_pos4 = 4
        end_pos1 = 1
        end_pos11 = 11

        # Horisontal:
        # empty board can't move stack
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, start_pos))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, end_pos1))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, end_pos15))

        # place pieces and check that the stack can move
        self.game_state.board.state[start_pos].append(Piece('black', False))
        self.game_state.board.state[start_pos].append(Piece('white', False))
        self.game_state.board.state[start_pos].append(Piece('black', False))
        self.game_state.board.state[start_pos].append(Piece('white', False))

        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos, end_pos1))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, start_pos))

        # check out of bounds move:
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, 0))

        # place laying piece in the way of the path of the stack and check it still works
        self.game_state.board.state[start_pos-1].append(Piece('white', False))
        self.game_state.board.state[start_pos-2].append(Piece('black', False))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos, end_pos1))

        # place a standing piece in the way and you can't move over it
        self.game_state.board.state[start_pos-1].append(Piece('black', True))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, end_pos1))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos, end_pos4))
        # still does not connect rows..
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, end_pos5))

        # Vertical:
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos, end_pos15))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos, end_pos11))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, start_pos))

        # laying piece in the way
        self.game_state.board.state[start_pos+4].append(Piece('black', False))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos, end_pos15))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos, end_pos11))

        # place standing piece in the way
        self.game_state.board.state[start_pos+4].append(Piece('black', True))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, end_pos15))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos, end_pos11))

        # start from start_pos+4 which has a standing piece on it..
        start_pos_plus_4 = start_pos+4
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos_plus_4, end_pos15))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos_plus_4, end_pos11))
        # horizontal also:
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos_plus_4, end_pos5))

        # start from new square
        start_pos2 = 13
        self.game_state.board.state[start_pos2].append(Piece('black', False))
        self.game_state.board.state[start_pos2].append(Piece('black', False))
        self.game_state.board.state[start_pos2].append(Piece('black', False))
        self.game_state.board.state[start_pos2].append(Piece('black', False))

        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos2, end_pos15))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos2, end_pos16))
        self.assertTrue(check_if_stack_can_move(
            self.game_state, start_pos2, end_pos1))

        # place standing pieces in the way of the move of stack
        self.game_state.board.state[start_pos2-8].append(Piece('black', True))
        self.game_state.board.state[start_pos2+2].append(Piece('black', True))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos2, end_pos15))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos2, end_pos16))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos2, end_pos1))
        self.assertFalse(check_if_stack_can_move(
            self.game_state, start_pos2, end_pos12))

    def test_move_stack(self):
        bottom_piece = Piece('black', False)
        middle_piece = Piece('white', False)
        top_piece = Piece('black', False)

        self.game_state.board.state[1].append(bottom_piece)
        self.game_state.board.state[1].append(bottom_piece)
        self.game_state.board.state[1].append(middle_piece)
        self.game_state.board.state[1].append(top_piece)
        
        self.assertTrue(move_stack(self.game_state, 1, 4, []))
        self.setUp()

        # horisontal
        self.game_state.board.state[1].append(bottom_piece)
        self.game_state.board.state[1].append(middle_piece)
        self.game_state.board.state[1].append(top_piece)

        # move a 3-stack 3 steps horisontally
        self.assertFalse(move_stack(self.game_state, 1, 4, [1, 0, 1, 1]))
        self.assertTrue(move_stack(self.game_state, 1, 4, [0, 1, 1, 1]))

        self.assertEqual(self.game_state.board.state[1], [])
        self.assertEqual(self.game_state.board.state[2], [bottom_piece])
        self.assertEqual(self.game_state.board.state[3], [middle_piece])
        self.assertEqual(self.game_state.board.state[4], [top_piece])
        self.setUp()

        # vertical
        self.game_state.board.state[4].append(bottom_piece)
        self.game_state.board.state[4].append(middle_piece)
        self.game_state.board.state[4].append(top_piece)

        # move stack 3 steps vertically
        self.assertTrue(move_stack(self.game_state, 4, 12, [0, 1, 2]))
        
        self.assertEqual(self.game_state.board.state[4], [])
        self.assertEqual(self.game_state.board.state[8], [bottom_piece])
        self.assertEqual(self.game_state.board.state[12], [middle_piece, top_piece])
        self.setUp()

        # Test choosing different amounts of pieces left behind
        self.game_state.board.state[4].append(bottom_piece)
        self.game_state.board.state[4].append(middle_piece)
        self.game_state.board.state[4].append(top_piece)
        self.game_state.board.state[4].append(bottom_piece)
        self.game_state.board.state[4].append(middle_piece)
        self.game_state.board.state[4].append(top_piece)

        # move stack 3 steps vertically
        self.assertFalse(move_stack(self.game_state, 4, 12, [6, 9, 9, 9]))
        self.assertFalse(move_stack(self.game_state, 4, 12, [2, 3, 3]))
        self.assertTrue(move_stack(self.game_state, 4, 12, [2, 3, 1]))

        self.assertEqual(self.game_state.board.state[4], [bottom_piece, middle_piece])
        self.assertEqual(self.game_state.board.state[8], [top_piece, bottom_piece, middle_piece])
        self.assertEqual(self.game_state.board.state[12], [top_piece])
        self.setUp()

        # vertical
        self.game_state.board.state[12].append(bottom_piece)
        self.game_state.board.state[12].append(middle_piece)
        self.game_state.board.state[12].append(top_piece)

        # move stack 2 steps vertically (up)
        self.assertTrue(move_stack(self.game_state, 12, 4, [0, 1, 2]))
        
        self.assertEqual(self.game_state.board.state[12], [])
        self.assertEqual(self.game_state.board.state[8], [bottom_piece])
        self.assertEqual(self.game_state.board.state[4], [middle_piece, top_piece])
        self.setUp()

        # Test choosing different amounts of pieces left behind
        self.game_state.board.state[16].append(bottom_piece)
        self.game_state.board.state[16].append(middle_piece)
        self.game_state.board.state[16].append(top_piece)
        self.game_state.board.state[16].append(bottom_piece)
        self.game_state.board.state[16].append(middle_piece)
        self.game_state.board.state[16].append(top_piece)

        # move stack 3 steps vertically (left)
        self.assertFalse(move_stack(self.game_state, 16, 13, [6, 9, 9, 9]))
        self.assertFalse(move_stack(self.game_state, 16, 13, [6]))
        self.assertTrue(move_stack(self.game_state, 16, 13, [0, 3, 1, 2]))

        self.assertEqual(self.game_state.board.state[16], [])
        self.assertEqual(self.game_state.board.state[15], [bottom_piece, middle_piece, top_piece])
        self.assertEqual(self.game_state.board.state[14], [bottom_piece])
        self.assertEqual(self.game_state.board.state[13], [middle_piece, top_piece])
        self.setUp()

        self.game_state.board.state[16].append(bottom_piece)
        self.assertTrue(move_stack(self.game_state, 16, 15, [0, 1]))
        self.setUp()

        self.game_state.board.state[16].append(bottom_piece)
        self.game_state.board.state[16].append(middle_piece)
        self.game_state.board.state[16].append(top_piece)
        self.game_state.board.state[16].append(bottom_piece)
        self.game_state.board.state[16].append(middle_piece)
        self.game_state.board.state[16].append(top_piece)

        self.assertTrue(move_stack(self.game_state, 16, 4, []))
        self.assertEqual(self.game_state.board.state[16], [bottom_piece])
        self.assertEqual(self.game_state.board.state[12], [middle_piece])
        self.assertEqual(self.game_state.board.state[8], [top_piece])
        self.assertEqual(self.game_state.board.state[4], [bottom_piece, middle_piece, top_piece])


if __name__ == '__main__':
    unittest.main()
