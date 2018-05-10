# -*- coding:utf-8 -*-
import requests
import math
import json
import re
import csv
import codecs
import os
import pandas as pd
poi=[]
i=0
# countrys=os.listdir('data - wgs84/公交站')
countrys=['港口.csv','公交站.csv','火车站.csv','汽车站.csv']
for country in countrys:
    print(country)
    with open('汇总poi/'+country, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            i+=1
            print(i)
            print(row['名称'],row['x'],row['y'])
            poi.append([row['名称'],row['x'],row['y']])
print(len(poi))
headers=['名称','x','y']
with codecs.open('分类poi/交通度.csv','w',encoding='utf-8') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(poi)
