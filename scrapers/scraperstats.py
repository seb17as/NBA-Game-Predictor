# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 16:16:24 2025

@author: sebas
"""

from nba_api.stats.endpoints import leaguedashteamstats
import pandas as pd

# =========================
# Parameters
# =========================
season = "2025-26"        # ejemplo
season_type = "Regular Season"

# =========================
# Call API
# =========================
team_stats = leaguedashteamstats.LeagueDashTeamStats(
    season=season,
    season_type_all_star=season_type,
    per_mode_detailed="PerGame"   # MUY IMPORTANTE
)

df = team_stats.get_data_frames()[0]

# =========================
# Preview
# =========================
print(df.head())
print("\nColumns:")
print(df.columns.tolist())

# =========================
# Optional: sort by WIN%
# =========================
df = df.sort_values("W_PCT", ascending=False)

# =========================
# Export
# =========================
df.to_csv("nba_team_stats_per_game.csv", index=False)

print("✅ File generated: nba_team_stats_per_game.csv")
