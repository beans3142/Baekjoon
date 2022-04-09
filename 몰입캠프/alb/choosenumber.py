from sys import *
from collections import *
#from math import *
#from itertools import *
#from heapq import *
#from bisect import *
#setrecursionlimit(100000)
#dx=[0,0,1,-1]
#dy=[1,-1,0,0]
input=stdin.readline

n=int(input())
s=[0]+[int(input()) for i in range(n)]
v=[0]*(n+1)
ans=[]
def dfs(x):
    global ans
    v[x]=1
    cycle.append(x)
    if s[x]==start:
        ans+=cycle
        return
    if v[s[x]]==0:
        dfs(s[x])
    v[x]=0
    
for start in range(1,n+1):
    cycle=[]
    dfs(start)
    v[start]=1

print(len(ans))
print(*sorted(ans))
