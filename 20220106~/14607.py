from math import *

co=1000001

def recur(x):
    if x<co:
        return arr[x]
    a=b=x/2
    a=ceil(a)
    b=floor(b)
    aa=recur(a)
    bb=recur(b)
    return aa+bb+a*b

n=int(input())

arr=[0,0,1,3]

for i in range(4,co):
    a=b=i/2
    a=ceil(a)
    b=floor(b)
    arr.append(arr[a]+arr[b])
    arr[-1]+=a*b

print(recur(n))

