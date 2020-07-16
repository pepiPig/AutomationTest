#NumPy包的核心是ndarray对象，N维数组
一维数组，arr=numpy.array([1,2,3,4])
二维数组，arr=numpy.array([[1,2,3,4],[3,4,5,6]])
a=numpy.arange(5)
a=numpy.arange(5,dtype=float)
a=numpy.arange(5,6,7)
date=numpy.genfromtxt('.csv',delimiter=',')

数组属性：
ndim（数据维度的数量）shape（数据对象的尺度） size（大小）
print(arr.ndim)  

数组的切片和索引与Python的list索引相似：
一维数组： print(arr[:6:1])  每隔一个取6个数
二维数组：print(arr([0:3],[2:5]) 行，列

形状转换：
arr.reshape 
arr.resize  
arr.ravel  flatten  降维

统计函数：arr.sum()
sum() mean() max() min()
添加横轴纵轴方向
sum(axis=0) 打印第一行的总和
np.sort(arr,axis=2)) 排序

#二维数组定义
data=[[],[]]
pandas.DataFrame(data,columns=['',''],index=[''])

字典：dictionary=[{'':'','':''},{'':''},{'':'','':''}]
pandas.DataFrame(dictionary,columns=['',''],index=[''])

csv格式数据读取
df=pandas.read_csv(filepath,header=0) #header取第几行
print(df.head(5))
print(df[列名])
df[['','']]
df.loc['':''] #第几列到第几列，左闭右闭
df.loc['x2':'x4',['y1','y2']]
df['x2':'x4',['y1','y2']] #行用：，列用，
df[df['x2']>=6] #打x2行中>=6的数值

df.count() df.min() df.max() 

df.sort_values([],)
df_group=df.groupby()
df_group['math'].agg("mean")

作业：
df=pd.read_csv('D:\sgmuserprofile\gu yifeng\Downloads\students_complete.csv')
#打印前十行数据
print(df.head(10))
#计算数学平均分
print(df['math_score'].mean())
#统计不及格学生人数
print(df[df['math_score']<60 & df['Student ID']]['Student ID'].count())
#从高到低打印每个学校的平均分数
df01=df_group['math_score'].agg("mean")
data=pd.DataFrame(df01,columns=['math_score'])
print(data.sort_values('math_score',ascending='True'))

#Python迭代器：
创建迭代器对象，iter()
输出迭代器的下个元素 next()
