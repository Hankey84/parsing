import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []

# Делаем липовый заголовок, ятобы сайты не поняли что запрос от бота
headers = {"User-Agent":
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

for count in range(1, 8): # У нас всего 7 вэб-страниц и их нужно все обработать

    sleep(3) # Задержка в 3 секунды, чтобы сайт не положить запросами
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    responce = requests.get(url, headers=headers)

    soup = BeautifulSoup(responce.text, "lxml") #Ещё один аналог lxml - htmll.parserб они нужны для структурирования HTML для лучшего поиска

    data = soup.find_all("div", class_="w-full rounded border")

    for i in data: #Делаем список из страниц с товаром для последующего разбора
        card_url = "https://scrapingclub.com" + i.find("a").get("href")
        list_card_url.append(card_url)

for card_url in list_card_url: # Цикл для проведения разбора на текущей странице
    responce = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(responce.text, "lxml") 
    data = soup.find("div", class_="my-8 w-full rounded border")

    name = data.find("h3", class_="card-title").text
    price = data.find("h4").text
    description = data.find("p", class_="card-description").text
    url_img = "https://scrapingclub.com" + data.find("img").get("src")


    print(name + "\n" + price +"\n" + url_img + "\n" + description + "\n\n")
