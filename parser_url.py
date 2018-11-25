import requests
import json
import unicodedata
import re
from pprint import pprint

from bs4 import BeautifulSoup

s = requests.Session()
s.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    })

# r = s.get("https://leroymerlin.ru/catalogue/lampy-e27/")
# soup = BeautifulSoup(r.content, 'lxml')

with open("input/catalogue_lampy-e27_.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')

pattern = re.compile('var items = (.*)')
scripts = soup.find_all("script")

stock=''
for script in scripts:
    if script.string:
        if 'var items' in script.string:

            string = str(script.string).encode().decode('unicode_escape')


            datas = pattern.search(string)
            data = datas.groups()[0]
            with open('input/script.js', 'w') as fp:
                fp.write(data)
            print(data)
            stock = json.loads(data)

print(stock)
