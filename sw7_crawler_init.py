from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
import django
django.setup()

from notice_sw7up.models import Post

req = requests.get('http://sw7up.cbnu.ac.kr/home')
html = req.text
bsObject = BeautifulSoup(html, "html.parser")

post_title = []
for title in bsObject.find_all('div', {"class":'title-container'}):
    post_title.append(title.text.strip())

post_date = []
for date in bsObject.find_all('div', {"class": 'date'}):
    post_date.append(date.text.strip())

post_link_data = []
for link in bsObject.find_all('a', {"class":'list-group-item'}):
    post_link_data.append(link)
post_link = []
for i in range(-4, 0):
    link_object = BeautifulSoup(str(post_link_data[i]), "html.parser")
    link = link_object.find("a")["href"]
    post_link.append("http://sw7up.cbnu.ac.kr"+link)

post_specific_id = []
for i in range(0, 4):
    post_link_parts = urlparse(post_link[i])
    path = post_link_parts.path
    post_specific_id.append(path[18:43])

post_content = []
for i in range(0, 4):
    content_req = requests.get(post_link[i])
    html = content_req.text

    bsObject_content = BeautifulSoup(html, "html.parser")
    for content in bsObject_content.find_all('div', {"class":"mt-4 ck ck-blurred ck-content ck-editor__editable ck-editor__editable_inline ck-rounded-corners"}):
        post_content.append(content.text.strip())

result = []
for i in range(0, 1):
    post_obj = {
        'title' : post_title[i],
        'link' : post_link[i],
        'date' : post_date[i],
        'specific_id' : post_specific_id[i],
        'content' : post_content[i]
    }
    result.append(post_obj)
print(result)
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