# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pyautogui
from bs4 import BeautifulSoup
import csv
import re
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
# (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
# dcap["phantomjs.page.settings.loadImages"] = False
# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
# driver = webdriver.PhantomJS(executable_path='D:/360安全浏览器下载/phantomjs-2.1.1-windows/bin/phantomjs.exe',\
#                               desired_capabilities=dcap)
driver=webdriver.Firefox(executable_path='C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
url='http://www.healthmap.org/zh/'
driver.get(url)
print (driver.title)
time.sleep(2)
driver.maximize_window()
driver.find_element_by_tag_name("body").click()
pyautogui.moveTo(1800,500,duration=2,tween=pyautogui.easeInOutQuad)
pyautogui.click()
time.sleep(10)
driver.find_element_by_id("show_search").click()
driver.find_element_by_id("diseases_drop").click()
driver.find_element_by_id("diseases_searchbox").click()
pyautogui.press("up")
pyautogui.press("enter")
driver.find_element_by_id("dates_drop").click()
driver.find_element_by_id("datechoice2").click()
driver.find_element_by_id("date1").send_keys("01/10/2017")
driver.find_element_by_id("date2").send_keys("07/10/2017")
driver.find_element_by_id("submit_search").click()
time.sleep(20)
pyautogui.moveTo(1170,110,duration=1,tween=pyautogui.easeInOutQuad)
pyautogui.click()
select=Select(driver.find_element_by_name("list_view_table_length"))
select.select_by_index(3)
time.sleep(1)
htmlcon=driver.page_source
soup=BeautifulSoup(htmlcon,"lxml",from_encoding="utf-8")
tr=soup.find("tbody").findAll("tr")
info=[]
zuobiao=re.compile(r'javascript:sc\(\'(.*?)\',\'(.*?)\'')
for t in tr:
    year=t.find("td", class_="sorting_1").get_text()
    location=t.findAll("td")[4].find("a")["href"]
    latitude=zuobiao.search(location).group(1)
    longitude=zuobiao.search(location).group(2)
    info.append(["齐卡病毒",year,latitude,longitude])
print(info)
# headers=["name","Year","Latitude","Longitude"]
# with open("zika.csv","w",newline="") as f:
#     f_csv=csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(info)
# driver.close()