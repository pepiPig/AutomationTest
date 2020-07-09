import os
i=0
with open('file.py','r',encoding='utf-8') as f:
    #remove null lines
    for line in f:
        if line.strip():
            i=i+1
    print(i)

count=0
fp=open('file.py','r',encoding='utf-8')
for line in fp:
    for chr in line:
        if chr in "0123456789":
            count=count+1
            break
fp.close()
print(count)

'''1.统计特殊行，统计含有数字的行数
2.去掉空白行，统计行数
3.把文件内容拿出来，修改文件某一行内容
4.复制一张图片
'''
#把文件拿出来的方式
with open('test.txt','r',encoding='utf-8') as ff:
    lines=ff.readlines()
    print('以列表形式打印出所有的行数%s'%lines)
    for r in range(len(lines)):
        if "8" in lines[r]:
            lines[r]=lines[r].replace(lines[r],"")
    print(lines)
    print(lines[::-1])
    fw=open('test_new.txt','w',encoding='utf-8')
    #按行写入，可以写入列表
    fw.writelines(lines[::-1])
    fw.close()

#复制图片
with open('.jpg','rb') as image:
    conten=image.read()
    image.close()
    new=open('new.jpg','wb')
    new.write(conten)
    new.close()
