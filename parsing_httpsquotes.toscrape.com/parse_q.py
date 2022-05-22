from ast import parse
from multiprocessing import AuthenticationError
from requests import Session
from bs4 import BeautifulSoup
from time import sleep
headers = {"User-Agent": "Ho-Ho-Ho"}

work = Session()
work.get("https://quotes.toscrape.com/", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")

data = {"csrf_token": token, "username": "noname", "password": "p@ssw0rd"}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

for page in 1000:
    result = soup.find_all("span", class_="text")
    author = soup.find_all("smal", class_="author")

    if len(result) != 0:
        pass
    else:
        break

