from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

nameList = bs.findAll(text='the prince')
for name in nameList:
    print(name.get_text())
