from bs4 import BeautifulSoup as bs
import requests
import json
import random

url = "http://www.studentsoftheworld.info/penpals/stats.php?Pays=IND"
url2 = "https://www.in.pampers.com/pregnancy/baby-names/article/the-most-popular-baby-girl-names-in-india"

page = requests.get(url)
page2 = requests.get(url2)

soup = bs(page.content, features = "html.parser")
soup2 = bs(page2.content, features = "html.parser")

names = []
names2 = []

all_tags = soup.find_all("font", {"class": "text2"})
all_tags2 = soup2.find_all("td")

for tags in all_tags:
        names.append(tags.text)

names = names[17:-100]

names = names[::2]

for tags2 in all_tags2:
    names2.append(tags2.text)

names2 = names2[::2]

names = names + names2
random.shuffle(names)

# print(names)

namesj = json.dumps(names)

# print(namesj)

filee = open(file = "names.json", mode = "w")
filee.write(namesj)

# for name in names:
#     file = open(file = "names.txt", mode = "a")
#     file.writelines(name)
#     file.writelines(" ")

