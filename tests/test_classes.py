import unittest
import __init__
import random
from classes import Board, Piece, Player, GameState


class BoardTestCase(unittest.TestCase):
    '''Test the board class'''

    def setUp(self):
        '''Create a board before running tests (is run before every test)'''
        random.seed(42)
        self.board = Board()

    def test_board_size(self):
        '''Test that the size of the board is 16'''
        correct_size = 16
        self.assertEqual(self.board.size, correct_size,
                         'The board has the wrong size.')

    def test_board_state(self):
        '''Test that the board state contains empty stacks (empty list)'''
        correct_value = []
        self.assertEqual(self.board.state[1], correct_value,
                         'The first square of the board does not contain a empty stack')
        self.assertEqual(self.board.state[16], correct_value,
                         'The last square of the board does not contain a empty stack')


# Test cases on the Piece definition
# Create a class called PiecesTestCase that inherits from the TestCase class
class PiecesTestCase(unittest.TestCase):
    # Convert the test functions into methods by adding self as the first argument
    def setUp(self):
        self.piece1 = Piece('white', False)
        self.piece2 = Piece('black', True)

# Test if a white and black piece are and are not white pieces.
    def test_white_piece(self):
        self.assertEqual(self.piece1.colour, 'white', 'piece not white')
        self.assertFalse(self.piece2.colour == 'white')

# Test if a white and black piece are and are not black pieces.
    def test_black_piece(self):
        self.assertEqual(self.piece2.colour, 'black', 'piece not black')
        self.assertFalse(self.piece1.colour == 'black')

# Test that there is a standing and not standing piece.
    def test_piece_is_standing(self):
        self.assertFalse(self.piece1.standing)
        self.assertTrue(self.piece2.standing)


# Test cases on the definition of a Player
class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.player1 = Player('white', 15)
        self.player2 = Player('black', 1)

    # Test that a player is white and another player not white
    def test_white_player(self):
        self.assertEqual(self.player1.colour, 'white')
        self.assertNotEqual(self.player2.colour, 'white')

    # Test that a player is black and another player not black
    def test_black_player(self):
        self.assertEqual(self.player2.colour, 'black')
        self.assertNotEqual(self.player1.colour, 'black')

    # Test that the players have the correct amount of assigned pieces
    def test_nr_of_pieces(self):
        self.assertEqual(self.player1.pieces, 15)
        self.assertEqual(self.player2.pieces, 1)

class GameStateTestCase(unittest.TestCase):
    '''Test that the game state is created correctly'''
    def setUp(self):
        self.game_state = GameState()

    def test_game_state(self):
        self.assertTrue(type(self.game_state.board) == Board)
        self.assertTrue(type(self.game_state.player_1) == Player)
        self.assertTrue(type(self.game_state.player_2) == Player)

    def test_randomise_colour(self):
        '''Test randomising colour for the two players
        
        Check that the colour of the players are not the same and that one is white and one is black'''
        self.assertFalse(self.game_state.player_1.colour == self.game_state.player_2.colour)
        self.assertTrue(self.game_state.player_1.colour == 'white' or self.game_state.player_2.colour == 'white')
        self.assertTrue(self.game_state.player_1.colour == 'black' or self.game_state.player_2.colour == 'black')

    def test_black_starts_game(self):
        '''Test checking if the player that starts the game is black'''
        self.assertTrue(self.game_state.current_player.colour == 'black')


if __name__ == '__main__':
    unittest.main()
