from player import AbstractPlayer
from boxscore import Boxscore, BoxscorePlayer
from boxscore import Boxscores
from roster import Roster
from teams import Team
from schedule import Schedule, Game
from game import GameData
from constants import PARSING_SCHEME
from sportsipy import utils

import time
import pandas as pd


MAIN_URL = 'https://www.pro-football-reference.com'
"""
kan_roster = Roster('KAN')
print(kan_roster.players)
boxscore1 = Boxscore('202209150kan')
print(boxscore1.summary)
player1 = AbstractPlayer('HopkDu00', 'Dustin Hopkins','202209150kan')
print(player1.name)
try_team = Team('CHI')
print(try_team.rank)


df_list = pd.read_html("https://www.pro-football-reference.com")
print(df_list[0])

phili = Team("PHI")
if('*' == df_list[1]['Tm'][1][3]):
    print("hhh")


boxscore1 = Boxscore('202209150kan')
print(boxscore1.winning_abbr)

phili = Team("KAN")
def findConferences(team1):
        url = "https://www.pro-football-reference.com"
        teamOneConf = 'AFC'
        df_list = pd.read_html(url)
        for i in range(0,len(df_list[1]['Tm'])):
            if team1.abbreviation == df_list[1]['Tm'][i][0:3]:
                teamOneConf = 'NFC'
        print(teamOneConf)

findConferences(phili)


houston_schedule = Schedule('HTX')
for game in houston_schedule:
    print(game.date)  # Prints the date the game was played
    print(game.quarterback_rating)  # Prints whether the team won or lost
    # Creates an instance of the Boxscore class for the game.
    boxscore = game.boxscore
boxscore1 = Boxscore('202302120phi')
kan_roster = Roster('KAN')




game1 = GameData('202302120phi', )


#check_game = GameData('202302120phi', 'PHI', 'KAN')

#print(check_game._gameValue)

ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')

ttt = Team('KAN')
ttt = Team('KAN')

ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')

ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')
ttt = Team('KAN')



houston_schedule = Team('HTX')
print(check_game._gameValue)

boxscore1 = Boxscore('202209150kan')
print(boxscore1.home_abbreviation)

check_game = GameData('202209150kan', 'LAC', 'KAN')
print(check_game._gameValue)


check_game = GameData('202209150kan', 'KAN', 'SDG')
print(check_game._gameValue)
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



boxscore1 = Boxscore('202209180rai')
print(boxscore1.away_abbreviation)
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
check_game = GameData('202212040nyg')
print(check_game._gameValue)


url = MAIN_URL
df_list = pd.read_html(url)
for i in range(0,len(df_list[1]['Tm'])):
        print(df_list[1]['Tm'][i][-1])


check_game = GameData('202212040nyg')
print(check_game._gameValue)



url = MAIN_URL
df_list = pd.read_html(url)
for i in range(0,len(df_list[1]['Tm'])):
    print(PARSING_SCHEME['NFC Team'].text())


 check_game = Boxscore('202209180rai')
team_name1 = check_game._retrieve_html_page('202209180rai')
team_name2 = team_name1('table[class="sortable stats_table"]').eq(1)
counter = 1
for score_info in team_name2('tbody tr').items():
    if(score_info('th[data-stat="player"]').text() != 'Player' and score_info('th[data-stat="player"]').text() != ''):
        counter+=1
        print(score_info('td[data-stat="rec_yds"]').text())   


check_game = Boxscore('202209180rai')
team_name1 = check_game._retrieve_html_page('202209180rai')
team_name2 = check_game._parse_players_stats(team_name1)
for player in team_name2:
    print(player['quarterback rating'])


maxRating = 0
check_game = Boxscore('202209180rai')
team_name1 = check_game._retrieve_html_page('202209180rai')
team_name2 = check_game._parse_players_stats(team_name1)
for player in team_name2:
            if(player['quarterback rating']) and float(player['quarterback rating']) > maxRating:
                maxRating = float(player['quarterback rating'])

print(maxRating)    


check_game = Boxscore('202211130chi')
team_name1 = check_game._retrieve_html_page('202211130chi')
team_name2 = check_game._parse_scoring(team_name1)
print(int(team_name2[3][-1]['current_score']['away']))
print(check_game.away_abbreviation.upper())
print(check_game.losing_abbr)

"""

check_game = GameData('202211130chi')
print(check_game.gameValue)
