import unittest
import __init__
import random
from piece_functions import generate_piece, piece_colour, piece_is_standing
from classes import GameState, Piece, Player
from player_functions import generate_new_player, player_colour, player_pieces_left, player_decrement_pieces, is_out_of_pieces


# Test cases on the functions of pieces and players.
class PlayerPiecesFunctionsTestCase(unittest.TestCase):
    def setUp(self):
        '''Create necessary testing pieces, game state and players before running tests (is run before every test)'''
        random.seed(42)
        
        self.game_state = GameState()
        self.game_state.player_2 = Player('black', 1)

        self.white_player = Player('white', 15)
        self.black_player = Player('black', 1)

        self.white_piece_standing = Piece('white', True)
        self.white_piece_laying = Piece('white', False)
        self.black_piece_standing = Piece('black', True)
        self.black_piece_laying = Piece('black', False)

    # test generate players correctly
    def test_generate_player_func(self):
        colour1 = 'white'
        colour2 = 'black'
        new_white_player = generate_new_player(colour1)
        new_black_player = generate_new_player(colour2)
        # generate with the right colour
        self.assertEqual(new_white_player.colour, 'white')
        # generate with the right colour
        self.assertEqual(new_black_player.colour, 'black')
        # generate with 15 pieces
        self.assertEqual(new_black_player.pieces, 15)
        # generate with 15 pieces
        self.assertEqual(new_white_player.pieces, 15)

    # test generate pieces correctly
    def test_generate_piece_func(self):
        # creates piece of same colour as player
        new_piece_white_standing = generate_piece(self.white_player, True)
        new_piece_white_laying = generate_piece(self.white_player, False)
        new_piece_black_standing = generate_piece(self.black_player, True)
        new_piece_black_laying = generate_piece(self.black_player, False)
        # assert right colour
        self.assertEqual(new_piece_white_standing.colour, 'white')
        self.assertEqual(new_piece_white_laying.colour, 'white')
        self.assertEqual(new_piece_black_standing.colour, 'black')
        self.assertEqual(new_piece_black_laying.colour, 'black')
        # assert standing or laying (standing == True, laying == False)
        self.assertTrue(new_piece_white_standing.standing)
        self.assertFalse(new_piece_white_laying.standing)
        self.assertTrue(new_piece_black_standing.standing)
        self.assertFalse(new_piece_black_laying.standing)

    # test player_colour returns colours correctly
    def test_player_colour_func(self):
        self.assertEqual(player_colour(self.white_player), 'white')
        self.assertEqual(player_colour(self.black_player), 'black')

    # test player_pieces_left returns pieces left correctly
    def test_player_pieces_func(self):
        self.assertEqual(player_pieces_left(
            self.white_player), 15)  # see setUp
        self.assertEqual(player_pieces_left(self.black_player), 1)  # see setUp

    # test player_decrement_pieces decrements a player's pieces by one
    def test_player_decrement_pieces_func(self):
        # should update white_player.pieces to 14
        player_decrement_pieces(self.white_player)
        # should update white_player.pieces to 0
        player_decrement_pieces(self.black_player)
        self.assertEqual(player_pieces_left(self.white_player), 14)
        self.assertEqual(player_pieces_left(self.black_player), 0)

    # test piece_colour returns a piece's colour correctly
    def test_piece_colour_func(self):
        self.assertEqual(piece_colour(self.white_piece_standing), 'white')
        self.assertEqual(piece_colour(self.black_piece_laying), 'black')

    # test piece_is_standing returns true if a piece is standing, false if it is laying
    def test_piece_is_standing_func(self):
        self.assertTrue(piece_is_standing(self.white_piece_standing))
        self.assertTrue(piece_is_standing(self.black_piece_standing))
        self.assertFalse(piece_is_standing(self.white_piece_laying))
        self.assertFalse(piece_is_standing(self.black_piece_laying))

    def test_out_of_pieces(self):
        '''Test checking if a player is out of pieces.

        Check if the white player and black player has pieces left 
        and then remove the black player's piece and check again'''
        self.assertFalse(is_out_of_pieces(self.game_state.player_1))
        self.assertFalse(is_out_of_pieces(self.game_state.player_2))
        player_decrement_pieces(self.game_state.player_2)
        self.assertTrue(is_out_of_pieces(self.game_state.player_2))


if __name__ == '__main__':
    unittest.main()
