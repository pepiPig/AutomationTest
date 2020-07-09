import collections
import os

def getAlldirWide(path):
    queue=collections.deque()
    queue.append(path)

    while len(queue)!=0:
        dirpath=queue.popleft()
        filelist=os.listdir(dirpath)
        for fileName in filelist:
            fileAbspath = os.path.join(dirpath, fileName)
            if os.path.isdir(fileAbspath):
                queue.append(fileAbspath)
                print ("目录：",fileName)
            else:
                print("普通文件：",fileName)

path='D:\Zhuliyuan\Software'
getAlldirWide(path)