  # -*- coding:utf-8 -*-
import urllib.request
import re
import tool
import os
import http.cookiejar
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
# import pymysql.cursors
#抓取MM
class Tbmm:
        #页面初始化
        def __init__(self):
                self.tool=tool.Tool()
	
        def getDetailPage(self,infoURL):  
                cookie=http.cookiejar.CookieJar()  
                opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))   
                uop=opener.open(infoURL)  
                data=uop.read().decode('gbk')  
                return data

        def getImgsPath(self,images,name):
                number=1
                print(u"发现",name,u"有照片")
                for image in images:
                        splitPath=image.split('.')
                        fTail=splitPath.pop()
                        if len(fTail)>3:
                                fTail="jpg"
                        fileName=name+"/"+str(number)+"."+fTail
                        imageURL="https:"+image
                        if number<3:
                                self.saveImg(imageURL,fileName)
                        else:
                                break
                        number+=1
        #获取个人文字简介
        def getBrief(self,page):
                pattern=re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
                result=re.search(pattern,page)
                return self.tool.replace(result.group(1))

        def saveBrief(self,content,name):
                fileName=name+"/"+name+".txt"
                f=open(fileName,"w+")
                print(u"正在保存信息为",fileName)
                f.write(content.decode('utf-8'))
                f.close

        #获取页面所有图片
        def getAllImg(self,page):
                pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--',re.S)
                content=re.search(pattern,page)
                patternImg=re.compile('<img.*?src="(.*?)"',re.S)
                images=re.findall(patternImg,content.group(1))
                return images

        def saveImg(self,imageURL,fileName):
                try:
                        u=urllib.request.urlopen(imageURL)
                        imgdata=u.read()
                        f=open(fileName,'wb')
                        f.write(imgdata)
                        print(u"正在保存的图片为",fileName)
                        f.close
                except urllib.request.UrlError as e:
                        print(e.reason)
        def mkdir(self,path):
                path=path.strip()
                print(u"新建名为",path,u"的文件夹")
                os.makedirs(path)

        def savedb(self,item):
                connection=pymysql.connect(host='localhost',
                           user='root',
                           password='password',
                           db='tbmm',
                           charset='utf8mb4')
                try:
                        with connection.cursor() as cursor:
                                sql="insert into `mminfo`(`name`,`home`,`height`,`weight`,`moods`) values(%s,%s,%s,%s,%s)"
                                cursor.execute(sql,(item[0],item[1],item[2],item[3],item[4]))
                                connection.commit()
                finally:
                        connection.close()
                


        def savePageInfo(self,pagenum):
                i=0
                browser=webdriver.Firefox()
                browser.get('https://mm.taobao.com/search_tstar_model.htm')
                browser.find_elements_by_class_name('page-skip')[0].send_keys(pagenum)
                time.sleep(3)
                browser.find_elements_by_class_name('page-btn')[0].click()
                items=browser.find_elements_by_class_name('item')
                aa=browser.find_elements_by_class_name('item-link')
                mmurl=[]
                for a in aa:
                        mmurl.append(str(a.get_attribute('href')))
                pa=re.compile(r'\w+')
                mminfo=[]
                for item in items:
                        item=pa.findall(item.text)
                        mminfo.append(item)
                for item in mminfo:
                        detailURL=mmurl[i]
                        i+=1
                        if os.path.isdir(item[0]):
                                print(item[0],"已经被爬取了！","正在爬取下一个")
                                continue
                        try:
                                print(item[0],item[1],item[2],item[3],"人气",item[4])
                                print("正在保存",item[0],"的信息")
                                print("她的主页是",detailURL)
                        except:
                                print('此人信息不完整')
                        detailPage=self.getDetailPage(detailURL)
                        brief=self.getBrief(detailPage)
                        #images=self.getAllImg(detailPage)
                        self.mkdir(item[0])
                        self.saveBrief(brief.encode('utf-8'),item[0])
                        #print("正在保存她的照片")
                        #self.getImgsPath(images,item[0])
                a=input('确定把以上信息保存到数据库么？是或者否'+'\n')
                if a=='是':
                        for item in mminfo:
                                try:
                                        self.savedb(item)
                                        print(item[0]+'已经存入数据库')
                                except:
                                        print(item[0]+'之前已经存入数据库')
                else:
                        print('谢谢你的访问')
                        
                browser.close()

        def savePageInfos(self,x,y):
                for pagenum in range(x,y+1):
                        print('正在爬取第',pagenum,'页')
                        self.savePageInfo(pagenum)
        
tbmm=Tbmm()
tbmm.savePageInfos(1,2)
print("所有mm信息全部得到，工作结束！！！")
