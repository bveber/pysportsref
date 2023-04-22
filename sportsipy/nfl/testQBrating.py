# Purpose: test the QBrating class
from nfl.weekly_games_Jonah import WeeklyGames

games10 = WeeklyGames(10, 2022)
games11 = WeeklyGames(11, 2022)

sumRatings = sum(games10.qb_ratings + games11.qb_ratings) 
amountGames = len(games10.qb_ratings) + len(games11.qb_ratings)

print("amount of games: " + str(amountGames))
print("average score: " + str(amountGames))
print("----------games10----------")
print(games10.qb_ratings)
print("----------games11----------")
print(games11.qb_ratings)
