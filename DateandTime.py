import datetime
import os

print('Hello')
date = input('do you want to know the date?  ')
if date == 'yes':
    def get_date():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('The current date and time is:', get_date())
if date == 'no':
    print('ok, bye')
