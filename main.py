from datetime import datetime
import requests
from idioms import today_idiom, all_idioms
from words import today_word
from dbmanager import DBManager


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

TODAY = datetime.today().strftime("%Y-%m-%d")

try:
    print("crawling...")
    word = today_word(HEADERS, TODAY)
    idiom = today_idiom(HEADERS, TODAY)
    idioms = all_idioms(HEADERS)
    print("crawling finish!!")
    print("=================")
    print("DB working...")
    daily_word = DBManager("daily_word", word)
    daily_word.create()
    daily_idiom = DBManager("daily_idiom", idiom)
    daily_idiom.create()
    all_idiom = DBManager("all_idioms", idioms)
    all_idiom.create()
    print("DB finish!!")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
