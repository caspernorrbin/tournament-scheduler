from ast import main
import unittest as ut
import game_state

class BoardCannotBeSmallerThanSixBySix(ut.TestCase):
    
    def test_width_cannot_be_less_than_six(self):
        with self.assertRaises(ValueError):
            game_state.Board(5, 10)


    def test_width_can_be_equal_to_six(self):
        game_state.Board(6, 10)

    def test_heigth_cannot_be_less_than_six(self):
        with self.assertRaises(ValueError):
            game_state.Board(10, 5)

    def test_height_can_be_equal_to_six(self):
        game_state.Board(10, 6)



if __name__ == '__main__':
    ut.main(verbosity=2)