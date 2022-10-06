import unittest
import __init__
import random
from classes import Piece, Player, GameState
from board_functions import contains_standing_piece, is_board_full, count_all_pieces, count_topmost_lying_pieces, is_stack_moveable, is_colour_in_square, convert_input_to_square, is_destination_valid


class BoardTestCase(unittest.TestCase):
    '''Test the board functions'''

    def setUp(self):
        '''Create a board, two players and one of each piece type before running tests (is run before every test)'''
        random.seed(42)
        self.game_state = GameState()
        self.game_state.player_2 = Player('black', 1)
        self.white_piece_standing = Piece('white', True)
        self.white_piece_laying = Piece('white', False)
        self.black_piece_standing = Piece('black', True)
        self.black_piece_laying = Piece('black', False)

    def test_is_board_full(self):
        '''Test checking if the board is full

        Check empty board, half-full board and full board'''
        self.assertFalse(is_board_full(self.game_state.board))
        for square in range(1, self.game_state.board.size // 2 + 1):
            self.game_state.board.state[square].append(Piece('black', False))

        self.assertFalse(is_board_full(self.game_state.board))
        for square in range(1, self.game_state.board.size + 1):
            self.game_state.board.state[square].append(Piece('black', False))
        self.assertTrue(is_board_full(self.game_state.board))

    def test_count_pieces(self):
        '''Test counting the pieces on the game board.

        Place three pieces of different colours on the board and count the pieces after placing a piece.'''
        self.game_state.board.state[1].append(self.white_piece_laying)
        self.assertEqual(count_all_pieces(self.game_state.board),
                         (1, 0, 1), 'Failed to count one white piece')

        self.game_state.board.state[2].append(self.white_piece_laying)
        self.assertEqual(count_all_pieces(self.game_state.board),
                         (2, 0, 2), 'Failed to count two white pieces')

        self.game_state.board.state[3].append(self.black_piece_laying)
        self.assertEqual(count_all_pieces(self.game_state.board), (2, 1, 3),
                         'Failed to count two white pieces and one black piece')

    def test_count_topmost_lying_pieces(self):
        '''Test counting the topmost lying pieces on the game board.

        Test base case (one piece), skip non-topmost pieces, one of each colour and skip standing pieces
        '''
        self.game_state.board.state[1].append(self.white_piece_laying)
        self.assertEqual(count_topmost_lying_pieces(
            self.game_state.board), (1, 0), 'Failed to count one white lying piece')

        self.game_state.board.state[1].append(self.white_piece_laying)
        self.assertEqual(count_topmost_lying_pieces(
            self.game_state.board), (1, 0), 'Failed to not count a non-topmost piece')

        self.game_state.board.state[2].append(self.black_piece_laying)
        self.assertEqual(count_topmost_lying_pieces(self.game_state.board),
                         (1, 1), 'Failed to count one white and one black lying piece')

        self.game_state.board.state[3].append(self.white_piece_standing)
        self.assertEqual(count_topmost_lying_pieces(
            self.game_state.board), (1, 1), 'Failed to not count a standing piece')

    def test_is_colour_in_square(self):
        '''Test checking if a certain colour is in a stack on a certain square.

        Check empty board, one black piece on each square, one white/black piece.
        '''
        self.assertFalse(is_colour_in_square(
            self.game_state.board, 1, 'black'))
        self.assertFalse(is_colour_in_square(
            self.game_state.board, 1, 'white'))
        for square in range(1, self.game_state.board.size + 1):
            self.game_state.board.state[square].append(Piece('black', False))
            self.assertTrue(is_colour_in_square(
                self.game_state.board, square, 'black'))
            self.assertFalse(is_colour_in_square(
                self.game_state.board, 1, 'white'))
        self.game_state.board.state[1].append(Piece('white', False))
        self.assertTrue(is_colour_in_square(self.game_state.board, 1, 'white'))
        self.assertTrue(is_colour_in_square(self.game_state.board, 1, 'black'))

    def test_contains_standing_piece(self):
        '''Test if a stack moveable or not'''
        ''' The square to check if it contains a standing piece'''
        square = 1

        '''First test when no piece is standing'''
        self.game_state.board.state[square].append(Piece('black', False))
        self.game_state.board.state[square].append(Piece('black', False))
        self.game_state.board.state[square].append(Piece('black', False))
        self.assertFalse(contains_standing_piece(
            self.game_state.board, square))

        '''Then test when one piece is standing'''
        self.game_state.board.state[square].append(Piece('black', True))
        self.assertTrue(contains_standing_piece(self.game_state.board, square))

    def test_is_stack_moveable(self):
        '''Test if a stack is moveable or not'''
        '''The square to check if its moveable'''
        square = 1

        '''First test when no piece is standing - should be moveable'''
        self.game_state.board.state[square].append(Piece('black', False))
        self.game_state.board.state[square].append(Piece('black', False))
        self.game_state.board.state[square].append(Piece('black', False))
        self.assertTrue(is_stack_moveable(self.game_state, square))

        '''Then test when one piece is standing - should not be moveable'''
        self.game_state.board.state[square].append(Piece('black', True))
        self.assertFalse(is_stack_moveable(self.game_state, square))

    def test_is_destination_valid(self):
        board = self.game_state.board
        valid, msg = is_destination_valid(board, 4, 4)
        self.assertTrue(valid)
        self.game_state.board.state[16].append(Piece('black', True))
        valid, msg = is_destination_valid(board, 4, 4)
        self.assertFalse(valid)
        valid, msg = is_destination_valid(board, 6, 3)
        self.assertFalse(valid)
        valid, msg = is_destination_valid(board, 2, 8)
        self.assertFalse(valid)
        valid, msg = is_destination_valid(board, 8, 8)
        self.assertFalse(valid)

    def test_convert_input_to_square(self):
        square = convert_input_to_square(4, 4)
        self.assertTrue(square == 16)
        square = convert_input_to_square(1, 1)
        self.assertTrue(square == 1)
        square = convert_input_to_square(1, 2)
        self.assertTrue(square == 2)
        square = convert_input_to_square(1, 3)
        self.assertTrue(square == 3)
        square = convert_input_to_square(1, 4)
        self.assertTrue(square == 4)
        square = convert_input_to_square(2, 1)
        self.assertTrue(square == 5)
        square = convert_input_to_square(2, 2)
        self.assertTrue(square == 6)
        square = convert_input_to_square(4, 3)
        self.assertTrue(square == 15)
        square = convert_input_to_square(3, 2)
        self.assertTrue(square == 10)


if __name__ == '__main__':
    unittest.main()
