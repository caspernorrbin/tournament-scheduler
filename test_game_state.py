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


if __name__ == '__main__':
    ut.main(verbosity=2)
