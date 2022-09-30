from random import shuffle
from itertools import combinations

from player import Player
from match import MatchResult, play_match

MatchList = list[tuple[Player, Player]]


class Tournament:
    """
    Represents a tournament.
    """

    def __init__(self):
        self.active_players = 0
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
        sorted = self.player_list.copy()
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
        self.active_players = answer

    def begin_tournament(self):
        """
        Starts tournament, sets players and match order
        """
        self.register_players()
        self.match_order = self.generate_match_order(self.player_list)

        self.play_match()

    def end_tournament(self):
        # TODO: Announce winner
        quit()


    def event_between_matches(self):
        """
        Handles events between matches. 
        Updates and prints leaderboard, checks for tiebreaks and generates new matches
        """

        self.leaderboard()

        # TODO: Check if any player wants to quit

        if len(self.match_order) == 0:
            tiebreak_list = self.tiebreak_player_list()
            if len(tiebreak_list) == 0:
                self.end_tournament()

            self.match_order = self.generate_match_order(tiebreak_list)
            self.active_players = len(tiebreak_list)

        self.play_match()


    def play_match(self):
        (white, black) = self.match_order.pop()
        if white.whiteplays < black.whiteplays:
            white, black = black, white
        result = play_match(white, black)
        white.whiteplays += 1
        black.blackplays += 1
        if MatchResult.WHITE_WIN == result:
            self.update_leaderboard(white.player_id)
        elif MatchResult.BLACK_WIN == result:
            self.update_leaderboard(black.player_id)
        elif MatchResult.WHITE_QUIT == result:
            self.player_quit(white)
            self.update_leaderboard(black)
        elif MatchResult.BLACK_QUIT == result:
            self.player_quit(black)
            self.update_leaderboard(white)

        self.event_between_matches()

    def player_quit(self, player):
        # TODO: Check how many players are left, if only one: end tournament
        if self.active_players == 2:
            self.end_tournament()
        
        self.active_players -= 1
        
        player.active = False
        for i, (player1, player2) in enumerate(self.match_order):
            if player == player1:
                del self.match_order[i]
                self.update_leaderboard(player2)
            if player == player2:
                del self.match_order[i]
                self.update_leaderboard(player1)
