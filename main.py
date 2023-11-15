import requests
from bs4 import BeautifulSoup
from time import sleep


# Делаем липовый заголовок, ятобы сайты не поняли что запрос от бота
headers = {"User-Agent":
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

def get_url(): # Создали функцию - генератор страниц, чтобы не захламлять опер.память списками 
    for count in range(1, 8): # У нас всего 7 вэб-страниц и их нужно все обработать

        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        responce = requests.get(url, headers=headers)

        soup = BeautifulSoup(responce.text, "lxml") #Ещё один аналог lxml - htmll.parserб они нужны для структурирования HTML для лучшего поиска

        data = soup.find_all("div", class_="w-full rounded border")

        for i in data: #Делаем список из страниц с товаром для последующего разбора
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url

def array(): # Создаём ещё одну ф-ю генератор, через которую будем записывать данные в XL
    for card_url in get_url(): # Цикл для проведения разбора на текущей странице
        responce = requests.get(card_url, headers=headers)

        sleep(1) # Задержка в n секунды, чтобы сайт не положить запросами
        soup = BeautifulSoup(responce.text, "lxml") 
        data = soup.find("div", class_="my-8 w-full rounded border")

        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        description = data.find("p", class_="card-description").text
        url_img = "https://scrapingclub.com" + data.find("img").get("src")
        yield name, price, description, url_img
