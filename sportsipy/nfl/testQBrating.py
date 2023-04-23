# Purpose: test the QBrating class
from nfl.weekly_games_Jonah import WeeklyGames

games10 = WeeklyGames(10, 2022)
games11 = WeeklyGames(11, 2022)

sumRatings = sum(games10._qb_ratings + games11._qb_ratings) 
amountGames = len(games10._qb_ratings) + len(games11._qb_ratings)

print("amount of games: " + str(amountGames))
print("average score: " + str(sumRatings/amountGames))
print("----------games10----------")
print(games10._qb_ratings)
print("----------games11----------")
print(games11._qb_ratings)

"""
amount of games: 28
----------games10----------
[89.0, 115.1, 78.6, 113.6, 129.6, 135.0, 153.3, 94.1, 79.7, 109.5, 146.7, 96.5, 94.3, 94.2]   
----------games11----------
[127.3, 100.2, 116.3, 107.1, 77.9, 149.6, 104.6, 83.0, 76.5, 106.5, 139.3, 104.1, 120.8, 131.9]
"""