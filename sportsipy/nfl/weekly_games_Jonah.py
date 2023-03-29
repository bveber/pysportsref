import datetime
import calendar
from nfl.boxscore import Boxscores, Boxscore
from nfl.game import GameData


class WeeklyGames:
    """Class that collects all the games from the past week"""

    def __init__(self):
        self.weekly_boxscores = []
        self.last_days_boxscores = []
        self.worth_watching_last = []
        self.worth_watching_week = []
        self.today_date = datetime.date.today()
        self._get_week_boxscores()
        self._get_worth_watching()

    def _get_week_boxscores(self):
        """Returns the boxscores from all the games in the past week"""
        # TODO - add scrapping to get current week number from https://www.pro-football-reference.com/boxscores/
        games = Boxscores(15, 2022).games  # TODO - base on [today_date]
        for week in games:
            self.weekly_boxscores = boxscores_from_games(games[week])
            self._get_last_games(games[week])

    # TODO - add usage back to code
    def _get_last_games(self, week_games):
        """return only the games from the past day of games out of past week"""
        latest_date = max([game.datetime for game in week_games])
        last_games = [game for game in week_games if game.datetime == latest_date]
        self.last_days_boxscores = boxscores_from_games(last_games)

    def _get_worth_watching(self):
        """Returns a list of strings with the games worth watching"""
        for boxscore in self.weekly_boxscores:
            # TODO - change to full ALGO!!!
            if (if_worth_watching(boxscore)):
                home, away = get_team_names(boxscore)
                self.worth_watching_week.append(print_teams(home, away))
                # print(self.print_teams(home, away))
        for boxscore in self.last_days_boxscores:
            # TODO - change to full ALGO!!!
            if (if_worth_watching(boxscore)):
                home, away = get_team_names(boxscore)
                self.worth_watching_last.append(print_teams(home, away))
                # print(self.print_teams(home, away))


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

def if_worth_watching(boxscore):
    """Checks if the game is worth watching based on it's boxscore"""
    print(boxscore.scoring)
    check_game = GameData('', boxscore)
    if check_game >= 5:
        return True
    return False
