from bs4 import BeautifulSoup
import requests

load_url = "https://www.ymori.com/books/python2nen/test1.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

aaa = soup.find("meta", charset = "UTF-8")
print(aaa.attrs['charset'])











