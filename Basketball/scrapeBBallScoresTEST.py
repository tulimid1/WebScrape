import unittest
from scrapeBasketballScores import scrapeBasketballScores
from bs4 import BeautifulSoup


class scrapeBBallScoresTEST(unittest.TestCase):

    todays_bball_scores = scrapeBasketballScores

    @classmethod
    def setUp(self):
        self.todays_bball_scores = scrapeBasketballScores()

    ## Visualize
    # def test_visualize_game_scores(self):
    #     self.todays_bball_scores.visualize_game_scores()

    def test_visualize_game_scores_is_method(self):
        self.assertTrue("visualize_game_scores" in dir(self.todays_bball_scores))

    ## Get scores
    def test_get_teams_scores_return_Pistons_v_Nets(self):
        self.assertEqual(
            self.todays_bball_scores.get_team_scores(game_number=2),
            {"DET": [30, 28, 43, 29], "BRK": [27, 32, 31, 32]},
        )

    def test_get_teams_scores_return_Knicks_v_Celtics(self):
        self.assertEqual(
            self.todays_bball_scores.get_team_scores(),
            {"NYK": [26, 32, 33, 19, 10], "BOS": [34, 26, 25, 25, 7]},
        )

    def test_get_team_scores_returns_dict(self):
        self.assertIsInstance(self.todays_bball_scores.get_team_scores(), dict)

    def test_get_team_scores_is_method(self):
        self.assertTrue("get_team_scores" in dir(self.todays_bball_scores))

    ## Get team names
    def test_get_team_names_return_Pistons_Nets(self):
        self.assertEqual(
            self.todays_bball_scores.get_team_names(game_number=2),
            ["Detroit Pistons", "Brooklyn Nets"],
        )

    def test_get_team_names_return_Knicks_Celtics(self):
        self.assertEqual(
            self.todays_bball_scores.get_team_names(),
            ["New York Knicks", "Boston Celtics"],
        )

    def test_get_team_names_returns_list(self):
        self.assertIsInstance(self.todays_bball_scores.get_team_names(), list)

    def test_get_team_names_is_method(self):
        self.assertTrue("get_team_names" in dir(self.todays_bball_scores))

    ## Get quarter played
    def test_get_quarters_played_return_1_to_4(self):
        self.assertEqual(
            self.todays_bball_scores.get_quarters_played(game_number=2),
            ["1", "2", "3", "4"],
        )

    def test_get_quarters_played_return_1_to_OT(self):
        self.assertEqual(
            self.todays_bball_scores.get_quarters_played(), ["1", "2", "3", "4", "OT"]
        )

    def test_get_quarters_played_returns_list(self):
        self.assertIsInstance(self.todays_bball_scores.get_quarters_played(), list)

    def test_get_quarters_played_is_method(self):
        self.assertTrue("get_quarters_played" in dir(self.todays_bball_scores))

    ## Get number of game summaries
    def test_get_number_of_game_summaries_return_6(self):
        self.assertEqual(self.todays_bball_scores.get_number_of_game_summaries(), 6)

    def test_get_number_of_game_summaries_return_int(self):
        self.assertIsInstance(
            self.todays_bball_scores.get_number_of_game_summaries(), int
        )

    def test_get_number_of_game_summaries_is_method(self):
        self.assertTrue("get_number_of_game_summaries" in dir(self.todays_bball_scores))

    ## Convert html to soup
    def test_website_soup_is_bs(self):
        self.assertIsInstance(self.todays_bball_scores.website_soup, BeautifulSoup)

    def test_website_soup_is_attr(self):
        self.assertTrue(hasattr(self.todays_bball_scores, "website_soup"))

    def test_convert_html_to_soup_return_soup(self):
        self.assertIsInstance(
            self.todays_bball_scores.convert_html_to_soup(), BeautifulSoup
        )

    def test_convert_html_to_soup_method(self):
        self.assertTrue("convert_html_to_soup" in dir(self.todays_bball_scores))

    ## Get website html
    def test_website_html_attr_is_str(self):
        self.assertIsInstance(self.todays_bball_scores.website_html, str)

    def test_website_html_is_attribute(self):
        self.assertTrue(hasattr(self.todays_bball_scores, "website_html"))

    def test_get_website_html_is_html(self):
        self.assertTrue("DOCTYPE" in self.todays_bball_scores.get_website_html())

    def test_get_website_html_return_str(self):
        self.assertIsInstance(self.todays_bball_scores.get_website_html(), str)

    def test_get_website_html_method(self):
        self.assertTrue("get_website_html" in dir(self.todays_bball_scores))


if __name__ == "__main__":
    unittest.main()
