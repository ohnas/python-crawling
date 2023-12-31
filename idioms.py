import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(levelname)s : %(asctime)s : %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S %p",
)


def today_idiom(headers, today):
    try:
        url = "https://www.theidioms.com/"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        daily = soup.find("div", {"class": "daily"})
        name = daily.contents[0].find("a").text
        link = daily.contents[0].find("a")["href"]
        meaning = daily.contents[1].text
        example = daily.contents[2].text.replace("Read more ➺", "").rstrip()
        daily_tuple = (today, name, link, meaning, example)
        logging.info("today_idiom is done.")

        return daily_tuple

    except Exception as err:
        logging.error(f"An error occurred: {err} in today_idiom")


def idioms_last_page_numbers(headers):
    try:
        letters = [
            # "a",
            # "b",
            # "c",
            # "d",
            # "e",
            # "f",
            # "g",
            # "h",
            # "i",
            # "j",
            # "k",
            # "l",
            # "m",
            # "n",
            # "o",
            # "p",
            # "q",
            # "r",
            # "s",
            # "t",
            # "u",
            # "v",
            # "w",
            # "x",
            "y",
            # "z",
        ]
        letters_last_page_numbers = []
        for letter in letters:
            url = f"https://www.theidioms.com/{letter}/"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            pno = soup.find("p", {"class": "pno"}).text.replace("Page 1 of ", "")
            letters_last_page_numbers.append(
                {
                    "letter": letter,
                    "last_page_number": int(pno),
                }
            )
        logging.info("idioms_last_page_numbers is done.")

        return letters_last_page_numbers

    except Exception as err:
        logging.error(f"An error occurred: {err} in idioms_last_page_numbers")


def all_idioms(headers):
    try:
        items = idioms_last_page_numbers(headers)
        idioms_list = []
        for item in items:
            for num in range(item["last_page_number"]):
                url = f"https://www.theidioms.com/{item['letter']}/page/{num + 1}/"
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                phrase = soup.find("div", id="phrase")
                idioms = phrase.find_all("article", {"class": "idiom"})
                for idiom in idioms:
                    name = idiom.contents[0].find("a").text
                    link = idiom.contents[0].find("a")["href"]
                    meaning = idiom.contents[1].text
                    example = idiom.contents[2].text.replace("Read more ➺", "").rstrip()
                    idioms_list.append((name, link, meaning, example))
        logging.info("all_idioms is done.")

        return idioms_list

    except Exception as err:
        logging.error(f"An error occurred: {err} in all_idioms")
