import unittest
from player import Player
from tournament import Tournament


class TestMatchOrder(unittest.TestCase):
    __min_players = 3
    __max_players = 8

    def test_no_duplicate_matches(self):
        for number_of_players in range(self.__min_players, self.__max_players):
            tournament = Tournament()
            player_list = [Player("player_name_"+str(player), player)
                           for player in range(number_of_players)]
            match_list = Tournament.generate_match_order(tournament,
                                                         player_list)

            # extract ids to check duplicates and reverse ids
            match_list_id_only = [(match[0].player_id, match[1].player_id)
                                  for match in match_list]

            self.assertEqual(len(match_list), len(set(match_list_id_only)))
            self.assertEqual(len(match_list), len(
                set([match[::-1] for match in match_list_id_only])))

    def test_all_play_all(self):
        for number_of_players in range(self.__min_players, self.__max_players):
            tournament = Tournament()
            player_list = [Player("player_name_"+str(player), player)
                           for player in range(number_of_players)]
            match_list = Tournament.generate_match_order(tournament,
                                                         player_list)

            # compare generated number of matches to theoretical number of matches
            self.assertEqual(
                len(match_list), number_of_players*(number_of_players-1)/2)

if __name__ == '__main__':
    unittest.main()
