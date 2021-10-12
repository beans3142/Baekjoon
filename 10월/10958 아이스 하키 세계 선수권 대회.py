from sys import stdin
from collections import defaultdict
from bisect import bisect_right
input=stdin.readline

n,m=map(int,input().split())
hf=defaultdict(int)
arr=sorted(map(int,input().split()))
shf=[]
ans=1

def fs(x,idx):
    global ans
    for i in range(idx,n//2):
        nx=x+arr[i]
        if nx<=m:
            ans+=1
            shf.append(nx)
            hf[nx]+=1
        fs(nx,i+1)

fs(0,0)
shf=sorted(shf)

def bs(x,idx):
    global ans
    for i in range(idx,n):
        nx=x+arr[i]
        if nx>m:
            continue
        loc=bisect_right(shf,m-nx)
        ans+=1
        if loc>0:
            ans+=loc
        bs(nx,i+1)

bs(0,n//2)

print(ans)
