from random import shuffle
from itertools import combinations
from player import Player

MatchList = list[tuple[Player, Player]]


def match_order(players: list[Player]) -> MatchList:
    """
    Generates a random combination of matches based on given list of players,
    which should consist of assigned integers for each player.

    :param players: list of players that should play matches
    :return: list of unique random player combinations
    """
    match_list = list(combinations(players, 2))
    shuffle(match_list)

    return match_list


# temporary testing, allowed number of players is 3-8
min_players = 3
max_players = 8


def test_no_duplicate_matches():
    for number_of_players in range(min_players, max_players):
        player_list = [Player("player_name_"+str(player), player)
                       for player in range(number_of_players)]
        match_list = match_order(player_list)

        # extract ids to check duplicates and reverse ids
        match_list_id_only = [(match[0].player_id, match[1].player_id)
                              for match in match_list]

        assert len(match_list) == len(set(match_list_id_only))
        assert len(match_list) == len(
            set([match[::-1] for match in match_list_id_only]))


def test_all_play_all():
    for number_of_players in range(min_players, max_players):
        player_list = [Player("player_name_"+str(player), player)
                       for player in range(number_of_players)]
        match_list = match_order(player_list)

        # compare generated number of matches to theoretical number of matches
        assert len(match_list) == number_of_players*(number_of_players-1)/2


test_no_duplicate_matches()
test_all_play_all()
