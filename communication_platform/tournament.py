from random import shuffle, getrandbits
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
        sorted_players = sorted(self.player_list, reverse=True)
        print("-----------------------\nLeaderboard\n-----------------------")
        for player in sorted_players:
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
        sorted_players = sorted(self.player_list, reverse=True)

        active_players = [player for player in sorted_players if player.active]

        tiebreak_list = [player for player in active_players if player.score == active_players[0].score]

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
            while True:
                name = input(f"Please type in player {i + 1}'s name! ")
                if len(name) != 0:
                    break
            self.player_list.append(Player(name, i))
        self.active_players = answer
        
    def select_player(self, players):
        active = [player for player in players if player.active]
        options = ["[Go back]", *active]
        while True:
            for i in range(len(options)):
                print(f"{i+1}. {options[i]}")
            selection = input("Selection: ")
            if selection == "1":
                return None
            elif selection.isdigit() and int(selection) <= len(options) and int(selection) > 0:
                return active[int(selection)-2]
            else:
                print("Invalid selection")

    def begin_tournament(self):
        """
        Starts tournament, sets players and match order
        """
        self.register_players()
        self.match_order = self.generate_match_order(self.player_list)

        self.play_match()

    def end_tournament(self):
        print("Tournament ended")
        sorted_players = sorted(self.player_list, reverse=True)
        for player in sorted_players:
            if player.active:
                winner = player
                break

        print(f"The winner is {winner.name}, congratulations!")


    def event_between_matches(self):
        """
        Handles events between matches. 
        Updates and prints leaderboard, checks for tiebreaks and generates new matches
        """

        self.leaderboard()

        if len(self.match_order) == 0:
            tiebreak_list = self.tiebreak_player_list()
            if len(tiebreak_list) == 0:
                self.end_tournament()
                return

            self.match_order = self.generate_match_order(tiebreak_list)
            self.active_players = len(tiebreak_list)
            print("Scores are tied, tiebreaker started!")

        ## Prints the players of the upcoming match.
        ## Creates a list of players who want to quit before the upcoming match.    

        while True:
            (player1, player2) = self.match_order[0]
            print(f"Next match: {player1.name} vs {player2.name}")
            print("1. Continue")
            print("2. A player wants to quit")
            selection = input("Selection: ")
            if selection == "1":
                break
            elif selection == "2":
                quitter = self.select_player(self.player_list)
                if quitter is not None:
                    self.player_quit(quitter)
        
        self.play_match()


    def play_match(self):
        (white, black) = self.match_order.pop(0)
        if white.whiteplays > black.whiteplays:
            white, black = black, white
        elif white.whiteplays == black.whiteplays:
            if getrandbits(1):
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
            self.update_leaderboard(black.player_id)
        elif MatchResult.BLACK_QUIT == result:
            self.player_quit(black)
            self.update_leaderboard(white.player_id)

        self.event_between_matches()

    def player_quit(self, player):
        self.active_players -= 1
        player.active = False

        new_match_order = []
        for i, (player1, player2) in enumerate(self.match_order):
            if player == player1:
                self.update_leaderboard(player2.player_id)
            elif player == player2:
                self.update_leaderboard(player1.player_id)
            else:
                new_match_order.append(self.match_order[i])
        self.match_order = new_match_order

        if self.active_players == 1:
            self.end_tournament()
                
        if len(self.match_order) == 0:
            self.event_between_matches()
