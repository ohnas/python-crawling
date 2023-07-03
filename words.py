import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}
URL = "https://www.britannica.com/dictionary/eb/word-of-the-day"


def today_word(headers, url):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    word = soup.find("span", {"class": "hw_txt georgia_font"}).text
    img_src = soup.find("div", {"class": "wod_img_act"}).find("img")["src"]
    link = f"https://www.britannica.com/dictionary/{word}"
    daily_tuple = (word, img_src, link)

    return daily_tuple


try:
    print("crawling...")
    word = today_word(HEADERS, URL)
    print(word)
    print("finish!")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
