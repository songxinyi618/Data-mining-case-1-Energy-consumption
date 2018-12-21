# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:40:07 2018

@author: z003z91z
"""

import pandas as pd
from numpy import NaN

f = open(r'F:\秋招\西门子\Data mining case\电能消耗量\summation.csv')
df = pd.read_csv(f)
df = df.rename(columns={'Unnamed: 0':'date'})#print(df)

data_info = df.describe()#print(data_info)
data_isnull = df.isnull().sum()#print(data_isnull)

df = df.replace(NaN, 0)
data = df.loc[:,['date','T1','T2','T3','T4','sum'] ]

for i in range(6,364,7):#从i=7到i=364,每隔7个数
    index_col=0 #要指明第一列为行索引，否则python会自动加一列索引
    data.drop(labels = [i, i+1], axis=0,inplace = True)
#print(data)

holidays = ['2017-10-01', '2017-10-02','2017-10-03','2017-10-04','2017-10-05','2017-10-06', '2017-12-24', '2017-12-25',
            '2018-01-01', '2018-02-15','2018-02-16','2018-02-19','2018-02-20','2018-02-21',
            '2018-04-05', '2018-04-06','2018-04-30','2018-05-01','2018-06-18','2018-09-24',]
data=data[~data['date'].isin(holidays)]

data.to_csv(r'F:\秋招\西门子\Data mining case\电能消耗量\summation_no-weekend-no-holiday.csv',index = False,encoding = 'utf-8')
