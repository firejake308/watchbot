# Author: Sam Shenoi
# Description: pulls information from the current webpage

import requests
from bs4 import BeautifulSoup

def fetch_current_webpage(webpage):
    r = requests.get(webpage)
    soup = BeautifulSoup(r.text)
    #res = soup.find(class= "leadSection")
    #print(res)
    return ""




# for testing purposes
if __name__ == "__main__":
    print(fetch_current_webpage())