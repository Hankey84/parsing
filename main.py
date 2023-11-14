import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

responce = requests.get(url)

soup = BeautifulSoup(responce.text, "lxml") #Ещё один аналог lxml - htmll.parserб они нужны для структурирования HTML для лучшего поиска

data = soup.find("div", class_="w-full rounded border")


name = data.find("h4").text.replace("\n", "")
price = data.find("h5").text
url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")

#print(data)
print(name + "\n" + price +"\n" + url_img+ "\n\n")