from mysql.connector import Error
from expert import SongConsult
import mysql.connector
import pandas as pd
import os
import warnings

#FOR FINAL USE ONLY, IMPORTANT CODE WARNINGS MAY BE IGNORED WHILE DEBUGGING!
warnings.filterwarnings("ignore")

songs_list, songs_features_list = [], []
song_features_map, songs_desc_map = {}, {}

#creates connection to MySQL local DB
def create_server_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
        host = host_name,
        user = user_name,
        passwd = user_password,
        database = database,
        buffered = True)
    except Error as err:
        print(f"Error: '{err}'")
    return connection
connection = create_server_connection("localhost", "root", "Hotmail1255.", "dj_patas")

#gets a disease list from DB 
def get_DB_songs(cursor):
    cursor.execute('SELECT song FROM dj_patas.songs')
    songs = []
    for row in cursor:
        for field in row:
            songs.append(field)
    return songs

#loads the knowledge from MySQL DB into variables
def process_DB_knowledge():
    cursor = connection.cursor()
    songs_list = get_DB_songs(cursor)

    for song in songs_list:
        cursor.execute(f"SELECT {song} FROM dj_patas.features")
        features = []
        for row in cursor:
            for field in row:
                features.append(field)
        songs_features_list.append(features)
        song_features_map[str(features)] = song

        cursor.execute(f"SELECT description FROM dj_patas.songs WHERE song = '{song}'")
        description =  pd.read_sql(f"SELECT description FROM dj_patas.songs WHERE song = '{song}'", connection)
        songs_desc_map[song] = description.iloc[0,0]


def get_song_desc(song): return songs_desc_map[song]


def if_unmatched(song):
    song_desc = get_song_desc(song)
    os.system('cls')
    print(f"The song that mostly match you rn is: {song}, {song_desc}\n")
    #print(f"{song_desc}\n")
    print(f"-----------------------------------------------")

#program entry point for greeting class creation and loop while user exits the program
if __name__ == "__main__":
    process_DB_knowledge()
    engine = SongConsult(song_features_map, if_unmatched, get_song_desc)

    while 1:
        engine.reset()
        engine.run()
        print("\nEnter any key to find another song or enter 'EXIT' to quit...")
        if input().lower() == "exit":
            exit()