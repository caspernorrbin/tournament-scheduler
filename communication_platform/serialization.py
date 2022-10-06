from pickle import load, dump

FILE_NAME = 'game_state.pickle'

def save_game_state(game_state: object):
    """Saves a game state to the file set by the FILE_NAME constant.
    
    :param game_state
    :raises OSError: Errors relating to being unable to open or write to the file.
    :raises PicklingError: game_state or member in gamestate cannot be pickled.
    see https://docs.python.org/3/library/pickle.html#pickle-picklable for details.
    """
    with open(FILE_NAME, "wb") as f:
        dump(game_state, f)

def load_game_state() -> object:
    """Loads a game state from the file set by the FILE_NAME constant.
    
    :raises OSError: Errors relating to being unable to open or write to the file.
    :raises UnpicklingError: game state cannot be unpickled.
    :raises ImportError: The game state is not in scope.
    This might occurr if the game-state is a class and has is not imported in the module
    that is attempting to use load_game_state()

    Other errors can also be raised, but assuming a well-formed game state and OS environment should not:
    https://docs.python.org/3/library/pickle.html#module-interface

    :return: Game state object saved to FILE_NAME.
    """
    with open(FILE_NAME, "rb") as f:
        return load(f)