# Author: Sam Shenoi
# Description: pulls information from the current webpage

import requests
from bs4 import BeautifulSoup

def fetch_current_webpage():
    r = requests.get('https://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2025')
    soup = BeautifulSoup(r.text, features='lxml')
    f = open('blank.html', 'w')
    f.write(r.text)
    res = soup.find_all('div', {"class": "leadsection"})
    print(res)
    return ""


# for testing purposes
if __name__ == "__main__":
    print(fetch_current_webpage())