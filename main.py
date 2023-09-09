import json
import sys
from typing import List

import mysql.connector
import requests

from card import Card
from config import *


resp: requests.Response = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
all_card_data: List[dict] = json.loads(resp.text)["data"]
cards: List[Card] = [Card(card_data) for card_data in all_card_data]


def main() -> int:
    try:
        with mysql.connector.connect(
                host=HOSTNAME,
                user=USERNAME,
                password=PASSWORD,
        ) as serverConnection:
            serverCursor = serverConnection.cursor()
            serverCursor.execute("SHOW DATABASES")
            # cursor execution results are lists of tuples
            # in this case first item of each tuple is the name of a db
            if DBNAME.casefold() not in [results[0].casefold() for results in serverCursor]:
                # create the yu-gi-oh card db if it doesn't exist
                serverCursor.execute(f"CREATE DATABASE {DBNAME}")

            serverConnection.commit()

    except mysql.connector.Error as ex:
        print(f"Error connecting to MySQL server: {ex}")
        return 1

    try:
        with mysql.connector.connect(
                host=HOSTNAME,
                user=USERNAME,
                password=PASSWORD,
                database=DBNAME
        ) as schemaConnection:
            schemaCursor = schemaConnection.cursor()
            schemaCursor.execute("SHOW TABLES")
            if MAIN_TABLE_NAME.casefold() not in [results[0].casefold() for results in schemaCursor]:
                schemaCursor.execute(f"CREATE TABLE {MAIN_TABLE_NAME} (id VARCHAR(255), name VARCHAR(255))")

            for card in cards:
                schemaCursor.execute(f"INSERT INTO {MAIN_TABLE_NAME} (id, name) VALUES (%s, %s)",
                                     (card.id, card.name))

            schemaConnection.commit()

    except mysql.connector.Error as ex:
        print(f"Error connecting to database: {ex}")
        return 1

    print("done")


if __name__ == "__main__":
    sys.exit(main())
