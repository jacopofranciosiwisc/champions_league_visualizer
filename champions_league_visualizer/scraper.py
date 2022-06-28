import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


class GroupStage:
    def __init__(self, Place, Team, PTS, GP, W, L, D, GF, GA, GD):
        self.Place = Place
        self.Team = Team
        self.PTS = PTS
        self.GP = GP
        self.W = W
        self.L = L
        self.D = D
        self.GF = GF
        self.GA = GD
        self.GD = GD


url = 'https://www.sportingnews.com/us/soccer/news/uefa-champions-league-group-standings-results-match-schedule/z7rxlzuxzlb01kl1ilcra9fz7'

page = requests.get(url)

soup = bs(page.content, 'html.parser')

tables = soup.findAll("table", {"class": "table-retro-standard"})

# print(pd.read_html(str(table)))
all_tables = []
for table in tables:
    all_tables.append(pd.read_html(str(table))[0])

df = pd.concat(all_tables)
df.to_csv('groupStage2022.csv')
