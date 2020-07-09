import os
def getAlldirDeep(path):
    stack = []
    stack.append(path)
    #当栈为空时结束循环
    while len(stack)!=0:
        dirpath= stack.pop()
        filelist = os.listdir(dirpath)
        for fileName in filelist:
            fileAbspath= os.path.join(dirpath,fileName)
            if os.path.isdir(fileAbspath):
                print("目录：", fileName)
                stack.append(fileAbspath)
            else:
                print ("普通文件:",fileName)

path='D:\Zhuliyuan\Software'
getAlldirDeep(path)