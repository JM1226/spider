from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random
import datetime
pages=set()
random.seed(datetime.datetime.now())
#得到内部链接
def getInternalLinks(bsobj,includeUrl):
    includeUrl=urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks=[]
    for link in bsobj.findAll('a',href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks
#得到外部链接
def getExternalLinks(bsobj,excludeUrl):
    externalLinks=[]
    for link in bsobj.findAll('a',href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
#得到随机外部链接
def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsobj=BeautifulSoup(html,'html.parser')
    try:
        print(bsobj.title)
    except:
        pass
    externalLinks=getExternalLinks(bsobj,urlparse(startingPage).netloc)
    if len(externalLinks)==0:
        print('No external links,looking around the site for one')
        domain=urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks=getInternalLinks(bsobj,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]
#得到随机内部链接
def getRandomInternalLinks(startingPage):
    html=urlopen(startingPage)
    bsobj=BeautifulSoup(html,'html.parser')
    try:
        print(bsobj.title)
    except:
        pass
    internalLinks=getInternalLinks(bsobj,startingPage)
    if len(internalLinks)==0:
        print('No internal links,looking around the site for one')
    else:
        return internalLinks[random.randint(0,len(internalLinks)-1)]
#查找所有外部链接
def followExternalOnly(startingSite):
    try:
        externalLink=getRandomExternalLink(startingSite)
        print("Random external link is "+externalLink)
        followExternalOnly(externalLink)
    except:
        print("已经找不到外链了，不好意思")
#查找所有内部链接
def followInternalOnly(startingSite):
    try:
        internalLink=getRandomInternalLinks(startingSite)
        print("Internal external link is "+internalLink)
        followInternalOnly(internalLink)
    except:
        print("已经找不到内链了，不好意思")
    
followInternalOnly('http://top.so.com/')
    
