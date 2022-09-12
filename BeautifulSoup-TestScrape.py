import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

website = "https://plusportals.com/doradoacademy"
requestResult = requests.get(website)
soup = BeautifulSoup(requestResult.text, "html.parser")
print(soup.prettify)