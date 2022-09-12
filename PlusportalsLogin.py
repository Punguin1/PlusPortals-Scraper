import requests
from bs4 import BeautifulSoup

payload = {
    'username': '2024jcrivera@doradoacademy.org',
    'password': 'Hrengin1'
}
r = requests.post("https://plusportals.com/doradoacademy", data=payload)
soup = BeautifulSoup(r.content, "html.parser")
fp = open('PlusPortals-Scraper/HTMLplusportals.html', 'w')
fp.write(r.text)
fp.close

