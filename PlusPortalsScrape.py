from PlusportalsLogin import sendLogin
from bs4 import BeautifulSoup
import re

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)


url = "https://plusportals.com/doradoacademy"

website = sendLogin("2024jcrivera@doradoacademy.org", "Hrengin1", url)
soup = BeautifulSoup(website.text, "html.parser")
print(website)
"""webTable = soup.find(id="GridRecentScore")
textExtract = soup.find(role="gridcell")
print(textExtract)"""