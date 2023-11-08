from player import AbstractPlayer
from boxscore import Boxscore
from boxscore import Boxscores
from roster import Roster
from teams import Team
from schedule import Schedule, Game
from game import GameData
import time
import pandas as pd


check_game = GameData('202212040nyg')
print(check_game._gameValue)

"""
------------------------------Gamas Checked------------------------------
202301150min - change QB rating - need to run avg (top 25%)
202212040nyg (tie game) - error in _inPlayoffPic - line 105 ("string out of range")

"""
