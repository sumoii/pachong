#!/user/bin/python3
# -*- codeing = utf-8 -*-
import xlwt
workbook = xlwt.Workbook(encoding='utf -8')
worksheet = workbook.add_sheet('sheet1')
# worksheet.write(0,0,'hello')

for i in range(0,9):
    for t in range(0,9):
        while i>=t:
            worksheet.write(i,t,"%d*%d=%d"%((i+1),(t+1),(i+1)*(t+1)))
            t=t+1
            break
    i=i+1
workbook.save('student.xls')
# workbook = xlwt.workbook(encoding='utf -8')
# worksheet = workbook.add.sheet('sheet1')
# worksheet.write(0,0,'hello')
# workbook.save('student.xls')