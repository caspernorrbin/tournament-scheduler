from random import shuffle

MatchList = list[tuple[int, int]]


def match_order(players: list[int]) -> MatchList:
    """
    Generates a random combination of matches based on given list of players,
    which should consist of assigned integers for each player.

    :param players: list of players that should play matches
    :return: list of unique random player combinations
    """
    match_list = []
    for p1 in players:
        for p2 in players:
            if (p1 != p2 and ((p1, p2) not in (match_list)) and ((p2, p1) not in (match_list))):
                match_list.append((p1, p2))
    shuffle(match_list)

    return match_list


# temporary testing, allowed number of players is 3-8
min_players = 3
max_players = 8


def test_no_duplicate_matches():
    for number_of_players in range(min_players, max_players):
        match_list = match_order(range(number_of_players))
        assert len(match_list) == len(set(match_list))
        assert len(match_list) == len(
            set([match[::-1] for match in match_list]))


def test_all_play_all():
    for number_of_players in range(min_players, max_players):
        match_list = match_order(range(number_of_players))

        # compare generated number of matches to theoretical number of matches
        assert len(match_list) == number_of_players*(number_of_players-1)/2


test_no_duplicate_matches()
test_all_play_all()

print(match_order(range(3)))
