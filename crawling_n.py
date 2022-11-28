# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 00:34:53 2022

@author: JIH
"""
## 코드 설명 : 네이버 이미지 웹 크롤링

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
import urllib.request
import pandas as pd
import time
import os
import sys

## soup to xpath
def xpath_soup(element):
    components = []
    child = element if element.name else element.parent
    for parent in child.parents:
        siblings = parent.find_all(child.name, recursive=False) # 직계자손 탐색
        components.append(
            child.name if 1 == len(siblings) else '%s[%d]' % (
                child.name,
                next(i for i, s in enumerate(siblings, 1) if s is child)
                )
            )
        child = parent
    components.reverse()
    return '/%s' % '/'.join(components)

## 검색 및 저장 정보 설정
url = 'https://www.naver.com/'
keyword = '진로 360ml 소주'
crolcnt = 500
labelimg = 'w0'
print('%s 로 검색\n'%keyword)
time.sleep(0.5)

import os
img_folder = 'C:/Users/----------------------------' # 저장경로 지정

if os.path.isdir(img_folder)==True:
    print('지정한 경로에 폴더가 존재합니다. : %s'%img_folder)
    if input("지정한 경로로 다운로드가 실행됩니다. \n동의하면 [y]입력 : ") == 'y':
        pass 
    else:
        sys.exit("크롤링 종료")
else:
    print('지정한 폴더가 존재하지 않습니다. 확인 후 실행')
    sys.exit("크롤링 종료")

## url chrome으로 열기
driverpath = "chromedriver.exe"
driver = webdriver.Chrome(driverpath)
driver.get(url)
time.sleep(3)

xpath_button = '//*[@id="query"]'

driver.find_element_by_xpath(xpath_button).send_keys(keyword,Keys.ENTER)

## 카테고리 순서가 변동되는 것 잡기
soup = BeautifulSoup(driver.page_source, 'html.parser') # 페이지 로딩
button = soup.find("a",{"role":"tab", "onclick":re.compile('tab\*i')})
path = xpath_soup(button)
driver.find_element_by_xpath(path).send_keys(Keys.ENTER)

## 페이지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight") 

while True:  
    # 최하단으로 스크롤 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    time.sleep(2) # 페이지 로딩 대기 (2초 미만 로딩 에러)
    new_height = driver.execute_script("return document.body.scrollHeight") 
    # 더이상 스크롤 되지 않을 2가지 경우 확인
    if new_height == last_height: 
        break
    last_height = new_height 

## 찾은 이미지 src 저장
full_html = driver.page_source
soup = BeautifulSoup(full_html, 'html.parser')
time.sleep(3)

src_lst=[]
images = soup.find_all("img", class_="_image _listImage")
for image in images:
    src_lst.append(image.get("data-lazy-src",image.get("src")))

time.sleep(2)
print('다운로드 가능한 이미지 갯수 : ',len(src_lst))

## 다운로드 경로 자동 지정
print('다운로드를 위해 파이썬 경로를 지정한 경로로 변경합니다. \n경로 : %s'%img_folder)
os.chdir(img_folder) # 지정된 경로로 다운로드 경로 설정

## 이미지 저장
print('이미지 다운로드 시작\n')
for k,i in enumerate(src_lst[:crolcnt]):
    url = i
    start = time.time()
    try:
        urllib.request.urlretrieve(url, "./"+str(labelimg)+"_"+str(k)+".jpg") # src / 저장할 파일명 지정
        print(str(k+1)+'/'+str(len(src_lst[:crolcnt]))+' 다운로드 중....... Download time : '+str(time.time() - start)[:5]+' 초')
    except: 
        print(str(k+1)+'/'+str(len(src_lst[:crolcnt]))+' 다운로드 실패')
print('\n---다운로드 완료---')

driver.close()

os.chdir('C:/Users/------') # 경로 원상 복귀


'''
[reference]
1. soup to xpath 함수 : https://gist.github.com/ergoithz/6cf043e3fdedd1b94fcf
2. 그 외 code : written by JIH
'''







