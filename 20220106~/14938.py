from sys import stdin
from math import gcd
from collections import defaultdict
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in graph[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
    return False
        

n=int(input())
arr=list(map(int,input().split()))
pown=set()
for i in range(1,2000001):
    pown.add(i**2)
    
graph=defaultdict(list)

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if arr[i]%2==1 and arr[j]%2==0:
            if gcd(arr[i],arr[j])!=1:
                continue
            num=arr[i]**2+arr[j]**2
            if num in pown:
                graph[i].append(j)

rev=[-1]*(1000001)
cnt=0
for i in graph:
    vi=defaultdict(bool)
    if dfs(i):
        cnt+=1

print(cnt)
