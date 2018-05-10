import requests
import math
import json
import re
import csv
import codecs

def getzb(content):
    zuobiao=[]
    for a in content["content"]:
        geo=a["geo"]
        geo=re.compile('\|(.*?)\;').search(geo).group(1)
        zuobiao.append([a['name'],geo])
    citys=content["more_city"]
    for city in citys[0]['city']:
        geo = city["geo"]
        geo = re.compile('\|(.*?)\;').search(geo).group(1)
        zuobiao.append([city['name'],geo])
    return zuobiao

def getlonlat(zuobiao):
    zonghe=[]
    for a in zuobiao:
        jwd=a[1].split(',')
        mercator = {"x":float(jwd[0]), "y":float(jwd[1])}
        lonlat = {}
        x = mercator['x']/ 20037508.34 * 180
        y = mercator['y']/ 20037508.34 * 180
        lonlat['name']=a[0]
        lonlat['x'] = x
        lonlat['y'] = 180 / math.pi * (2 * math.atan(math.exp(y * math.pi / 180)) - math.pi / 2)
        zonghe.append(lonlat)
    return zonghe

def baocun(zonghe):
    info=[]
    i=0
    for a in zonghe:
        print(i)
        i+=1
        info.append([a['name'],a['x'],a['y']])
    headers=['name','x','y']
    with codecs.open('data/老挝火车站.csv','w',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(info)

def main():
    response = requests.get('http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E7%81%AB%E8%BD%A6%E7%AB%99&c=80485&src=0&wd2=&pn=0&sug=0&l=15&b=(11433555.199999996,2011264.3500000103;11436835.199999996,2017416.3500000103)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&tn=B_NORMAL_MAP&nn=0&u_loc=12949555,4828305&ie=utf-8&t=1515846466428')
    response.encoding = 'utf-8'
    content = response.text
    content = json.loads(content)
    zuobiao=getzb(content)
    zonghe=getlonlat(zuobiao)
    baocun(zonghe)
    print("Done")

main()