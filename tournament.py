from round_robin import match_order
from player import Player


class Tournament:
    """
    Represents a tournament.
    """

    def __init__(self):
        self.player_list = []
        self.match_order = []
        self.initialize_tournament()

    def leaderboard(self):
        """
        prints the leaderboard
        """
        sorted = self.player_list.copy()
        sorted.sort(reverse=True)
        print("Leaderboard\n-----------------------")
        for player in sorted:
            print(player)

    # NB: we don't know in what kind of format the game component outputs
    # the score after each match, right now we assume winner_id
    def update_leaderboard(self, winner_id: int):
        """
        updates the leaderboard
        :param winner_id: the id of the player who one the last match
        """
        if 0 <= winner_id < len(self.player_list):
            self.player_list[winner_id].score += 1

    def check_for_tiebreak(self):
        """
        check if there is a tiebreak
        :return: list of players with the same (highest) score if more than one player, else return empty list
        """
        sorted = self.player_list.copy()
        sorted.sort(reverse=True)

        tiebreak_list = []
        for player in sorted:
            if player.score < sorted[0].score:
                break
            tiebreak_list.append(player)
        return tiebreak_list if len(tiebreak_list) > 1 else []

    def initialize_players(self):
        """
        asks user to input how many players will be playing, and the names of the players
        saves the players in the tournament
        """
        answer = ""
        while True:
            answer = input("How many players are playing today? ")
            if answer.isdigit():
                answer = int(answer)
                if 3 <= answer <= 8:
                    break
                else:
                    print("Please type in a number between 3 and 8")

        self.player_list = []
        for i in range(answer):
            name = input(f"Please type in player {i+1}'s name! ")
            self.player_list.append(Player(name, i))

    def initialize_tournament(self):
        """
        Starts tournament, sets players and match order
        """
        self.initialize_players()
        self.match_order = match_order(self.player_list)
        [print(player) for player in self.match_order]
        # TODO: Start the first match

    def end_tournament(self):
        # TODO: Announce winner
        return

    def event_between_matches(self, winner_id: int):
        """
        Handles events between matches. 
        Updates and prints leaderboard, checks for tiebreaks and generates new matches
        """
        # TODO: use self.update_leaderboard(winner_id) when winner_id is implemented/available
        self.leaderboard()

        if len(self.match_order) == 0:
            tiebreak_list = self.check_for_tiebreak()
            if len(tiebreak_list) == 0:
                self.end_tournament()

        # TODO: Check if any player wants to quit, update tiebreak_list accordingly

        self.match_order = match_order(tiebreak_list)

        # TODO: Start next match, pop match from match list
