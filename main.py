from pymongo import MongoClient
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.fmkorea.com/hotdeal")
bsObject = BeautifulSoup(html, "html.parser")

client = MongoClient(host='localhost', port=27017)
collection = client['hotdeal']['hotdeal']

for li in bsObject.body.find_all('li', {"class" : "li li_best2_pop0 li_best2_hotdeal0"}):
    title = li.h3.a.get_text().strip()
    title = title[:title.rfind('[')].strip()
    data = li.find('div', attrs={'class': 'hotdeal_info'}).get_text().strip().split('/')


    rawData = {
        "title" : title,
        "platform" : data[0].split(' ')[1].strip(),
        "price" : data[1].split(' ')[1].strip(),
        "delivery" : data[2].split(' ')[1].strip(),
    }

    #print(rawData)
    collection.insert_one(rawData)


