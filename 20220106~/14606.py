from math import *
n=int(input())
arr=[0,0,1,3]
for i in range(4,11):
    a=b=i/2
    a=ceil(a)
    b=floor(b)
    arr.append(arr[a]+arr[b])
    arr[-1]+=a*b

print(arr[n])
