from heapq import heappop,heappush
import sys
input=sys.stdin.readline
inf=sys.maxsize

a,b=map(int,input().split())
n,m=map(int,input().split())

word={i:[]for i in range(1,n+1)}

for i in range(m):
    w1,w2=map(int,input().split())
    word[w1].append(w2)
    word[w2].append(w1)

queue=[(0,a)]
change=[inf]*(n+1)

while queue:
    tmpt,now=heappop(queue)
    if tmpt>change[now]:
        continue
    change[now]=tmpt
    for i in word[now]:
        if change[i]>tmpt+1:
            change[i]=tmpt+1
            heappush(queue,(tmpt+1,i))

print(change[b] if change[b]!=inf else -1)
        
