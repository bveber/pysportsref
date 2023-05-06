# Purpose: test the QBrating class
from nfl.weekly_games_Jonah import WeeklyGames

games1 = [89.0, 115.1, 78.6, 113.6, 129.6, 135.0, 153.3, 94.1, 79.7, 109.5, 146.7, 96.5, 94.3, 94.2]   
games2 = [127.3, 100.2, 116.3, 107.1, 77.9, 149.6, 104.6, 83.0, 76.5, 106.5, 139.3, 104.1, 120.8, 131.9]
all_games = games1 + games2
games1.sort()
games2.sort()
all_games.sort()
print("games1: " + str(games1))
print("games2: " + str(games2))
print("general: " + str(all_games))
print("games1 Average: " + str(sum(games1)/len(games1)))
print("games2 Average: " + str(sum(games2)/len(games2)))
print("games1 Median: " + str(games1[len(games1)//2]))
print("games2 Median: " + str(games2[len(games2)//2]))
print("general Average: " + str(sum(all_games)/len(all_games)))
print("general Median: " + str(all_games[len(all_games)//2]))
print("general top 10% threshold: " + str(all_games[(len(all_games)*9)//10]))
print("general top 25% threshold: " + str(all_games[(len(all_games)*3)//4]))
print("general top 30% threshold: " + str(all_games[(len(all_games)*7)//10]))
print("general top 40% threshold: " + str(all_games[(len(all_games)*6)//10]))

"""
------------------TEST RESULTS------------------
games1 Average: 109.22857142857143
games2 Average: 110.36428571428571
games1 Median: 109.5
games1 Median: 109.5
games2 Median: 107.1
general Average: 109.79642857142856
general Median: 107.1
general top 10% threshold: 146.7
general top 25% threshold: 129.6
general top 30% threshold: 120.8
general top 40% threshold: 113.6
"""

"""
------------------TESTING TO GET GAMES QB RATING INFO------------------
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

amount of games: 28
----------games10----------
[89.0, 115.1, 78.6, 113.6, 129.6, 135.0, 153.3, 94.1, 79.7, 109.5, 146.7, 96.5, 94.3, 94.2]   
----------games11----------
[127.3, 100.2, 116.3, 107.1, 77.9, 149.6, 104.6, 83.0, 76.5, 106.5, 139.3, 104.1, 120.8, 131.9]
"""