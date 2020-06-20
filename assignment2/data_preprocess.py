import sqlite3
import zipfile
import pandas as pd
import json
import datetime
import numpy as np
from players import *

'''
FORMATTING CONSTANTS
'''
SEPARATOR = "***********************************************"

'''
INPUT DATA Constants
'''
INPUTFILE_DIR = "/root/content/"
INPUTZIPFILE = "soccer.zip"
DATABASENAME = "database.sqlite"

'''
SQL STATEMENTS
'''
SHOW_TABLES_SQL = "SELECT name FROM sqlite_master WHERE type='table' " \
                  "ORDER BY name;"
DESC_TABLES_SQL = "DESC"

AWAY_PLAYER_COLUMNS = ["away_player_1", "away_player_2", "away_player_3",
                       "away_player_4", "away_player_5", "away_player_6",
                       "away_player_7", "away_player_8", "away_player_9",
                       "away_player_10", "away_player_11"]

HOME_PLAYER_COLUMNS = ['home_player_1', 'home_player_2', 'home_player_3',
                       "home_player_4", "home_player_5", "home_player_6",
                       "home_player_7", "home_player_8", "home_player_9",
                       "home_player_10", "home_player_11"]

PLAYER_TYPES = ['Attacker', 'Defender', 'Goalkeeper', 'Midfielder']

# TODO: Move SKILL COLUMNS to Utils.py
SKILL_COLUMNS = ['finishing', 'sliding_tackle',
                 'gk_reflexes', 'short_passing']

def select_all_query_table(table_name):
  return "SELECT * from " + table_name

def sql_to_dataframe(conn, sql):
  df = pd.read_sql_query(sql, conn)
  return df


def map_country_to_name(countries_df, country_id):
  return countries_df.loc[countries_df['id'] == country_id, 'name']

######################## PRE-PROCESS ###########################

def uncompress_and_open_sqlite():
  zip = zipfile.ZipFile(INPUTFILE_DIR + INPUTZIPFILE)
  zip.extractall(path=INPUTFILE_DIR)
  conn = sqlite3.connect(INPUTFILE_DIR + DATABASENAME)
  return conn


def execute_query_print_results(conn, sql_query):
  cur = conn.cursor()
  cur.execute(sql_query)
  rows = cur.fetchall()
  for row in rows:
    print row


def desc_table(table_df, table_name):
  print SEPARATOR
  print "For table " + table_name + " there are " + str(table_df.shape[0]) + \
        " entries with " + str(table_df.shape[1]) + " features"
  print table_df.columns.tolist()
  print SEPARATOR


def home_advantage(matches_df, conn):
  # TODO: Convert to DataFrama and Plot
  country_id_to_num_matches = matches_df[['country_id', 'result_label']].copy()
  grouped_df = country_id_to_num_matches.\
    groupby(['country_id'], as_index=False).agg({'result_label':'count'}).rename(columns={'result_label': 'matches_per_country'})

  win_df = country_id_to_num_matches[country_id_to_num_matches['result_label']=='HOME_WIN']
  grouped_home_df = win_df. \
    groupby(['country_id'], as_index=False).agg({'result_label':'count'}).rename(columns={'result_label': 'home_wins_per_country'})
  join_df = pd.merge(grouped_df, grouped_home_df, on='country_id',
                            how='outer')
  join_df['percentage_home_win']= join_df.apply(
      lambda r: np.true_divide(r['home_wins_per_country'], r['matches_per_country']) * 100., axis=1)

  countries_df = sql_to_dataframe(conn, select_all_query_table("Country"))
  join_df_name = pd.merge(countries_df, join_df, left_on = 'id', right_on='country_id',
                          how='outer')
  return join_df_name[['name', 'percentage_home_win']]


def get_team_name_to_team_api_id_dict(team_df):
  team_name_to_team_api_id = dict(zip( team_df.team_long_name, team_df.team_api_id))
  return team_name_to_team_api_id

def get_team_api_dict_to_team_name(team_df):
  team_api_id_to_team_name = dict(zip(team_df.team_api_id, team_df.team_long_name))
  return team_api_id_to_team_name


if __name__ == '__main__':
  conn = uncompress_and_open_sqlite()
  get_team_name_to_team_api_id_dict()

######################## PLAYERS ###########################

'''
Classify players into midfield, defense, attacking
'''
def player_to_player_type(players_skills, player_names_df, player_name,
    COLUMNS_OF_INTEREST):
  """
  Takes in as an input the relevant player skills and classifies into
  midfielder, attacker, defender or goalie; based on the most recent numbers
  from the database.
  """
  player_join_df = pd.merge(players_skills, player_names_df, on='player_api_id',
                            how='outer')
  my_player_df = (
    player_join_df[player_join_df['player_name'].str.contains(player_name)])
  most_recent_date = my_player_df['date'].max()
  latest_df = my_player_df[my_player_df['date'] == most_recent_date]
  latest_skills_df = latest_df[['finishing', 'sliding_tackle',
                                  'gk_reflexes', 'short_passing']]
  # TODO: Convert this to lambda function; see matches.result method
  latest_skills_df['player_type'] = latest_skills_df.idxmax(axis=1)
  latest_skills_df['player_name'] = player_name
  latest_skills_df['player_api_id'] = latest_df['player_api_id']
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'finishing', 'Attacker', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'short_passing', 'Midfielder', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'sliding_tackle', 'Defender', latest_skills_df['player_type'])
  latest_skills_df['player_type'] = np.where(latest_skills_df['player_type'] ==
                                             'gk_reflexes', 'Goalkeeper', latest_skills_df['player_type'])

  return latest_skills_df[['player_name', 'player_type', 'player_api_id']]

def player_api_id_to_player_type(players_skills, COLUMNS_OF_INTEREST, player_api_id):
  """
  Takes in as an input the relevant player skills and classifies into
  midfielder, attacker, defender or goalie; based on the most recent numbers
  from the database.
  """
  my_player_df = players_skills[players_skills['player_api_id'] == player_api_id]
  most_recent_date = my_player_df['date'].max()
  latest_df = my_player_df[my_player_df['date'] == most_recent_date]
  latest_skills_df = latest_df[COLUMNS_OF_INTEREST]
  latest_skills_df['player_type'] = latest_skills_df.idxmax(axis=1)
  max_skill = latest_skills_df['player_type'].values[0]
  if max_skill == 'finishing':
    return 'Attacker'

  if max_skill == 'sliding_tackle':
    return 'Defender'

  if max_skill == 'short_passing':
    return 'Midfielder'

  if max_skill == 'gk_reflexes':
    return 'Goalkeeper'


def player_rating(player_api_id, last_date, players_ratings_label):
  """
  Gets the rating for a season for a player_api_id, based on the closest date
  :param player_api_id:
  :return:
  """
  all_player_ratings_df = players_ratings_label[
    players_ratings_label['player_api_id'] == player_api_id]
  pivot = datetime.datetime.strptime(last_date, "%Y-%m-%d").date()
  all_player_ratings_df.date = pd.to_datetime(all_player_ratings_df.date)
  min_date = (nearest(all_player_ratings_df.date, pd.to_datetime(last_date)))
  return all_player_ratings_df[all_player_ratings_df.date == min_date]

def nearest(items, pivot):
  value = min(items, key=lambda x: abs(pivot - x))
  return value

def average_team_rating(match_df):
  return None
