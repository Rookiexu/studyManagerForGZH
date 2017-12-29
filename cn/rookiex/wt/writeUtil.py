#把传入的数据写成对应的excl文件
#需要有几个文件,一个是班级的排名(文件1),一个是年级的排名(文件2),然后是成绩的整理(总分,平均分,分段区分)(文件3)
#一个学生需要有一个表格,或者说一行数据分数,本班排名(+-x),多班排名(+-x)
import xlwt

def set_style(name, height, bold = False):
    style = xlwt.XFStyle()   #初始化样式

    font = xlwt.Font()       #为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style

def write_excel(banjis):
    #创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')

    for banji in banjis:
        students = banji.Students
        lens = len(students)
        print(banji.name)
        data_sheet = workbook.add_sheet(banji.name+banji.testName)
        for i in range(lens ):
            j = 0
            student = students[i]
            while (j < 4):
                data_sheet.write(i, j, student.getInfo(j), xlwt.XFStyle())
                j += 1
                # data_sheet.write(1, i, row1[i], xlwt.XFStyle())
        row0 = ['班级', '考试人数', '缺考人数', '100分/人', '95~99.5', '90~94.5', '80~89.5', '70~79.5', '60~69.5', '60以下','90以上比例',
                '60以下比例', '总分', '平均分']
        row1 = [banji.name, banji.pNum, banji.quekao, banji.manfen, banji.up95, banji.up90, banji.up80 + banji.up85,
                banji.up70 + banji.up75, banji.up60 + banji.up65, banji.up0 + banji.up40,
                (banji.up90 + banji.up95 + banji.manfen) / banji.pNum, (banji.up0 + banji.up40) / banji.pNum,
                banji.zongfen, banji.zongfen / banji.pNum]

        for i in range(len(row0)):
            data_sheet.write(lens+1, i, row0[i], xlwt.XFStyle())
            data_sheet.write(lens+2, i, row1[i], xlwt.XFStyle())
    #生成第一行和第二行
    # for i in range(len(row0)):
    #     j = 0
    #     while(j < 4):
    #         data_sheet.write(i, j, row0[i], xlwt.XFStyle())
    #         j+=1
        # data_sheet.write(1, i, row1[i], xlwt.XFStyle())

    #保存文件
    workbook.save('..//writePath//demo.xls')
    print('a')

# if __name__ == '__main__':
#     write_excel(0)
#     print (u'创建demo.xlsx文件成功')