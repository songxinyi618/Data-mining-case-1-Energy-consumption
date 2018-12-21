# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 12:29:51 2018

@author: z003z91z
"""

from urllib import request
from bs4 import BeautifulSoup
import pandas as pd 
import csv

head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

result = pd.DataFrame(columns=['date','highest temperature','lowest temperature','weather','wind direction','wind scale'])
month_list = ['201710','201711','201712','201801','201802','201803','201804','201805','201806','201807','201808','201809']

for month in month_list:
    weather_url = 'https://lishi.tianqi.com/shanghai/'+ month +'.html'
    weather_req = request.Request(url = weather_url, headers = head)
    weather_response = request.urlopen(weather_req)
    weather_html = weather_response.read().decode('gbk',errors='ignore')
    weather_soup = BeautifulSoup(weather_html , 'lxml')
    #print(weather_soup)
        
    weather_info = weather_soup.find(name = 'div', attrs = {'class':'tqtongji2'}).get_text()
    #print(weather_info)
    #weather_info.replace(' ','')#不是空格，是换行符
    weather_info = weather_info.splitlines(False)#在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。

    while '' in weather_info:
        weather_info.remove('')

    text_list = [weather_info[i:i + 6] for i in range(0, len(weather_info), 6)]
    #print(text_list)

    df =  pd.DataFrame(text_list,columns=['date','highest temperature','lowest temperature','weather','wind direction','wind scale'])
    df.drop(index=0, inplace=True)#inplace=True，直接在原数据上进行删除操作，删除后就回不来了
    #print(df)
    result = result.append(df)

print(result)
result.to_csv(r'D:\Data mining case\电能消耗量\weather.csv',index = True,encoding = 'utf-16')
#2018年9月少了7，8，9，15四天

################################delete weekend#################################
for i in range(6,364,7):#从i=7到i=364,每隔7个数
    index_col=0 #要指明第一列为行索引，否则python会自动加一列索引
    data.drop(labels = [i, i+1], axis=0,inplace = True)
