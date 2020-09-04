import requests
from bs4 import BeautifulSoup

LIMIT = 3
req = requests.get('http://sw7up.cbnu.ac.kr/home')
html = req.text
bsObject = BeautifulSoup(html, "html.parser")

post = []
for i in range(1,LIMIT+1):
    post.append(bsObject.select(f"#content > div.container.space-top-1.space-top-lg-2 > div > div.col-lg-7.mb-5.mb-lg-0 > lf-board > div.board-content > div > lf-notice-list > ul > a:nth-child({i})"))

post = str(post)

print(post)