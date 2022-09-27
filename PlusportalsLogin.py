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
    resp = session.get(r.url)
    resp.html.render()
    print(resp)
    return 

