import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}
URL = "https://www.theidioms.com/a/"

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    phrase = soup.find("div", id="phrase")
    idioms = phrase.find_all("article", {"class": "idiom"})
    idioms_list = []
    for idiom in idioms:
        name = idiom.contents[0].find("a").text
        link = idiom.contents[0].find("a")["href"]
        meaning = idiom.contents[1].text
        example = idiom.contents[2].text.replace("Read more ➺", "").rstrip()
        idioms_list.append(
            {
                "name": name,
                "link": link,
                "meaning": meaning,
                "example": example,
            }
        )
    print(idioms_list)

else:
    print(response.status_code)
