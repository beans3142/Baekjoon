from sys import stdin
from collections import *
input=stdin.readline

n=int(input())
d1=defaultdict(int)
d2=defaultdict(int)

for i in range(n):
    a,b=map(int,input().split())
    d1[a]+=1
    d2[b]+=1

a=[(-cnt,grade) for grade,cnt in d1.items()]
a.sort()
b=[(-cnt,grade) for grade,cnt in d2.items()]
b.sort()
ans=min(a[0],b[0])
print(-ans[0],ans[1])
