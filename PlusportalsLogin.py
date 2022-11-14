import requests 
from requests_html import HTMLSession
from bs4 import BeautifulSoup
def sendLogin(username, password, url):
    payload = {
        "User-agent": "*",
        "username": username,
        "password": password
    }
    session = HTMLSession()
    r = requests.post(url, data=payload)
    print(r.url)
    resp = session.get(r.url)
    print(resp.url)
    resp.html.render(cookies=payload)
    f = open("HTMLplusportals.html", "w")
    f.write(resp.html.html)
    f.close

    return r

