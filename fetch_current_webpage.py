# Author: Sam Shenoi
# Description: pulls information from the current webpage

import requests
from bs4 import BeautifulSoup

def fetch_current_webpage(webpage):
    soup = BeautifulSoup(r.text, features='lxml')
    res = soup.find('div', {"class": "leadsection"})
    return res


# for testing purposes
if __name__ == "__main__":
    print(fetch_current_webpage())