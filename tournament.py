from random import shuffle
from itertools import combinations
from game import select_player
from player import Player

MatchList = list[tuple[Player, Player]]


class Tournament:
    """
    Represents a tournament.
    """

    def __init__(self):
        self.player_list = []
        self.match_order = []

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

    def tiebreak_player_list(self):
        """
        check if there is a tiebreak
        :return: list of players with the same (highest) score if more than one player, else return empty list
        """
        sorted = self.get_active_players()
        sorted.sort(reverse=True)

        tiebreak_list = []
        for player in sorted:
            if player.score < sorted[0].score:
                break
            tiebreak_list.append(player)
        return tiebreak_list if len(tiebreak_list) > 1 else []

    def generate_match_order(self, players: list[Player]) -> MatchList:
        """
        Generates a random combination of matches based on given list of players
        """
        match_list = list(combinations(players, 2))
        shuffle(match_list)

        return match_list

    def register_players(self) -> list[Player]:
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

    def begin_tournament(self):
        """
        Starts tournament, sets players and match order
        """
        self.register_players()
        self.match_order = self.generate_match_order(self.player_list)

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

        self.match_order = self.generate_match_order(tiebreak_list)

        # TODO: Start next match, pop match from match list

        ## Prints the players of the upcoming match.
        ## Creates a list of players who want to quit before the upcoming match.    
        (player1, player2) = self.match_order[0]
        players = self.player_list
        quitters = []
        while True:
            print(f"Next match: {player1} vs {player2}")
            print("1. Continue")
            print("2. A player wants to quit")
            selection = input("Selection: ")
            if selection == "1":
                break
            elif selection == "2":
                quitter = select_player(players)
                if quitter != None:
                    quitters.append(quitter)
                if quitter == player1 or quitter == player2:
                    break
        #TODO: Remove quitters from match_order and player_list