# Using Regex

# a-z all alphabate
# 0-9 digits
#. _ at a time 1
# @ time 1
# . 2,3

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"    # Regex condition  
user_email = input('Enter your Email : ')

if re.search(email_condition, user_email):
    print('Right Email..')
else:
    print('Wrong Email')    