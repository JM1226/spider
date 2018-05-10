import requests
import math
import json
import re
import csv
import codecs
def get_citycode():
    response = requests.get('http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=s&da_src=searchBox.button&wd=%E9%85%92%E5%90%A7&c=131&src=0&wd2=&pn=0&sug=0&l=6&b=(8836879.999996675,791587.9999967255;13133583.999996675,3941411.9999967255)&from=webmap&biz_forward={%22scaler%22:1,%22styles%22:%22pl%22}&sug_forward=&tn=B_NORMAL_MAP&nn=0&u_loc=12949555,4828305&ie=utf-8&t=1516099451410')
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
    response = requests.get('http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=direct&pcevaname=pc4.1&qt=spot&from=webmap&c='+str(code)+'&wd=%E9%85%92%E5%90%A7&wd2=&pn=0&nn=0&db=0&sug=0&addr=0&pl_data_type=cater&pl_sub_type=&pl_price_section=0%2C%2B&pl_sort_type=data_type&pl_sort_rule=0&pl_discount2_section=0%2C%2B&pl_groupon_section=0%2C%2B&pl_cater_book_pc_section=0%2C%2B&pl_hotel_book_pc_section=0%2C%2B&pl_ticket_book_flag_section=0%2C%2B&pl_movie_book_section=0%2C%2B&pl_business_type=cater&pl_business_id=&da_src=pcmappg.poi.page&on_gel=1&src=7&gr=3&l=6.786988674318071&rn=50&tn=B_NORMAL_MAP&u_loc=12949555,4828305&ie=utf-8&b=(9637211.138751868,881440.2927503737;11747561.250650223,2706928.7472496266)&t=1516099583967')
    response.encoding = 'utf-8'
    content = response.text
    content = json.loads(content)
    try:
        for a in content['content']:
            geo=a['geo']
            geo = re.compile('\|(.*?)\;').search(geo).group(1)
            poi.append([a['name'],geo])
            print(a['name'],geo)
    except:
        print('在当前视图区域内未找到相关地点')
# print(len(poi))
# headers=['名称','坐标']
# with codecs.open('data/酒吧/越南酒吧.csv','w',encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(headers)
#     writer.writerows(poi)