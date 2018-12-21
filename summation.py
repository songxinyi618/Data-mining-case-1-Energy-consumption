# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:44:30 2018

@author: Z003Z91Z
"""

import os
import xlrd
import glob
import pandas as pd

os.getcwd()
os.chdir(r'D:\Data mining case\电能消耗量\电量')

files=glob.glob('*.xls')

result = pd.DataFrame(columns=['serial number','datetime','T1','T2','T3','T4','sum'])

for filename in files:
    name = filename[0:6]
    domain = os.path.abspath(r'D:\Data mining case\电能消耗量\电量')
    filepath = os.path.join(domain,filename)
    
    excel = xlrd.open_workbook(filepath)
    sheet = excel.sheet_by_index(0)
          
    row_start=6 #开始的行
    row_end=30 #结束的行
    
    col_start=1 #开始的列
    col_end=8 #结束的列
    
    values_list = []
    for i in range(row_start,row_end):
        values = []
        for j in range(col_start, col_end):
            #查看表格的数据类型:0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error
            ctype = sheet.cell(i, j).ctype
            if ctype == 3:
                value = xlrd.xldate.xldate_as_datetime(sheet.cell_value(i, j),0)
            else:
                value = sheet.cell_value(i, j)
            values.append(value)
        values_list.append(values)
    
    df =  pd.DataFrame(values_list,columns=['serial number','datetime','T1','T2','T3','T4','sum'])       
    result = pd.concat([result,df],axis=0,ignore_index=True)

print(result)
result.to_csv(r'D:\Data mining case\电能消耗量\result.csv',index = True,encoding = 'utf-8')
