from dataclasses import dataclass
from collections import defaultdict
from enum import Enum

MIN_BOARD_SIZE = 6
MAX_BOARD_SIZE = 24


class Orientation(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Color(Enum):
    BLACK = 0
    WHITE = 1


@dataclass
class Piece:
    orientation: Orientation
    color: Color


@dataclass(init=False)
class Board:
    """Data structure for representing a board. Currently implemented as a dict 
    of coordinates for piece placement to a list of pieces.

    TODO: It might be probable that other components represent their board as a
    3D list, if so this representation might need to change. Representing the
    board as a dict of list should have the benefit of being easlily 
    serializable."""
    size: int

    board: defaultdict[tuple: list]

    def __init__(self, size: int) -> None:
        """TODO: If board input takes care of checking for valid sizes, the
        checks here become unneccesary. It is currently impossible to construct
        a board of an invalid size."""
        if not MIN_BOARD_SIZE <= size <= MAX_BOARD_SIZE:
            raise ValueError(
                f'Dimension of board is ({size},{size}) side length must be between {MIN_BOARD_SIZE} and {MAX_BOARD_SIZE}')
        
        self.size = size
        self.board = defaultdict(list)

    @property
    def dimensions(self):
        return (self.size, self.size)


    def add_piece(self, piece: Piece, coordinate: tuple[int, int]) -> None:
        location = self.board[coordinate]
        
        # If the top piece is vertical we cannot place a piece there.
        if location and location[-1].orientation == Orientation.VERTICAL:
            return
        
        location.append(piece)
