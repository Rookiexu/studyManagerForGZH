import xlwt
import xlrd
import time
from xlutils.copy import copy


def get_system_time():
    new_time = time.strftime('%Y%m%d%H%M', time.localtime())  # 格式化时间，按照 2017-04-15 13:46:32的格式打印出来
    print(new_time)
    return new_time

#open existed xls file
#newWb = xlutils.copy(gConst['xls']['fileName']);
#newWb = copy(gConst['xls']['fileName']);
oldWb=xlrd.open_workbook('../excl/16周周测数据分析.xls', formatting_info=True)
print(oldWb)#<xlrd.book.Book object at 0x000000000315C940>
newWb=copy(oldWb)
print(newWb)#<xlwt.Workbook.Workbook object at 0x000000000315F470>
newWs=newWb.get_sheet('一年级数学')
newWs.write(1,0,"value1")
newWs.write(1,1,"value2")
newWs.write(1,2,"value3")
print("write new values ok")
name = '../excl/demo_{a}.xls'.format(a=get_system_time())
print(name)
newWb.save(name)
print ("save with same name ok")
