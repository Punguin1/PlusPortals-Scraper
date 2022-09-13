import requests
from bs4 import BeautifulSoup
def loginPayload(username, password):
    payload = {
        "username": username,
        "pass word": password
    }
    r = requests.post("https://plusportals.com/doradoacademy", data=payload)
    fp = open('PlusPortals-Scraper/HTMLplusportals.html', 'w')
    fp.write(r.text)
    fp.close
    return r

