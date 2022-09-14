from PlusportalsLogin import loginPayload
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

website = loginPayload("2024jcrivera@doradoacademy.org", "Hrengin1")
soup = BeautifulSoup(website.text, "html.parser")
print(website.url)
"""webTable = soup.find(id="GridRecentScore")
textExtract = soup.find(role="gridcell")
print(textExtract)"""