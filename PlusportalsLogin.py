import pip._vendor.requests as requests
from bs4 import BeautifulSoup
def loginPayload(username, password):
    payload = {
        "User-agent": "*",
        "username": username,
        "password": password
    }
    r = requests.post("https://plusportals.com/doradoacademy", data=payload)
    fp = open('PlusPortals-Scraper/HTMLplusportals.html', 'w')
    fp.write(r.text)
    fp.close
    return r

