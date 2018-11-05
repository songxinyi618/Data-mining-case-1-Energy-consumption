# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:27:59 2018

@author: z003z91z
"""

import os
import xlrd
import glob
import pandas as pd

os.getcwd()
os.chdir(r'D:\Data mining case\电能消耗量\电量')

files=glob.glob('*.xls')

values_list = []
name_list = []

for filename in files:
    name = filename[0:6]
    domain = os.path.abspath(r'D:\Data mining case\电能消耗量\电量')
    filepath = os.path.join(domain,filename)
    name_new = '20'+name[0:2]+'-'+name[2:4]+'-'+name[4:6]
    name_list.append(name_new)
    
    excel = xlrd.open_workbook(filepath)
    sheet = excel.sheet_by_index(0)#第0个sheet
    
    values = []
    for j in range(3,8):
        value = sheet.cell_value(31, j)
        values.append(value)
    values_list.append(values)
    
summation =  pd.DataFrame(values_list, index=name_list, columns=['T1','T2','T3','T4','sum'])   
print(summation) 
summation = summation.replace(0, 'null')   
summation.to_csv(r'D:\Data mining case\电能消耗量\summation.csv',index = True,encoding = 'utf-8')

    
  
    