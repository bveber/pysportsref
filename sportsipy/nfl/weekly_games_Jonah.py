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
        check_game = GameData('', boxscore).gameValue
        self.weekly_ratings[boxscore._uri] = check_game
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


class TestWeeklyGames(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.games = WeeklyGames(10, 2022)

    def test_weekly_games_simple(self):
        self.assertGreater(len(self.games.weekly_boxscores), 0, "No games in the past week")
        # assert len(games.last_days_boxscores) > 0
        self.assertGreater(len(self.games.worth_watching_week), 0, "No games worth watching in the past week")
        # assert len(games.worth_watching_last) > 0

    def test_week_ratings(self):
        for uri in self.games.weekly_ratings:
            self._test_game_ratings(uri)

    def _test_game_ratings(self, uri):
        match uri:
            case '202211100car': self.assertEqual(self.games.weekly_ratings[uri], 3.5, "Wrong rating for car")
            case '202211130tam': self.assertEqual(self.games.weekly_ratings[uri], 7.5, "Wrong rating for tam")
            case '202211130buf': self.assertEqual(self.games.weekly_ratings[uri], 19, "Wrong rating for buf")
            case '202211130chi': self.assertEqual(self.games.weekly_ratings[uri], 13.5, "Wrong rating for chi")
            case '202211130kan': self.assertEqual(self.games.weekly_ratings[uri], 10.5, "Wrong rating for kan")
            case '202211130mia': self.assertEqual(self.games.weekly_ratings[uri], 4, "Wrong rating for mia")
            case '202211130nyg': self.assertEqual(self.games.weekly_ratings[uri], 6.5, "Wrong rating for nyg")
            case '202211130oti': self.assertEqual(self.games.weekly_ratings[uri], 3, "Wrong rating for oti")
            case '202211130pit': self.assertEqual(self.games.weekly_ratings[uri], 2, "Wrong rating for pit")
            case '202211130rai': self.assertEqual(self.games.weekly_ratings[uri], 9.5, "Wrong rating for rai")
            case '202211130gnb': self.assertEqual(self.games.weekly_ratings[uri], 11, "Wrong rating for gnb")
            case '202211130ram': self.assertEqual(self.games.weekly_ratings[uri], 4, "Wrong rating for ram")
            case '202211130sfo': self.assertEqual(self.games.weekly_ratings[uri], 6, "Wrong rating for sfo")
            case '202211140phi': self.assertEqual(self.games.weekly_ratings[uri], 4.5, "Wrong rating for phi")


if __name__ == '__main__':
    suite = unittest.TestSuite()
    #TestWeeklyGames.setUpClass()
    suite.addTest(TestWeeklyGames("test_weekly_games_simple"))
    suite.addTest(TestWeeklyGames("test_week_ratings"))
    runner = unittest.TextTestRunner()  # reruns the setup (check the params here), erase?
    result = runner.run(suite)
    print(result)


"""
print(games.worth_watching_week)
print("-------------------------------------------------")
# print(games.worth_watching_last)
"""
