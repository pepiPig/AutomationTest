'''write by @zly
Excel中有一列数据，需要把这一列数据都插入某数据库的临时表中，使用Python实现
插入语句如下，values内容为：日期+编号+数据内容
insert into owdoss.TEMP_DOSS (SERIAL_NUM) values (日期+编号+数据内容)'''


import xlrd
import xlwt
import time
#读取excel中的内容：读取excel中sheet1的每行内容，读取后重新插入，所以需要保存excel的格式为test.xlsx示例
'''
打开excel；
根据sheet名字获取excel表；
逐行读取excel中的内容，存放起来；
给每行的数据加上需要的字符
'''
def insertTemptable(input_number,input_dataRow,filepath):
    wb=xlrd.open_workbook(filepath)
    sheet=wb.sheet_by_name('Sheet1')
    i=0
    with open('临时表.txt','w',encoding='utf-8') as f:
        for cell in range(int(input_dataRow)):
            cells=sheet.row_values(cell)
            new_cells="insert into owdoss.TEMP_DOSS (SERIAL_NUM) values"+"("+time.strftime("%Y%m%d",time.localtime())+str(input_number)+str(cells[0])+")"+"\n"
            f.writelines(new_cells)
            i=i+1
            if i==10000:
                f.writelines('commit'+'\n')
                i=0
        f.writelines('commit'+'\n')

input_number=input('输入今天是第几次插入临时表：')
input_dataRow=input('输入数据总行数：')
filepath=input('文件名：')#test.xlsx
insertTemptable(input_number,input_dataRow,filepath)


