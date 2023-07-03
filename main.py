import requests
from idioms import today_idiom, all_idioms
from words import today_word


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


try:
    print("crawling...")
    word = today_word(HEADERS)
    idiom = today_idiom(HEADERS)
    idioms = all_idioms(HEADERS)
    print("Today word :", word)
    print("Today idiom :", idiom)
    print("All idioms :", idioms)
    print("finish!")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
