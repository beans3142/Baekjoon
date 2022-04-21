from sys import stdin
from heapq import *
from collections import defaultdict
input=stdin.readline

n,k=map(int,input().split())
hq=list(map(int,input().split()))
st=sorted(hq)

for i in range(k):
    now=heappop(hq)
    for i in st:
        heappush(hq,now*i)
        if now%i==0:
            break
            
print(now)
