#递归方法
def sum(n):
    if n==1 or n==2:
        return 1
    elif (n>2):
        return sum(n-1)+sum(n-2)

#非递归方法
def sumP(n):
    a, b = 1, 1
    if n==1 or n==2:
        return 1
    elif(n>=3):
        for i in range(n-2):
            a,b=b,a+b
        return b

for i in range(1,101):
    print('第%d行：%d'%(i,sumP(i)))

for i in range(1, 101):
    if sumP(i)%2==0:
        print('属于偶数的斐波那契数列：第%d行，值：%d' % (i, sumP(i)))
