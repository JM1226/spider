import requests
import math
import json
import re
import csv
import codecs
def get_citycode():
    s = requests.session()
    response = s.get('https://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E5%85%AC%E4%BA%A4%E7%AB%99&c=31260&src=0&wd2=&pn=0&sug=0&l=6&b=(12308735.999999998,44587.99999999977;14635263.999999998,3194412)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&tn=B_NORMAL_MAP&nn=0&u_loc=12949555,4828305&ie=utf-8&t=1517301465117')
    response.encoding = 'utf-8'
    content = response.text
    content = json.loads(content)
    code=[]
    for a in content["content"]:
        code.append(a['code'])
    citys=content["more_city"]
    for city in citys[0]['city']:
        code.append(city['code'])
    return code
codes=get_citycode()
poi=[]
for code in codes:
    i=0
    num=0
    print(code)
    while(num<10):
        print(i)
        try:
            response = requests.get('http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=con&from=webmap&c=' + str(code) + '&wd=公交站&wd2=&pn=' + str(i) + '&nn=' + str(i) + '0')
            response.encoding = 'utf-8'
            content = response.text
            content = json.loads(content)
            for a in content['content']:
                geo=a['geo']
                geo = re.compile('\|(.*?)\;').search(geo).group(1)
                poi.append([a['name'], geo])
                print(a['name'],geo)
        except:
            print('在当前视图区域内未找到相关地点')
            num+=1
        finally:
            i+=1
print(len(poi))
headers=['名称','坐标']
with codecs.open('data/公交站/菲律宾公交站.csv','w',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(poi)