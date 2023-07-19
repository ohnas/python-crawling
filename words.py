import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(levelname)s : %(asctime)s : %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S %p",
)


def today_word(headers, today):
    try:
        url = "https://www.britannica.com/dictionary/eb/word-of-the-day"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        word = soup.find("span", {"class": "hw_txt georgia_font"}).text
        img_src = soup.find("div", {"class": "wod_img_act"}).find("img")["src"]
        link = f"https://www.britannica.com/dictionary/{word}"
        daily_tuple = (today, word, img_src, link)
        logging.info("today_word is done.")

        return daily_tuple

    except Exception as err:
        logging.error(f"An error occurred: {err} in today_word")
