# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 13:44:45 2025

@author: sebas
"""

from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
from datetime import datetime

# =========================
# Date range
# =========================
start_date = "12/18/2025"
end_date = datetime.today().strftime("%m/%d/%Y")

# =========================
# Download NBA game data
# =========================
gamefinder = leaguegamefinder.LeagueGameFinder(
    date_from_nullable=start_date,
    date_to_nullable=end_date
)

df = gamefinder.get_data_frames()[0]

# =========================
# Keep only HOME games
# =========================
df = df[df["MATCHUP"].str.contains(" vs. ", na=False)]

# =========================
# Remove duplicate games
# =========================
df = df.drop_duplicates(subset="GAME_ID")

# =========================
# Column order (STRICT)
# =========================
final_columns = [
    "SEASON_ID",
    "TEAM_ID",
    "TEAM_ABBREVIATION",
    "TEAM_NAME",
    "GAME_ID",
    "GAME_DATE",
    "MATCHUP",
    "WL",
    "MIN",
    "FGM",
    "FGA",
    "FG_PCT",
    "FG3M",
    "FG3A",
    "FG3_PCT",
    "FTM",
    "FTA",
    "FT_PCT",
    "OREB",
    "DREB",
    "REB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "PLUS_MINUS"
]

# =========================
# Keep only requested columns
# =========================
df = df[final_columns]

# =========================
# Preview
# =========================
print(df.head(15))
print("\nColumns in output:")
print(df.columns.tolist())

# =========================
# Export
# =========================
df.to_csv("nba_games_home_only_since_yesterday.csv", index=False)

print("✅ File generated: nba_games_home_only_since_yesterday.csv")
