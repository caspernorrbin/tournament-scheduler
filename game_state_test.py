from ast import main
import unittest as ut
import game_state

class BoardCannotBeSmallerThanSixBySix(ut.TestCase):
    
    def width_cannot_be_less_than_six(self):
        with self.assertRaises(ValueError):
            game_state.Board(5, 10)


    def width_can_be_equal_to_six(self):
        game_state.Board(6, 10)

    def heigth_cannot_be_less_than_six(self):
        with self.assertRaises(ValueError):
            game_state.Board(10, 5)

    def height_can_be_equal_to_six(self):
        game_state.Board(10, 6)



if __name__ == '__main__':
    ut.main()