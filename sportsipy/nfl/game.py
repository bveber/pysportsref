import datetime
import pandas as pd
from pyquery import PyQuery as pq
from lxml.etree import ParserError
import requests
import calendar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from boxscore import Boxscore
from boxscore import Boxscores
from schedule import Schedule
from schedule import Game
from teams import Team

BOXSCORE_URL = 'https://www.pro-football-reference.com/boxscores/%s.htm'
MAIN_URL = 'https://www.pro-football-reference.com'


class GameData:
    """
    class that colleects all the data from the game.
    this data includes the boxScore details, stats from the game and the players inside the game
    Furtermore, the game will add in the future additional information about the game and will calculate the 'Value' of the game according to the Parameters the game checks out.
    """

    def __init__(self, boxscoreString):
        self._boxscore = Boxscore(boxscoreString)
        team_name1 = self._boxscore.winning_abbr
        team_schedule = Schedule(team_name1)
        for game in team_schedule:
            if game.boxscore_index == boxscoreString:
                self._game = game
        #self._game = Game(game_data, game_type, year) - game_data = None, game_type= None, year= None
        self._winningTeam = Team(self._boxscore.winning_abbr)
        self._losingTeam = Team(self._boxscore.losing_abbr)
        self._altTeam1Name, self._altTeam2Name = self._boxscore._alt_abbreviations(self._boxscore._retrieve_html_page(boxscoreString))
        self._awayTeam = Team(self._boxscore.away_abbreviation.upper())
        self._homeTeam = Team(self._boxscore.home_abbreviation.upper())
        self._gameValue = None
        self._gameSummery = None
        self._homePoints = None
        self._awayPoints = None
        self._totalPoints = None
        self._thirdQuarterAway = None
        self._thirdQuarterHome = None
        self._diffThird = None
        self._diffPoints = None
        self._isOvertime = None
        self._lastMinWin = None
        self._counterChangeLead = None
        self._isTeamOnePlayoffs = None
        self._isTeamTwoPlayoffs = None
        self._percentageDiff = None
        self._rankDiff = None
        self._team1Conf = None
        self._team2Conf = None
        self._totalYards = None
        self._diffYards = None
        self._totalMinPoss = None
        self._diffMinPoss = None
        self.firstValue = 0.0
        self.secondValue = 0.0
        self.thirdValue = 0.0
        self.forthValue = 0.0
        self.fifthValue = 0.0
        self.sixthValue = 0.0
        self.seventhValue = 0.0
        self.eightValue = 0.0
        self.ninthValue = 0.0
        self.tenthValue = 0.0
        self.eleventhValue = 0.0
        self.twelthValue = 0.0

        self._setGameValue(boxscoreString)

    
    def _calGameScores(self):
        lastMinScore = False
        counterLeadChanges = 0
        lastScoreHome = 0
        lastScoreTeamAway = 0
        diffBefore = 0
        for i in range (4):
            for score in self._boxscore.scoring[i]:
                diffNow = int(score['current_score']['away']) - int(score['current_score']['home'])
                timePlay = score['time']
                if(diffBefore <= 0 and diffNow > 0) or (diffBefore >= 0 and diffNow < 0):
                    counterLeadChanges+= 1
                    if (i==3) and (int(timePlay[0]) < 3) and (timePlay[1] == ':'):
                        lastMinScore = True
                diffBefore = diffNow
        return lastMinScore, counterLeadChanges
                
                 

   
        
    def _inPlayoffPic(self):
        url = MAIN_URL
        isTeam1Playoff = False
        isTeam2Playoff = False
        df_list = pd.read_html(url)
        for i in range(0,len(df_list[1]['Tm'])):
            if ((self._altTeam1Name == df_list[1]['Tm'][i][0:3]) and ((i % 5 == 1) or ('*' == df_list[1]['Tm'][i][-1]))) or ((self._altTeam1Name == df_list[1]['Tm'][i][0:3]) and ( (self._awayTeam.rank <=13 ) or ('+' == df_list[1]['Tm'][i][-1]))):
                isTeam1Playoff = True
            if ((self._altTeam1Name == df_list[0]['Tm'][i][0:3]) and ((i % 5 == 1) or ('*' == df_list[0]['Tm'][i][-1]))) or ((self._altTeam1Name == df_list[0]['Tm'][i][0:3]) and ( (self._awayTeam.rank <=13 ) or ('+' == df_list[0]['Tm'][i][-1]))):
                isTeam1Playoff = True
            if ((self._altTeam2Name == df_list[1]['Tm'][i][0:3]) and ((i % 5 == 1) or ('*' == df_list[1]['Tm'][i][-1]))) or ((self._altTeam2Name == df_list[1]['Tm'][i][0:3]) and ( (self._homeTeam.rank <=13 ) or ('+' == df_list[1]['Tm'][i][-1]))):
                isTeam2Playoff = True
            if ((self._altTeam2Name == df_list[0]['Tm'][i][0:3]) and ((i % 5 == 1) or ('*' == df_list[0]['Tm'][i][-1]))) or ((self._altTeam2Name == df_list[0]['Tm'][i][0:3]) and ( (self._homeTeam.rank <=13 ) or ('+' == df_list[0]['Tm'][i][-1]))):
                isTeam2Playoff = True
        return isTeam1Playoff, isTeam2Playoff

    def _findConferences(self):
        url = MAIN_URL
        teamOneConf = 'AFC'
        teamTwoConf = 'AFC'
        df_list = pd.read_html(url)
        for i in range(0,len(df_list[1]['Tm'])):
            if self._altTeam1Name == df_list[1]['Tm'][i][0:3]:
                teamOneConf = 'NFC'
            if self._altTeam2Name == df_list[1]['Tm'][i][0:3]:
                teamTwoConf = 'NFC'
        return teamOneConf, teamTwoConf
    

    def _setGameValue(self, boxscoreString):
        """
        Calculates the value of the game according to the algorithem.
        """
        counterValue = 0.0
        self._gameSummary = self._boxscore.summary
        self._homePoints = self._boxscore.home_points
        self._awayPoints = self._boxscore.away_points
        self._totalPoints = self._homePoints + self._awayPoints
        self._thirdQuarterAway = sum(self._gameSummary['away'][:3])
        self._thirdQuarterHome = sum(self._gameSummary['home'][:3])
        self._diffThird = abs(self._thirdQuarterHome - self._thirdQuarterAway)
        self._diffPoints = abs(self._homePoints - self._awayPoints)
        self._isOvertime = self._game.overtime
        self._lastMinWin, self._counterChangeLead = self._calGameScores()
        self._isTeamOnePlayoffs, self._isTeamTwoPlayoffs = self._inPlayoffPic()
        self._percentageDiff = abs(self._winningTeam.win_percentage - self._losingTeam.win_percentage)
        self._rankDiff = abs(self._winningTeam.rank - self._losingTeam.rank)
        self._team1Conf, self._team2Conf = self._findConferences()
        self._totalYards = self._boxscore.away_total_yards + self._boxscore.home_total_yards
        self._diffYards = abs(self._boxscore.away_total_yards - self._boxscore.home_total_yards)
        self._totalMinPoss = int(self._boxscore.away_time_of_possession[0:2]) + int(self._boxscore.home_time_of_possession[0:2])
        self._diffMinPoss = abs(int(self._boxscore.away_time_of_possession[0:2]) - int(self._boxscore.home_time_of_possession[0:2]))


        "first parameter"
        if(self._diffPoints == 0):
            self.firstValue = 2.0
        elif (self._totalPoints / self._diffPoints) >= 6:
            self.firstValue = 2.0
        
        "second parameter"
        if(self._diffThird <= 6):
            self.secondValue = 1.0

        "third parameter"
        if self._isOvertime:
            self.thirdValue = 2.0

        "forth parameter"
        if self._lastMinWin:
            self.forthValue = 3.0

        "fifth parameter"
        self.fifthValue = self._counterChangeLead / 2.0

        "sixth parameter"
        if (((self._winningTeam.win_percentage >= 0.65) or (self._winningTeam.rank <= 10)) and ((self._losingTeam.win_percentage >= 0.65) or (self._losingTeam.rank <= 10))):
            self.sixthValue = 3.0

        "seventh parameter"
        if(self._isTeamOnePlayoffs and self._isTeamTwoPlayoffs):
            self.seventhValue = 2.0

        "Eighth parameter"
        if (self._percentageDiff >= 0.3 or self._rankDiff >= 8) and (self._winningTeam.rank > self._losingTeam.rank):
            self.eightValue = 2.0

        "Ninth parameter"
        if(self._team1Conf == self._team2Conf):
            self.ninthValue = 1.0

        "Tenth parameter"
        if (self._totalYards >= 700 and (self._diffYards / self._totalYards) <= 0.1):
            self.tenthValue = 2.0
        
        "Eleventh parameter"
        #need to set parameters - now are arbitrary
        if(self._game.quarterback_rating >= 75):
             self.eleventhValue = 2.0

        "Twolth parameter"
        if(self._diffMinPoss / self._totalMinPoss) <= 0.05:
            self.twelthValue = 1.0
        
        self._gameValue = self.firstValue + self.secondValue + self.thirdValue + self.forthValue + self.fifthValue + self.sixthValue + self.seventhValue + self.eightValue + self.ninthValue + self.tenthValue + self.eleventhValue + self.twelthValue
        

        

        
        
             


"""
    def _calGameScores2(self, boxscoreString):
        url = BOXSCORE_URL % boxscoreString
        lastMinScore = False
        counterLeadChanges = 0 
        lastScoreWin = 0
        lastScoreLose = 0
        winningTeam = self._boxscore.winning_abbr
        losingTeam = self._boxscore.losing_abbr
        df_list = pd.read_html(url)
        quarter = 'nan'
        for i in range(0,len(df_list[1]['Quarter'])):
            diffBefore = lastScoreWin - lastScoreLose 
            diffNow = int(df_list[1][winningTeam][i]) - int(df_list[1][losingTeam][i])
            if(diffBefore < 0 and diffNow >= 0) or (diffBefore > 0 and diffNow <= 0):
                counterLeadChanges+= 1
            if(str(df_list[1]['Quarter'][i]) != 'nan'):
                quarter = str(df_list[1]['Quarter'][i])
            timePlay = str(df_list[1]['Time'][i])
            if(quarter == "4.0" and  (int(timePlay[0]) < 3) and timePlay[1] == ':'):
                if(lastScoreWin - lastScoreLose <= 0) and (int(df_list[1][winningTeam][i]) - int(df_list[1][losingTeam][i]) > 0):
                    lastMinScore = True
            lastScoreLose = int(df_list[1][losingTeam][i])
            lastScoreWin = int(df_list[1][winningTeam][i])    
        return lastMinScore, counterLeadChanges
"""