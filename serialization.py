from pickle import load, dump

FILE_NAME = 'game_state.pickle'

def save_game_state(gamestate: object):
    with open(FILE_NAME, "wb") as f:
        dump(gamestate, f)

def load_game_state() -> object:
    with open(FILE_NAME, "rb") as f:
        return load(f)