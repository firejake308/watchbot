# Author: Sam Shenoi
# Description: pulls information from the current webpage

import requests

def fetch_current_webpage():
    r = requests.get('https://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2025')
    return r.text



# for testing purposes
if __name__ == "__main__":
    print(fetch_current_webpage())