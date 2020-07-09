#encoding=utf-8
with open('new_test.txt','w',encoding='urf-8') as f:
    f.write('this is first for firstline')

with open('new_test.txt','r+',encoding='utf-8') as r:
    #一次性读取全部文件内容
    conten = r.read()
    content = r.readlines()#一次性读取,所有行内容放到列表中
    #只读一行内容
    line=r.readline()
    print(line)
    #逐行读取
    for line in r:
        print(line)

