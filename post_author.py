from requests import Session
from bs4 import BeautifulSoup
from time import sleep

# Код для пост-авторизации
# Делаем липовый заголовок, ятобы сайты не поняли что запрос от бота
headers = {"User-Agent":
           "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}

work = Session()

work.get("https://quotes.toscrape.com/", headers=headers) # Заходим на сайт под левым заголовком, чтобы сымитировать  пользователя

responce = work.get("https://quotes.toscrape.com/login", headers=headers) # Заходим в раздел идентификации

soup = BeautifulSoup(responce.text, "lxml")
token = soup.find("form").find("input").get("value") # Парсим на странице одноразовый токен для последующей авторизации

data = {"csrf_token":token, "username": "noname", "password": "password"} # Заводим словарь для последующей генерации логина и пароля, токен уже есть

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True) # Авторизация и переброска на другую страницу

#print(result.text)
result = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

    if len(result) != 0:
        # Do something
    else:
        break