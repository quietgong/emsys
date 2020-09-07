from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()
from notice_sw.models import Post

LIMIT = 25

html = urlopen("https://software.cbnu.ac.kr/bbs/bbs.php?db=notice")
bsObject = BeautifulSoup(html, "html.parser")

post_title = []
for title in bsObject.find_all('b'):
    post_title.append(title.text.strip()[:28])

post_link = []
for link in bsObject.find_all('td', {"class":'body_bold'}):
    post_link.append("https://software.cbnu.ac.kr/"+link.find("a")["href"])

post_specific_id = []
for i in range(0, LIMIT):
    post_link_parts = urlparse(post_link[i])
    query = post_link_parts.query
    post_specific_id.append(query[23:27])

post_content = []
for i in range(0, LIMIT):
    content_link = urlopen(post_link[i])
    bsObject_content = BeautifulSoup(content_link, "html.parser")
    for content in bsObject_content.find_all('div', {"id":"articles"}):
        post_content.append(content.text.strip())

post_date = []
for date in bsObject.find_all('td', {"class":'body_num'}):
    post_date.append(date.text.strip())
post_date = post_date[2::4]

result = []
for i in range(0, LIMIT):
    post_obj = {
        'title' : post_title[i],
        'link' : post_link[i],
        'specific_id' : post_specific_id[i],
        'content' : post_content[i],
        'date' : post_date[i]
    }
    result.append(post_obj)

# 크롤링한 데이터를 장고 DB에 저장
db_specific_id = []
items_to_insert_into_db = []
n = Post.objects.count()

for i in range(1, n+1):
    row = Post.objects.get(pk=i)
    db_specific_id.append(row.specific_id)

for item in result:
    if item['specific_id'] not in db_specific_id:
        items_to_insert_into_db.append(item)

for item in items_to_insert_into_db:
    print("new item added!! : " + item['title'])
    Post(specific_id=item['specific_id'],
         content=item['content'],
         title=item['title'],
         date=item['date'],
         link=item['link']).save()