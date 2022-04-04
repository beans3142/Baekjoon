from heapq import heappop,heappush
from sys import stdin
from collections import defaultdict
input=stdin.readline

n,m=map(int,input().split())

order={i:[] for i in range(1,n+1)}
level={i:0 for i in range(1,n+1)}

for i in range(m):
    a,b=map(int,input().split())
    order[a].append(b)
    level[b]+=1

while level:
    for i in level:
        if level[i]==0:
            print(i,end=' ')
            for nxt in order[i]:
                level[nxt]-=1
            del level[i]
            break
