# this script posts the names
# run this after app.py

import requests
import json

# navs 35mr03x61
# test k76j34jnl

url = "https://truelove.gamesoa.com/35mr03x61"
urls = "https://truelove.gamesoa.com/send"

page = requests.get(url)

names = json.loads(open('names.json').read())

# payload is html form data in url
for girl in names:
    payload = {'vname': 'naveen', 'cname': girl, 'sid': 't3drjdouo87u4kg'}
    requests.post(url = urls, data = payload)
