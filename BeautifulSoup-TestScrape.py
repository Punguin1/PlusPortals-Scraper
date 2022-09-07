from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq



with open("PlusPortals-Scraper/testhtml.html") as website:
    soup = bs(website, "html.parser")
tag = soup.b    
print(str(tag.name))