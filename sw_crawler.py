from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()
from notice_sw.models import Post

LIMIT = 25

html = urlopen("https://software.cbnu.ac.kr/bbs/bbs.php?db=notice")
bsObject = BeautifulSoup(html, "html.parser")

result = []

post_title = []
for title in bsObject.find_all('b'):
 post_title.append(title.text.strip())

post_link = []
for link in bsObject.find_all('td', {"class":'body_bold'}):
  post_link.append("https://software.cbnu.ac.kr/"+link.find("a")["href"])

for i in range(0, LIMIT):
  post_obj = {
      'post_title' : post_title[i],
      'post_link' : post_link[i]
  }
  result.append(post_obj)
print(result)

for item in result:
  Post(title = item['post_title'], link = item['post_link']).save()