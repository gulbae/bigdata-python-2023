# 표준 라이브러리
# import datetime as dt

from datetime import date, datetime
first_date = date(2022, 12, 25)
cur_date = date.today()
print(cur_date - first_date)

cur_dt = datetime.now() #많이씀
print(cur_dt)
print(cur_dt.strftime('%Y-%m-%d')) #date.today() str

print(cur_dt.weekday()) # 0부터 월요일
print(cur_dt.isoweekday()) # 1부터 월요일

import time

for x in range(10):
    print(x)
    time.sleep(1) # second C#, java, C++ time.sleep(ms)

import math

print(math.pi)

import os

# print(os.environ)
# print(os.environ['PATH'])

print(os.getcwd)
print(os.system)

import json

with open('./Day04/data.json', 'r', encoding='UTF8') as f:
    data = json.load(f)

print(data)