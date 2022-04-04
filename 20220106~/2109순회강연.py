from sys import stdin
from heapq import heappush,heappop
input=stdin.readline

n=int(input())
queue=[]
ans=[]

for i in range(n):
    a,b=map(int,input().split())
    heappush(queue,(b,-a))

while queue:
    first=heappop(queue)
    if len(ans)<first[0]:
        heappush(ans,-first[1])
    elif len(ans)==first[0] and ans[0]<-first[1]:
        heappop(ans)
        heappush(ans,-first[1])

print(sum(ans))
