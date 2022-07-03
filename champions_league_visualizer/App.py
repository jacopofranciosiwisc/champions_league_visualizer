from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_csv(
        'data\groupStage2022.csv', header=0)
    df = df.rename(columns={'Unnamed: 0': 'Place'})
    df['Place'] = df['Place'] + 1

    # Cleaning the team column of dataframe
    all_teams = df['Team'].to_list()
    new_teams = []
    for team in all_teams:
        team = team[2:]
        if "(X)" in team:
            team = team[:-4]
        new_teams.append(team)
    df['Team'] = new_teams

    groups = "ABCDEFGH"
    return render_template('index.html', table=df, groups=groups)


if __name__ == "__main__":
    app.run(debug=True)
