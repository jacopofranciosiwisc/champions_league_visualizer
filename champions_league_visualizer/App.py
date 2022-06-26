from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello():
    url = 'https://www.sportingnews.com/us/soccer/news/uefa-champions-league-group-standings-results-match-schedule/z7rxlzuxzlb01kl1ilcra9fz7'

    page = requests.get(url)

    soup = bs(page.content, 'html.parser')

    tables = soup.findAll("table", {"class": "table-retro-standard"})

    all_tables = []
    for table in tables:
        all_tables.append(pd.read_html(str(table))[0])

    return render_template('index.html', group_tables=all_tables)


if __name__ == "__main__":
    app.run()
