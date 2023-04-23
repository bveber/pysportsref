import datetime
import unittest
from nfl.boxscore import Boxscores, Boxscore
from nfl.game import GameData


class WeeklyGames:
    """Class that collects all the games from the past week"""

    def __init__(self, week=10, year=2022):
        self.weekly_boxscores = []
        # self.last_days_boxscores = []
        # self.worth_watching_last = []
        self.worth_watching_week = []
        self.today_date = datetime.date.today()
        self.weekly_ratings = {}
        self._qb_ratings = []  # for testing, TODO - remove
        self._get_week_boxscores(week, year)
        self._get_worth_watching()
        

    def _get_week_boxscores(self, week, year):
        """Returns the boxscores from all the games in the past week"""
        # TODO - add scrapping to get current week number from https://www.pro-football-reference.com/boxscores/
        games = Boxscores(week, year).games  # TODO - base on [today_date]
        for week in games:
            self.weekly_boxscores = boxscores_from_games(games[week])
            # self._get_last_games(games[week])

    """
    # TODO - add usage back to code
    def _get_last_games(self, week_games):
        # return only the games from the past day of games out of past week
        latest_date = max([game.datetime for game in week_games])
        last_games = [game for game in week_games if game.datetime == latest_date]
        self.last_days_boxscores = boxscores_from_games(last_games)
    """

    def _get_worth_watching(self):
        """Returns a list of strings with the games worth watching"""
        # i = 0  # TODO - for test, remove
        for boxscore in self.weekly_boxscores:
            # print(i)
            # i += 1
            home, away = get_team_names(boxscore)  # TODO - for test, remove
            # print(print_teams(home, away))  # TODO - for test, remove
            # print(boxscore._uri)
            if (self._if_worth_watching(boxscore)):
                home, away = get_team_names(boxscore)
                self.worth_watching_week.append(print_teams(home, away))
                # print(self.print_teams(home, away))
        """
        for boxscore in self.last_days_boxscores:
            # TODO - change to full ALGO!!!
            if (self._if_worth_watching(boxscore)):
                home, away = get_team_names(boxscore)
                self.worth_watching_last.append(print_teams(home, away))
                # print(self.print_teams(home, away))
        """
    def _if_worth_watching(self, boxscore):
        """Checks if the game is worth watching based on it's boxscore"""
        # print(boxscore.scoring)
        game = GameData('', boxscore)
        check_game = game.gameValue
        self.weekly_ratings[boxscore._uri] = check_game
        self._qb_ratings.append(game._quarterback_rating_max)  # TODO - for test, remove 
        print(str(check_game) + "game score")  # TODO - for test, remove
        if check_game >= 5:
            return True
        return False


def boxscores_from_games(games):
    boxscores_names = []
    boxscores = []
    for game in games:
        boxscores_names.append(game['boxscore'])
        # could add abbv here
    for box_name in boxscores_names:
        boxscore = Boxscore(box_name)
        boxscores.append(boxscore)
    return boxscores


def get_team_names(boxscore):
    """Returns the home(first) and away team(second) names"""
    if (boxscore.winner == 'Home'):
        home_name = boxscore.winning_name
        away_name = boxscore.losing_name
    else:
        home_name = boxscore.losing_name
        away_name = boxscore.winning_name
    return home_name, away_name


def print_teams(home, away):
    """Returns string with team for email"""
    return (home + " - " + away)

