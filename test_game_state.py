import unittest as ut
import game_state


class BoardSizeBetween6x6And24x24(ut.TestCase):

    def test_size_cannot_be_less_than_6(self):
        with self.assertRaises(ValueError):
            game_state.Board(5)

    def test_size_can_be_equal_to_6(self):
        game_state.Board(6)

    def test_size_cannot_be_greater_than_24(self):
        with self.assertRaises(ValueError):
            game_state.Board(26)

    def test_size_can_be_equal_to_24(self):
        game_state.Board(24)

class SerializationOfGameState(ut.TestCase):

    def setUp(self) -> None:
        self.board = game_state.Board(6)
        a = game_state.Piece(game_state.Orientation.HORIZONTAL, game_state.Color.WHITE)
        b = game_state.Piece(game_state.Orientation.HORIZONTAL, game_state.Color.BLACK)
        c = game_state.Piece(game_state.Orientation.VERTICAL, game_state.Color.WHITE)

        self.board.add_piece(a, (1,1))
        self.board.add_piece(b, (1,1))
        self.board.add_piece(c, (0,0))

        game_state.save_game_state(self.board)

    def test_saving_game_state(self):
        game_state.save_game_state(self.board)

    def test_loading_game_state(self):
        state = game_state.load_game_state()
        self.assertEqual(type(self.board), type(state))

    def test_saving_and_loading_does_not_change_state(self):
        state = game_state.load_game_state()
        self.assertEqual(self.board, state)
        

if __name__ == '__main__':
    ut.main(verbosity=2)
