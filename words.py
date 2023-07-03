import requests
from bs4 import BeautifulSoup


def today_word(headers):
    url = "https://www.britannica.com/dictionary/eb/word-of-the-day"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    word = soup.find("span", {"class": "hw_txt georgia_font"}).text
    img_src = soup.find("div", {"class": "wod_img_act"}).find("img")["src"]
    link = f"https://www.britannica.com/dictionary/{word}"
    daily_tuple = (word, img_src, link)

    return daily_tuple
