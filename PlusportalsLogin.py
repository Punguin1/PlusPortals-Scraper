import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
def sendLogin(username, password, url):
    payload = {
        "User-agent": "*",
        "username": username,
        "password": password
    }



    PATH = "C:\Program Files (x86)\PYTHON DEPENDENCIES\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    wdriver = webdriver.Chrome(executable_path=PATH, options=chrome_options)
    wdriver.get(url)
    soup = BeautifulSoup(wdriver.page_source.encode("utf-8"), "html.parser")
    sleep(3)
    fp = open('PlusPortals-Scraper/HTMLplusportals.html', 'w')
    fp.write(str(soup.prettify))
    fp.close
    return soup

