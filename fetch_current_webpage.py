# Author: Sam Shenoi
# Description: pulls information from the current webpage

import requests
from bs4 import BeautifulSoup

# hack to allow Heroku's less secure SSL
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
    # no pyopenssl support used / needed / available
    pass

def fetch_current_webpage(webpage):
    r = requests.get(webpage)
    soup = BeautifulSoup(r.text, features='lxml')
    content = soup.find('div', {"class": "leadsection"})
    lis = content.find_all('li')
    items = []
    for li in lis:
        content  = li.text
        links = li.find('a')
        href = ': ' + links['href'] if links else ''
        items.append(content + href)
    return items


# for testing purposes
if __name__ == "__main__":
    print(fetch_current_webpage('http://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2026'))