from sys import stdin
from math import log
from bisect import bisect_left
input=stdin.readline

n,k,q=map(int,input().split())

case=[0]
for i in range(64):
    if n<case[-1]:
        break
    case.append(case[-1]+k**i)
if k==1:
    for i in range(q):
        x,y=map(int,input().split())
        print(abs(x-y))
else:
    for _ in range(q):
        x,y=map(int,input().split())
        xdep=bisect_left(case,x)
        ydep=bisect_left(case,y)
        cnt=abs(xdep-ydep)
        for i in range(xdep,ydep):
            y=(y+k-2)//k
        for j in range(ydep,xdep):
            x=(x+k-2)//k
        while x!=y:
            y=(y+k-2)//k
            x=(x+k-2)//k
            cnt+=2
        print(cnt)
