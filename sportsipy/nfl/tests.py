import datetime
import unittest
from nfl.weekly_games_Jonah import WeeklyGames
from nfl.game import GameData

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
            case '202211130oti': self.assertEqual(self.games.weekly_ratings[uri], 5, "Wrong rating for oti")
            case '202211130pit': self.assertEqual(self.games.weekly_ratings[uri], 4, "Wrong rating for pit")
            case '202211130rai': self.assertEqual(self.games.weekly_ratings[uri], 9.5, "Wrong rating for rai")
            case '202211130gnb': self.assertEqual(self.games.weekly_ratings[uri], 11, "Wrong rating for gnb")
            case '202211130ram': self.assertEqual(self.games.weekly_ratings[uri], 4, "Wrong rating for ram")
            case '202211130sfo': self.assertEqual(self.games.weekly_ratings[uri], 8, "Wrong rating for sfo")
            case '202211140phi': self.assertEqual(self.games.weekly_ratings[uri], 4.5, "Wrong rating for phi")


class TestSingleGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game = GameData('202211130buf').gameValue

    def test_game(self):
        self.assertEqual(self.game, 19, "Wrong rating for buf game")

def testWeek(suite):
    suite.addTest(TestWeeklyGames("test_weekly_games_simple"))
    suite.addTest(TestWeeklyGames("test_week_ratings"))


def testSingleGame(suite):
    suite.addTest(TestSingleGame("test_game"))


if __name__ == '__main__':
    suite = unittest.TestSuite()
    testSingleGame(suite)
    testWeek(suite)
    runner = unittest.TextTestRunner()  
    result = runner.run(suite)
    print(result)
