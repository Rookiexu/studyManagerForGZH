import xlrd
import os
from cn.rookiex.domain.BanJi import *
from cn.rookiex.wt import writeUtil


def getBanJiChengJi(path,type1):
    FileNames = os.listdir(path)
    banjis = []
    for filename in  FileNames:
        keyWords = filename.split('_')
        className = keyWords[0]
        testName = keyWords[1]
        testNo = keyWords[2].split('.')[0]
        banji  = getFenDuan(path,filename,1,str(className),str(testName),int(testNo))
        banjis.append(banji)
        # for keyWord in keyWords:
    return banjis

def getFenDuan(path: str, fileName: str, type1: int, className: str, testName: str, testNo: int):
    FileNames = os.listdir(path)
    print(FileNames[0])
    print(fileName.split('_'))

    print (path+fileName,"分析结果")
    data = xlrd.open_workbook(path+fileName) # 打开xls文件
    table = data.sheets()[0] # 打开第一张表
    nrows = table.nrows # 获取表的行数3
    pNum = 0
    zongfen = 0
    manfen = 0
    up95 = 0
    up90 = 0
    up85 = 0
    up80 = 0
    up75 = 0
    up70 = 0
    up65 = 0
    up60 = 0
    up40 = 0
    up0 = 0
    quekao = 0
    dict = {}

    for i in range(nrows): # 循环逐行打印
        chengji = table.row_values(i)[2]
        name = table.row_values(i)[1]
       # print (chengji)
        if (name == ''): # 跳过空行
             continue
        if (name == '姓名'):  # 跳过空行
            continue
        if (chengji == '缺考'):  # 跳过缺考
            dict[name] = -1
            quekao = quekao +1
            continue
        if (name != ''):
            dict[name] = chengji
            zongfen = chengji + zongfen
        if(chengji == 100):
            manfen= manfen+1
        elif (100 > chengji >= 95):
            up95 = up95+1
        elif (95 > chengji >= 90):
            up90 =up90+1
        elif (90 > chengji >= 85):
            up85=up85+1
        elif (85 > chengji >= 80):
            up80 =up80+1
        elif (80 > chengji >= 75):
            up75 = up75 + 1
        elif (75 > chengji >= 70):
            up70 = up70 + 1
        elif (70 > chengji >= 65):
            up65 = up65 + 1
        elif (65 > chengji >= 60):
            up60 = up60 + 1
        elif (60 > chengji >= 40):
            up40 = up40 + 1
        else:
           up0=up0+1
        pNum=pNum+1

    # print ('参考总人数',pNum)
    # print ('缺考',quekao)
    # print ('总分',zongfen)
    # print ('平均分',zongfen/pNum)
    # print ('100分一共',manfen,'人','占比',manfen/pNum)
    # print ('95分以上一共',up95,'人','占比',up95/pNum)
    # print ('90分以上一共',up90,'人','占比',up90/pNum)
    # print ('80分以上一共',(up85 + up80),'人','占比',(up85 + up80)/pNum)
    # print ('60分以上一共',(up60+up65+up70+up75),'人','占比',(up60+up65+up70+up75)/pNum)
    # print ('60分以下一共',(up0+up40),'人','占比',(up0+up40)/pNum)


    # print(dict)
    a = sorted(dict.items(), key=lambda item: item[1],reverse = True)
    # print(dict.__len__())

    students = []

    if(type1 == 1):
        paiming = 1  # 排名方式1
        fenshu1 = a[0][1]  # 第一名分数
        for b in a:
            c = b[1]
            d = b[0]
            if (c < fenshu1):
                paiming += 1
                fenshu1 = c

            print(c, d, paiming, paiming)
            student = Student(d, c, paiming, paiming)
            students.append(student)
            # print(students)
            # student.__init__(d, c, paiming, paiming)
            # print(student)
            # print(c, d, paiming)
    else:
        paiming3 = 1
        paiming2 = 0  # 排名方式2
        fenshu2 = a[0][1]  # 第一名分数
        for b in a:
            c = b[1]
            d = b[0]
            paiming2 += 1
            if (c < fenshu2):
                paiming3 = paiming2
                fenshu2 = c
            # print(c, d, paiming3)
            student = Student(d, c, paiming3,paiming3)
            students.append(student)
           # print(student)

    assert isinstance(a, object)
    banji = BanJi(className ,testName,testNo,pNum ,zongfen ,manfen,up95,up90,up85,up80,up75,up70,up65,up60,up40,up0,quekao,students)
    print(banji)
    return banji

if __name__ == '__main__':
    a = getBanJiChengJi("..\\source\\",1)

    writeUtil.write_excel(a)


