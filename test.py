import requests
from bs4 import BeautifulSoup

LIMIT = 3
req = requests.get('http://sw7up.cbnu.ac.kr/home')
html = req.text
bsObject = BeautifulSoup(html, "html.parser")

post_title = []
for title in bsObject.find_all('div', {"class":'title-container'}):
    post_title.append(title.text.strip())

post_link = []
for link in bsObject.select("ul > a:nth-child(1)"):
    post_link.append(link)
print(post_link)

