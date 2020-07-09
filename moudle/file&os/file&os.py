import os
#import pickle
import sys
with open('test.txt','w',encoding="UTF-8") as f:
    f.write('abcdefgr\n1208132')
    f.seek(4) #从位置4开始
    f.write('Hello')
fr=open('test.txt','r')
print('test.txt:',fr.read())
#f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
with open('test01.txt','r',encoding='utf-8') as fr:
    #print(fr.read(2))
    #print(fr.readlines())#若给定数字>0，返回实际size字节的行数
    print('test01.txt:',fr.read())
    fr.seek(4) #seek[offset[,whence] 把当前位置(进行读和写的位置)移动到offset和whence定义的位置，offset为偏移量
    print('test01.txt偏移四位:',fr.read())
frr=open('test01.txt','r')
for i in range(3):
    print(str(i) + ':', frr.readline())
#pipeline管式输出
# text=sys.stdin.read()
# words=text.split()
# wordcount=len(words)
# print(wordcount)

'''文件内容的迭代'''
'''1按字节处理文件，当到达文件末尾时候结束'''
def process(string):
    print('process:',string)
f=open('test01.txt','r')
while True:
    char=f.read(1)
    if not char:break
    process(char)
f.close()

'''使用pickle模块你可以把Python对象直接保存到文件，而不需要把他们转化为字符串，
也不用底层的文件访问操作把它们写入到一个二进制文件里。 
pickle模块会创建一个python语言专用的二进制格式，你基本上不用考虑任何文件细节，
它会帮你干净利落地完成读写独享操作，唯一需要的只是一个合法的文件句柄。'''

#目录操作
print (os.getcwd()) #返回当前目录
print(os.stat('test01.txt')) #指定路径的属性信息
#print(os.system('notepad'))
print(os.path.abspath(os.getcwd())) #绝对路径

print(dir(os))

# file.flush()
# 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入
