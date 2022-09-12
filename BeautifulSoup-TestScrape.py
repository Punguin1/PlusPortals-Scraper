from gettext import find
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

website = "https://plusportals.com/doradoacademy"

page = urlopen(website)
pageTextBytes = page.read()
poodoc = pageTextBytes.decode("utf-8")
soup = BeautifulSoup(poodoc, "html.parser")
tag = soup.find("h1")

print(remove_tags(str(tag)))