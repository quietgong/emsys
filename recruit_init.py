from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()
from recruit.models import Post

LIMIT = 1

html = urlopen("https://software.cbnu.ac.kr/bbs/bbs.php?db=recruit")
bsObject = BeautifulSoup(html, "html.parser")

post_title = []
for title in bsObject.find_all('b'):
    post_title.append(title.text.strip()[:26])

post_link = []
for link in bsObject.find_all('td', {"class":'body_bold'}):
    post_link.append("https://software.cbnu.ac.kr/"+link.find("a")["href"])

post_specific_id = []
for i in range(0, LIMIT):
    post_link_parts = urlparse(post_link[i])
    query = post_link_parts.query
    post_specific_id.append(query[24:28])

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

post_order = []
for total in post_order:
    post_order.append()

result = []
for i in range(0, LIMIT):
    post_obj = {
        'title' : post_title[i],
        'link' : post_link[i],
        'date' : post_date[i],
        'specific_id' : post_specific_id[i],
        'content' : post_content[i]
    }
    result.append(post_obj)

# 크롤링한 데이터를 장고 DB에 저장
first_inserted_items = Post.objects.first()
if first_inserted_items is None:
    first_inserted_specific_id = ""
else:
    first_inserted_specific_id = getattr(first_inserted_items, 'specific_id')
items_to_insert_into_db = []
for item in result:
    if item['specific_id'] == first_inserted_specific_id:
        break
    items_to_insert_into_db.append(item)

for item in items_to_insert_into_db:
    print("new item added!! : " + item['title'])
    Post(specific_id=item['specific_id'],
         content=item['content'],
         title=item['title'],
         date=item['date'],
         link=item['link']).save()