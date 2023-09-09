import requests
import json
import mysql.connector
from typing import List
from card import Card


HOSTNAME = "localhost"
USERNAME = "root"
DBNAME = "YGOCards"
MAIN_TABLE_NAME = "cards"

resp: requests.Response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
all_card_data: List[dict] = json.loads(resp.text)["data"]
cards: List[Card] = [Card(card_data) for card_data in all_card_data]

serverConnection = mysql.connector.connect(
    host=HOSTNAME,
    user=USERNAME,
)
serverCursor = serverConnection.cursor()

serverCursor.execute("SHOW DATABASES")
# cursor execution results are lists of tuples
# in this case first item of each tuple is the name of a db
if DBNAME not in [results[0] for results in serverCursor]:
    # create the yu-gi-oh card db if it doesn't exist
    serverCursor.execute(f"CREATE DATABASE {DBNAME}")

schemaConnection = mysql.connector.connect(
    host=HOSTNAME,
    user=USERNAME,
    database=DBNAME
)
schemaCursor = schemaConnection.cursor()

schemaCursor.execute("SHOW TABLES")
if MAIN_TABLE_NAME not in [results[0] for results in schemaCursor]:
    schemaCursor.execute(f"CREATE TABLE {MAIN_TABLE_NAME} (id VARCHAR(255), name VARCHAR(255))")

for card in cards:
    schemaCursor.execute(f"INSERT INTO {MAIN_TABLE_NAME} (id, name) VALUES (%s, %s)", (card.id, card.name))

schemaConnection.commit()

print("done")
