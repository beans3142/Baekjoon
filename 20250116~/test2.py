from math import *

def getAns(x):
    for i in range(round(500000/x**2),floor(100-1250/(125-x))):
        res.append(i)

def getRes(x, y):
    res1 = y * x**2
    res2 = (n1 - x) * (n2 - y)
    flag = res1 - 500000 > 0 and res2 - 1250 > 0
    if flag:
        return ((res1 - 500000, res2 - 1250), res1, res2, x, y)
    else:
        return (res1 - 500000, res2 - 1250)
n1=125
n2=100
for i in range(1,100):
    res=[]
    getAns(i)
    if res:
        for j in res:
            print(i,j,getRes(i,j))
        print()
