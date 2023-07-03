import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


def today_idiom(headers):
    url = "https://www.theidioms.com/"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    daily = soup.find("div", {"class": "daily"})
    name = daily.contents[0].find("a").text
    link = daily.contents[0].find("a")["href"]
    meaning = daily.contents[1].text
    example = daily.contents[2].text.replace("Read more ➺", "").rstrip()
    daily_tuple = (name, link, meaning, example)

    return daily_tuple


def all_idioms(headers):
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
    last_page_numbers = []
    for letter in letters:
        url = f"https://www.theidioms.com/{letter}/"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        pno = soup.find("p", {"class": "pno"}).text.replace("Page 1 of ", "")
        last_page_numbers.append(
            {
                "letter": letter,
                "last_page_number": int(pno),
            }
        )
    idioms_list = []
    for item in last_page_numbers:
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

    return idioms_list


try:
    print("crawling...")
    idiom = today_idiom(HEADERS)
    idioms = all_idioms(HEADERS)
    print("finish!")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
