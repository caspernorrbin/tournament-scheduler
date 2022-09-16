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
    width: int
    height: int

    board: defaultdict[tuple: list]

    def __init__(self, width: int, height :int) -> None:
        """TODO: If board input takes care of checking for valid sizes, the
        checks here become unneccesary. It is currently impossible to construct
        a board of an invalid size."""
        if width < MIN_BOARD_SIZE or height < MIN_BOARD_SIZE:
            raise ValueError(
                f'Dimension of board is ({width},{height}) side length must be greater than {MIN_BOARD_SIZE}')

        if width > MAX_BOARD_SIZE or height > MAX_BOARD_SIZE:
            raise ValueError(
                f'Dimension of board is ({width},{height}) side length must be smaller than {MAX_BOARD_SIZE}')

        self.width = width
        self.height = height

        self.board = defaultdict(default_factory=list)

    @property
    def size(self):
        return (self.width, self.height)


    def add_piece(self, piece: Piece, coordinate: tuple[int, int]) -> None:
        location = self.board[coordinate]
        
        # If the top piece is vertical we cannot place a piece there.
        if location and location[0].orientation == Orientation.VERTICAL:
            return
        
        self.board[location].push(piece)
