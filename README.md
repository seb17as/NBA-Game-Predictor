# 🏀 NBA Game Predictor

Machine learning model that predicts the outcome of NBA games (home team win/loss) using team box score statistics.

## Overview

This project uses **XGBoost** to classify NBA game outcomes based on per-game team statistics like field goal percentage, rebounds, assists, steals, blocks, and turnovers — for both the home and away teams.

The model is trained on historical game data scraped from the official NBA Stats API and can predict the outcome of any upcoming matchup by pulling current season averages.

## Features

- XGBoost classifier with tuned hyperparameters (~450 estimators, learning rate 0.05)
- 80/20 stratified train/test split
- Feature importance visualization
- Confusion matrix evaluation
- Predict any specific matchup using current team stats
- Automated data collection via custom scrapers (NBA Stats API)

## Project Structure
```
NBA-Game-Predictor/
├── README.md
├── NBAPredictorV4.ipynb      # Main notebook: EDA, model training, evaluation, predictions
├── requirements.txt
└── scrapers/
    ├── scraperhome.py         # Scrapes home team game logs
    ├── scraperaway.py         # Scrapes away team game logs
    └── scraperstats.py        # Scrapes per-game team stats for current season
```

## Model Features

| Home Team | Away Team |
|-----------|-----------|
| FG% | FG% |
| 3PT% | 3PT% |
| FT% | FT% |
| Rebounds | Rebounds |
| Assists | Assists |
| Steals | Steals |
| Blocks | Blocks |
| Turnovers | Turnovers |

## Tech Stack

- Python 3
- XGBoost
- scikit-learn
- pandas / NumPy
- matplotlib
- nba_api

## Setup
```bash
pip install -r requirements.txt
```

### requirements.txt
```
pandas
numpy
scikit-learn
xgboost
matplotlib
nba_api
```

## Usage

1. Run the scrapers to collect fresh data:
```bash
python scrapers/scraperhome.py
python scrapers/scraperaway.py
python scrapers/scraperstats.py
```

2. Open `NBAPredictorV4.ipynb` and run all cells to train the model and make predictions.
