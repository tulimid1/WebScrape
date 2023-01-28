from scrapeBasketballScores import scrapeBasketballScores

todays_bball_scores = scrapeBasketballScores()
n_games = todays_bball_scores.get_number_of_game_summaries()
for i_game in range(n_games-1):
    todays_bball_scores.visualize_game_scores(game_number=i_game+1)
