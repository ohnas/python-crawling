from datetime import datetime
import logging
import requests
from idioms import today_idiom, all_idioms
from words import today_word
from dbmanager import DBManager, is_empty


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}

TODAY = datetime.today().strftime("%Y-%m-%d")

logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(levelname)s : %(asctime)s : %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S %p",
)

try:
    logging.info("Crawling is working...")
    word = today_word(HEADERS, TODAY)
    idiom = today_idiom(HEADERS, TODAY)
    daily_word = DBManager("daily_word", word)
    daily_word.create()
    daily_idiom = DBManager("daily_idiom", idiom)
    daily_idiom.create()

    count = is_empty()
    if count == None:
        idioms = all_idioms(HEADERS)
        all_idiom = DBManager("all_idioms", idioms)
        all_idiom.create()
    logging.info("Crawling is success!!")
except requests.exceptions.HTTPError as err:
    logging.error(f"HTTP error occurred: {err} in main.py")
except Exception as err:
    logging.error(f"An error occurred: {err} in main.py")
