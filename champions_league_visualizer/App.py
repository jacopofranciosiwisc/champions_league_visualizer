from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_csv(
        'champions_league_visualizer\data\groupStage2022.csv', header=0)

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
    ks_df = pd.read_csv(
        'champions_league_visualizer/data/knockoutStage2022.csv')
    ks_df['total_Tm1'] = ks_df[' Gm1Tm1'] + ks_df[' Gm2Tm1']
    ks_df['total_Tm2'] = ks_df[' Gm1Tm2'] + ks_df[' Gm2Tm2']

    return render_template('index.html', table=df, group_teams=new_teams, knockout=ks_df)


if __name__ == "__main__":
    app.run(debug=True)
