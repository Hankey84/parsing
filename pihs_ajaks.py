from requests import Session
from bs4 import BeautifulSoup
import time, random 

base_url = "https://scrapingclub.com/exercise/list_infinite_scroll/"

headers = {"User-Agent":
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}



def main(base_url):

    s = Session()
    s.headers.update(headers)

    count = 1
    pagination = 0

    while True:

        if count > 1:
            url = base_url + "?page=" + str(count)
        else:
            url = base_url

        response = s.get(url)
        # with open("data.html", "w", encoding="utf-8") as r: # Запись в файл для удобного выдергивания заголовков и тэгов
        #     r.write(response.text)
        soup = BeautifulSoup(response.text, "lxml")

        if count == 1:
            # Необходимо найти номер последней подгужаемой скриптом страницы, т.е. пагинация:
            pagination = int(soup.find("nav", class_="pagination").find_all("span", class_="page")[-2].text)


        cards = soup.find_all("div", class_="w-full rounded border post")

        for card in cards:
            name = card.find("h4").text
            price = card.find("h5").text

            print(name, price)

        print(count)
        time.sleep(random.choice([5,7,9]))
        if count == pagination:
            break

        count += 1



main(base_url)