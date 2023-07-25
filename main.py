import requests
from bs4 import BeautifulSoup

KEYWORDS = ["дизайн", "веб", "фото", "python"]

url = "https://habr.com/ru/all/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_articles = soup.find_all("article")

for article in all_articles:
    try:
        if article.attrs["id"] is not None:
            date = article.find("time").attrs["title"]
            title = article.h2.get_text(strip=True)
            href = "".join(["https://habr.com", article.h2.a.attrs["href"]])
            preview = article.div.text.strip()

        for keyword in KEYWORDS:
            if keyword in preview.lower() or keyword in title.lower():
                print(f"{date} {title} {href}")

    except:
        pass
