import os
def getAlldir(path,sp='',i=0):

    filelist=os.listdir(path)
    sp = sp +' '
    i=i+1
    for fileName in filelist:
        fileAbspath=os.path.join(path,fileName)
        if os.path.isdir(fileAbspath):
            print(sp+"目录：",i,fileName)
            getAlldir(fileAbspath,sp,i)
        else:
            print(sp+"普通文件：",i,fileName)

path='D:\Zhuliyuan\Software'
getAlldir(path)