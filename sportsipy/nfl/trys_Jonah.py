from player import AbstractPlayer
from boxscore import Boxscore
from boxscore import Boxscores
from roster import Roster
from teams import Team
from schedule import Schedule, Game
from game import GameData
import time
import pandas as pd


boxscore1 = Boxscore('202209150kan')

print(int(boxscore1.scoring[3][-1]['current_score']['away']))
check_game = GameData('202209150kan')
print(check_game._gameValue)
boxscore1 = Boxscore('202209150kan')
print(boxscore1.winning_abbr)
print(boxscore1.losing_abbr)


boxscore1 = Boxscore('202209150kan')
print(boxscore1._alt_abbreviations)
print(boxscore1.home_abbreviation)

boxscore2 = Boxscore('202209180rai')
team1, team2 = boxscore2._alt_abbreviations(boxscore2._retrieve_html_page('202209150kan'))
print(team1)
print(team2)
print(boxscore2.home_abbreviation)
print(boxscore2.away_abbreviation)
boxscore1 = Boxscore('202209150kan')
print(boxscore1.winning_abbr)
print(boxscore1.losing_abbr)
print(boxscore1.home_abbreviation.upper())
print(boxscore1.away_abbreviation.upper())

"""
check_game = GameData('202209150kan')
print(check_game._gameValue)
"""
