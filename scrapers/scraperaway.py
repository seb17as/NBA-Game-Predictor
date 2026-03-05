from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
from datetime import datetime

# Configuración del rango de fechas
start_date = "12/18/2025"
end_date = datetime.today().strftime("%m/%d/%Y")

# Descargar datos
gamefinder = leaguegamefinder.LeagueGameFinder(date_from_nullable=start_date,
                                                date_to_nullable=end_date)
df = gamefinder.get_data_frames()[0]

# Filtrar solo partidos donde el equipo fue visitante (MATCHUP contiene "@")
df_away = df[df['MATCHUP'].str.contains(" @ ")]

# Eliminar duplicados por ID del partido
df_away = df_away.drop_duplicates(subset="GAME_ID")

# Renombrar columnas para estadísticas del equipo visitante
df_away = df_away.rename(columns={
    "GAME_ID": "game_id",
    "GAME_DATE": "game_date",
    "TEAM_ID": "team_id_away",
    "TEAM_ABBREVIATION": "team_abbreviation_away",
    "TEAM_NAME": "team_name_away",
    "MATCHUP": "matchup_away",
    "WL": "wl_away",
    "FGM": "fgm_away",
    "FGA": "fga_away",
    "FG_PCT": "fg_pct_away",
    "FG3M": "fg3m_away",
    "FG3A": "fg3a_away",
    "FG3_PCT": "fg3_pct_away",
    "FTM": "ftm_away",
    "FTA": "fta_away",
    "FT_PCT": "ft_pct_away",
    "OREB": "oreb_away",
    "DREB": "dreb_away",
    "REB": "reb_away",
    "AST": "ast_away",
    "STL": "stl_away",
    "BLK": "blk_away",
    "TOV": "tov_away",
    "PF": "pf_away",
    "PTS": "pts_away",
    "PLUS_MINUS": "plus_minus_away"
})

# Seleccionar columnas deseadas (ordenadas)
columns_away = [
    "game_id", "game_date",
    "team_id_away", "team_abbreviation_away", "team_name_away", "matchup_away", "wl_away",
    "fgm_away", "fga_away", "fg_pct_away", "fg3m_away", "fg3a_away", "fg3_pct_away",
    "ftm_away", "fta_away", "ft_pct_away", "oreb_away", "dreb_away", "reb_away",
    "ast_away", "stl_away", "blk_away", "tov_away", "pf_away", "pts_away", "plus_minus_away"
]
df_away = df_away[columns_away]

# Mostrar primeras 15 filas
print(df_away.head(15))

# Exportar a CSV
df_away.to_csv("nba_away_stats_since_yesterday.csv", index=False)
print("✅ Archivo generado: nba_away_stats_since_yesterday.csv")
