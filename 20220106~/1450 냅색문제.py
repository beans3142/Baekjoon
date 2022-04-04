from sys import stdin
from bisect import bisect_right
input=stdin.readline
n,c=map(int,input().split())
arr=[i for i in sorted(map(int,input().split())) if i<=c]
n=len(arr)
d=[]
ans=1

def fh(x,idx):
    global ans
    for i in range(idx,n//2):
        val=x+arr[i]
        if val<=c:
            d.append(val)
            ans+=1
            fh(val,i+1)
fh(0,0)

d.sort()

def bh(x,idx):
    global ans
    for i in range(idx,n):
        val=x+arr[i]
        if val<=c:
            ans+=1+bisect_right(d,c-val)
            bh(val,i+1)

bh(0,n//2)
        
print(ans)
