# Data-mining-case-1-Energy-consumption
一句话介绍：将西门子2017-10-01至2018-9-30天的电能消耗量.xls用Python调整格式、合并、保存成CSV

语言：Python

软件：Spyder(Python 3.6)

调用的库：

os —— Python os模块包含普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。(引用https://blog.csdn.net/lygzscnt12/article/details/52470017?utm_source=blogxgwz0) 
os.getcwd()   #返回当前工作目录 
os.chdir(path)   #改变当前工作目录 
os.path.abspath(path)   #返回绝对路径
os.path.join(path1[, path2[, ...]])   #把目录和文件名合成一个路径

xlrd —— Python操作excel主要用到xlrd和xlwt这两个库，即xlrd是读excel，xlwt是写excel的库。(引用https://www.cnblogs.com/insane-Mr-Li/p/9092619.html）
data = xlrd.open_workbook(filename)   #打开Excel文件读取数据
table = data.sheet_by_index(sheet_indx))   #通过索引顺序获取
table = data.sheet_by_name(sheet_name)   #通过名称获取
table.cell_value(rowx,colx)   #返回单元格中的数据

glob —— glob模块用来查找文件目录和文件，常见的两个方法有glob.glob()和glob.iglob()，可以和常用的find功能进行类比，glob支持*?[]这三种通配符。
*代表0个或多个字符
?代表一个字符
[]匹配指定范围内的字符，如[0-9]匹配数字
