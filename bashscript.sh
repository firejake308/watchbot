#!/bin/bash

# Author: Sam Shenoi
# Description: This file checks the differences between two webpages

curl https://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2025 > newversion.txt
curl https://www.bcm.edu/education/school-of-medicine/m-d-program/current-students/student-affairs/class-of-2025 > oldversion.txt
diff newversion.txt oldversion.txt