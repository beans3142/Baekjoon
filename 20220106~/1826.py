from sys import stdin
from heapq import heappush,heappop
input=stdin.readline

n=int(input())
q=[]
for i in range(n):
    a,b=map(int,input().split())
    q.append([a,b])
q.sort()

l,p=map(int,input().split())
idx=0
pq=[]
cnt=0
while idx<len(q) and p<l:
    while idx<len(q) and q[idx][0]<=p:
        a=q[idx][0]
        b=-q[idx][1]
        heappush(pq,(b,a))
        idx+=1
    if not pq:
        break
    stop=heappop(pq)
    p+=-1*stop[0]
    cnt+=1

if l<=p:
    print(cnt)
else:
    print(-1)
