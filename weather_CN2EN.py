# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 21:57:36 2018

@author: xinyisong
"""

import pandas as pd

f = open(r'F:\秋招\西门子\Data mining case\电能消耗量\weather.csv', encoding='UTF-16')
df = pd.read_csv(f)
df = df.rename(columns={'weather':'weather type'})
df.drop(columns=['Unnamed: 0'],inplace = True)#print(df)

df['weather type'].replace({'晴':'clear','多云':'cloudy','阴':'overcoat','小雨':'light rain','中雨':'moderate rain','大雨':'heavy rain',
                            '阵雨':'shower','雷阵雨':'thunder shower','雨夹雪':'sleet','中雪':'moderate snow'},inplace =True)

df['wind direction'].replace({'北风':'N','东北风':'NE','东风':'E','东南风':'SE','南风':'S','西南风':'SW','西风':'W','西北风':'NW'},inplace =True)

df['wind scale'].replace({'微风':'breeze','1级':'1','2级':'2','小于3级':'<3','3～4级':'3~4','4级':'4'},inplace =True)

df.to_csv(r'F:\秋招\西门子\Data mining case\电能消耗量\weather_CN2EN.csv',index = False,encoding = 'utf-8')