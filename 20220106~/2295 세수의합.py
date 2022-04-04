from sys import stdin
from collections import defaultdict
input=stdin.readline

n=int(input())
arr={}
two={}
lst=[]
mx=0

for i in range(1,n+1):
    a=int(input())
    arr[a]=a
    lst.append(a)

for i in range(n):
    for j in range(i,n):
        two[lst[i]+lst[j]]=1

for i in range(n):
    for j in range(n):
        num=lst[j]-lst[i]
        try:
            two[num]
            mx=max(mx,lst[j])
        except:
            pass

print(mx)
