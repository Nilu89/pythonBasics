
from datetime import datetime
from time import *
from os import *

def get_date():
    return datetime.today().strftime('%y-%m-%d')

ctime = datetime.today().strftime('%H:%M:%S')
sleep(2)
fntimestamp = datetime.today().strftime('%Y-%m-%d.%H:%M:%S')

print(f"current date is : {get_date()}")
print(f"current time is : {ctime}")
print(f"current time is : '{fntimestamp} - myapp.log'")

current_dir = path.dirname(path.abspath(__file__))
print(f"current dir : {current_dir}")