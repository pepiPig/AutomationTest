import os
#目录操作
print (os.getcwd()) #返回当前目录
print(os.stat('test01.txt')) #指定路径的属性信息
#print(os.system('notepad'))
print(os.path.abspath(os.getcwd())) #绝对路径
print(dir(os))
'''
建立一个十级目录的深度，每一层目录名叫testzly
每一层目录下面，新建两个文件，文件1文件2
'''
# os.mkdir("testzly")
# for i in range(1,11):
#     dirname='testzly'+str(i)
#     os.chdir(dirname)
# os.path.split()#获取文件名/目录名
# os.path.dirname()
# os.path.basename()
# os.path.exists("")
'''练习：统计一个下面的文件有几个，目录有几个？'''
# os.path.isdir()
# os.path.isfile()
path='moudle/file&os'
dircount=0
for filename in os.listdir(path):
    newpath=os.path.join(path,filename)
    if os.path.isdir(newpath):
        dircount+=1
print(dircount)