from datetime import datetime
import requests
import sqlite3
from idioms import today_idiom, all_idioms
from words import today_word


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

TODAY = datetime.today().strftime("%Y-%m-%d")

try:
    print("crawling...")
    # word = today_word(HEADERS)
    idiom = today_idiom(HEADERS)
    print(idiom)
    # con = sqlite3.connect("crawling.db")
    # cur = con.cursor()
    # cur.execute(
    #     """
    #     CREATE TABLE IF NOT EXISTS daily_idiom
    #         (id INTEGER PRIMARY KEY, date text, name text, link text, meaning text, example text)
    # """
    # )
    # cur.execute(
    #     """
    #     CREATE TABLE IF NOT EXISTS all_idioms
    #         (id INTEGER PRIMARY KEY, name text, link text, meaning text, example text)
    # """
    # )
    # cur.execute(
    #     """
    #     CREATE TABLE IF NOT EXISTS daily_word
    #         (id INTEGER PRIMARY KEY, date text, word text, img_src text, link text)
    # """
    # )
    # cur.execute('INSERT INTO daily_idiom VALUES (?,?,?,?,?)', idiom)

    # con.commit()
    # con.close()
    # idioms = all_idioms(HEADERS)
    # print("Today word :", word)
    # print("Today idiom :", idiom)
    # print("All idioms :", idioms)
    print("finish!")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
