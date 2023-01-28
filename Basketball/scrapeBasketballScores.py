import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import savingfigures as sf
import os

plt.style.use(["ggplot", "dark_background"])
plt.rcParams.update({"font.size": 20, "lines.linewidth": 5})


class scrapeBasketballScores:

    website_html = str
    website_soup = BeautifulSoup

    def __init__(self):
        self.website_html = self.get_website_html()
        self.website_soup = self.convert_html_to_soup()

    def visualize_game_scores(self, game_number: int = 1):
        os.chdir("Basketball")
        fig = plt.figure()
        score_dict = self.get_team_scores(game_number=game_number)
        for (team_name, score_values) in score_dict.items():
            sns.lineplot(
                x=self.get_quarters_played(game_number=game_number),
                y=np.cumsum(score_values),
                label=team_name,
            )
        plt.xlabel("Quarter")
        plt.ylabel("Score")
        team_names_full = self.get_team_names(game_number=game_number)
        team_names_abbrev = list(score_dict.keys())
        plt.title(
            team_names_full[0]
            + " ["
            + str(np.sum(score_dict[team_names_abbrev[0]]))
            + "]"
            + "\n"
            + team_names_full[1]
            + " ["
            + str(np.sum(score_dict[team_names_abbrev[1]]))
            + "]"
        )
        sf.auto_save(fig, fig_name=team_names_abbrev[0] + "_v_" + team_names_abbrev[1])
        os.chdir("..")

    def get_team_scores(self, game_number: int = 1) -> dict:
        # team names
        winner_abbreviation = self.website_soup.select(
            "#scores > div.game_summaries > div:nth-child("
            + str(game_number)
            + ") > table:nth-child(2) > tbody > tr:nth-child(1) > td:nth-child(1) > a"
        )[0].getText()
        loser_abbreviation = self.website_soup.select(
            "#scores > div.game_summaries > div:nth-child("
            + str(game_number)
            + ") > table:nth-child(2) > tbody > tr:nth-child(2) > td:nth-child(1) > a"
        )[0].getText()
        score_dict = {winner_abbreviation: [], loser_abbreviation: []}
        # team scores
        all_centers = self.website_soup.find_all("td", {"class": "center"})
        n_quarters_played = len(self.get_quarters_played(game_number=game_number))
        n_scores_to_get = n_quarters_played * 2
        game_score_index_add = 0
        for i_game in range(game_number - 1):
            game_score_index_add += len(self.get_quarters_played(i_game + 1)) * 2
        all_scores = all_centers[
            30 + game_score_index_add : 30 + game_score_index_add + n_scores_to_get + 1
        ]
        for i_score in range(n_quarters_played):
            score_dict[winner_abbreviation].append(int(all_scores[i_score].getText()))
            score_dict[loser_abbreviation].append(
                int(all_scores[i_score + n_quarters_played].getText())
            )
        return score_dict

    def get_team_names(self, game_number: int = 1) -> list:
        winner = self.website_soup.select(
            "#scores > div.game_summaries > div:nth-child("
            + str(game_number)
            + ") > table.teams > tbody > tr.winner > td:nth-child(1) > a"
        )[0].getText()
        loser = self.website_soup.select(
            "#scores > div.game_summaries > div:nth-child("
            + str(game_number)
            + ") > table.teams > tbody > tr.loser > td:nth-child(1) > a"
        )[0].getText()
        return [winner, loser]

    def get_quarters_played(self, game_number: int = 1) -> list:
        html_elements = self.website_soup.select(
            "#scores > div.game_summaries > div:nth-child("
            + str(game_number)
            + ") > table:nth-child(2) > thead > tr"
        )
        quarters_text = html_elements[0].getText()
        acceptable_quarters = ["1", "2", "3", "4", "O"]
        quarters_played = []
        for (idx, i_str) in enumerate(quarters_text):
            is_acceptable_quarter_str = i_str in acceptable_quarters
            if is_acceptable_quarter_str:
                game_had_OT = i_str == "O"
                if not game_had_OT:
                    quarters_played.append(i_str)
                elif game_had_OT:
                    quarters_played.append(quarters_text[idx : idx + 2])
        return quarters_played

    def get_number_of_game_summaries(self) -> int:
        all_game_summaries_classes = self.website_soup.find_all(
            "div", {"class": "game_summary expanded nohover"}
        )
        return len(all_game_summaries_classes)

    def convert_html_to_soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.website_html, "html.parser")

    def get_website_html(self) -> str:
        downloaded_html = requests.get("https://www.basketball-reference.com/")
        try:
            downloaded_html.raise_for_status()
            website_html = downloaded_html.text
        except:
            with open(
                "Basketball/BBall_01_27_2023.html", "r", encoding="utf-8"
            ) as html_file:
                website_html = html_file.read()
        return website_html
