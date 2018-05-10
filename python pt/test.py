__author__ = 'JM'
# -*- coding:utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup
repon=requests.get("https://rate.tmall.com/list_detail_rate.htm?itemId=559441419648&spuId=883407445&sellerId=1114511827&order=3&currentPage=2&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvLpvEvbQvUpCkvvvvvjiPPLqhsjDRnLF90jljPmPUzjn8n2qplj3Wn2SWzjEbPgwCvvpvCvvv2QhvCvvvMM%2FivpvUvvmvWHE1XwKEvpvVmvvC9jXhKphv8vvvvvCvpvvvvvvCAyCv2V9vvUEpphvWh9vv9DCvpv11vvmmZhCv2jhEvpCWH219vvawAjc6kbVzb9AQD7zUdigDN%2B3ldU9srVERLNoxfBeKN6zI1b2XrqpyCW2%2BFO7t%2BeCBTWex6fItb9Txfw3l5dUf8c7%2BkE6BH9hCvvOvCvvvphvtvpvhvvvvv8wCvvpvvUmm&isg=Ai8v8q91qYdd4627fxwHfOAWvkP5fMYKO1MndkG8wB6lkE-SSaQTRi1CZLZV&needFold=0&_ksTS=1512132795853_838&callback=jsonp839")
repon=repon.text
repon=repon.strip(')')
repon=repon[12:]
repon=json.loads(repon)
repon=repon['rateDetail']['rateList']
for a in repon:
    print(a['rateContent'])


# repon.encoding="utf-8"
# bs=BeautifulSoup(repon.text,"lxml")
# a=bs.find_all("a",class_="mnav")
# for a in a:
#     print(a)
