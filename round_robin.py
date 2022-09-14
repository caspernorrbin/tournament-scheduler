from random import shuffle

MatchList = list[tuple[int, int]]


def match_order(players: list[int]) -> MatchList:
    """
    Generates a random combination of matches based on given list of players,
    which should consist of assigned integers for each player.

    :param players: list of players that should play matches
    :return: list of unique random player combinations
    """
    match_list = [(p1, p2) for p1 in players for p2 in players if p1 != p2]
    return shuffle(match_list)
