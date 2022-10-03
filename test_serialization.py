import game_state
import serialization
import unittest as ut

class SerializationOfGameState(ut.TestCase):

    def setUp(self) -> None:
        self.board = game_state.Board(6)
        a = game_state.Piece(game_state.Orientation.HORIZONTAL, game_state.Color.WHITE)
        b = game_state.Piece(game_state.Orientation.HORIZONTAL, game_state.Color.BLACK)
        c = game_state.Piece(game_state.Orientation.VERTICAL, game_state.Color.WHITE)

        self.board.add_piece(a, (1,1))
        self.board.add_piece(b, (1,1))
        self.board.add_piece(c, (0,0))

        serialization.save_game_state(self.board)

    def test_saving_game_state(self):
        serialization.save_game_state(self.board)

    def test_loading_game_state(self):
        state = serialization.load_game_state()
        self.assertEqual(type(self.board), type(state))

    def test_saving_and_loading_does_not_change_state(self):
        state = serialization.load_game_state()
        self.assertEqual(self.board, state)