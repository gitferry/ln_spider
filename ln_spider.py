import requests
import re
from bs4 import BeautifulSoup

def ln_spider():
    url = 'https://hashxp.org/lightning/node/?onlyliving=1'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for line in soup.find_all("td", text=re.compile("^\d{1,4}$")):
        print(line.text)

if __name__ == "__main__":
    ln_spider()