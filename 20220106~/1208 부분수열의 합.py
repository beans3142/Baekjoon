from sys import stdin
from collections import defaultdict
input=stdin.readline

n,s=map(int,input().split())
arr=list(map(int,input().split()))
ss=sum(arr[n//2:])
c=defaultdict(int)
cnt=0

def LSum(x,idx):
    global cnt
    for i in range(idx,n//2):
        nx=x+arr[i]
        if nx==s:
            cnt+=1
        c[nx]+=1
        LSum(nx,i+1)


LSum(0,0)

def Rsum(x,idx):
    global cnt
    for i in range(idx,n):
        nx=x+arr[i]
        if nx==s:
            cnt+=1
        cnt+=c[s-nx]
        Rsum(nx,i+1)

Rsum(0,n//2)

print(cnt)
