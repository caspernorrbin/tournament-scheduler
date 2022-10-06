import unittest
import __init__
import random

from classes import GameState, Piece
from visualisation import board_to_str, game_state_to_str, players_to_str


class VisualisationTestCase(unittest.TestCase):
    '''Test the board'''

    def setUp(self):
        '''Create a board before running tests (is run before every test)'''
        random.seed(42)
        self.game_state = GameState()
        self.maxDiff = None

    def test_show_empty_board(self):
        '''Test the conversion of an empty board to a string representation'''
        correct_string = '''+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
'''
        self.assertEqual(board_to_str(self.game_state.board), correct_string,
                         'The empty board is not converted to string properly.')

    def test_show_board_with_pieces(self):
        '''Test the conversion of an empty board to a string representation'''
        correct_string = '''+----------+----------+----------+----------+
| Stack: 1 | Stack: 0 | Stack: 0 | Stack: 0 |
|    B     |          |          |          |
|  Lying   |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
'''
        self.game_state.board.state[1].append(Piece('black', False))
        self.assertEqual(board_to_str(self.game_state.board), correct_string,
                         'The board with one piece is not converted to string properly.')

        correct_string1 = '''+----------+----------+----------+----------+
| Stack: 3 | Stack: 0 | Stack: 0 | Stack: 0 |
|  B (W)   |          |          |          |
|  Lying   |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
'''
        self.game_state.board.state[1].append(Piece('white', False))
        self.game_state.board.state[1].append(Piece('black', False))
        self.assertEqual(board_to_str(self.game_state.board), correct_string1,
                         'The board with one piece is not converted to string properly.')

    def test_show_players(self):
        correct_str = '''Player 1                 Player 2: 
Colour: black            Colour: white
Pieces remaining: 15     Pieces remaining: 15
'''
        self.assertEqual(players_to_str(self.game_state.player_1,
                         self.game_state.player_2), correct_str)

    def test_show_game_state(self):
        correct_string = '''+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+
| Stack: 0 | Stack: 0 | Stack: 0 | Stack: 0 |
|          |          |          |          |
|          |          |          |          |
+----------+----------+----------+----------+

Player 1                 Player 2: 
Colour: black            Colour: white
Pieces remaining: 15     Pieces remaining: 15
'''
        self.assertEqual(game_state_to_str(self.game_state), correct_string)


if __name__ == '__main__':
    unittest.main()
