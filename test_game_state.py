import unittest as ut
import game_state


class BoardCannotBeSmallerThan6x6(ut.TestCase):

    def test_width_cannot_be_less_than_6(self):
        with self.assertRaises(ValueError):
            game_state.Board(5, 10)

    def test_width_can_be_equal_to_6(self):
        game_state.Board(6, 10)

    def test_heigth_cannot_be_less_than_6(self):
        with self.assertRaises(ValueError):
            game_state.Board(10, 5)

    def test_height_can_be_equal_to_6(self):
        game_state.Board(10, 6)


class BoardCannotBeLargerThan24x24(ut.TestCase):
    def test_width_cannot_be_more_than_24(self):
        with self.assertRaises(ValueError):
            game_state.Board(25, 10)

    def test_width_can_be_equal_to_24(self):
        game_state.Board(24, 10)

    def test_heigth_cannot_be_less_more_24(self):
        with self.assertRaises(ValueError):
            game_state.Board(10, 25)

    def test_height_can_be_equal_to_24(self):
        game_state.Board(10, 24)


if __name__ == '__main__':
    ut.main(verbosity=2)
