import os
from selenium import webdriver
# driver=webdriver.Firefox(executable_path='C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
chromedriver = os.path.abspath("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.iqiyi.com/')
print(driver.title)
driver.close()
