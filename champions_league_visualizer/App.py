from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os

DATA_FOLDER = os.path.join('data', 'tourney-template')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DATA_FOLDER

@app.route('/')
def home():
    return "Welcome to the Champions League Visualizer!"



@app.route('/2022')
def index():
    tournament_template = os.path.join(app.config['UPLOAD_FOLDER'], 'tournament-template.jpg')

    df = pd.read_csv('champions_league_visualizer\data\groupStage2022.csv', header=0)
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

    return render_template('index.html', table=df, group_teams=new_teams, user_image = tournament_template)


if __name__ == "__main__":
    app.run(debug=True)
