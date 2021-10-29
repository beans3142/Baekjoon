from sys import stdin
from heapq import heappop,heappush
input=stdin.readline

n=int(input())
queue=[]
ans=[]

for i in range(n):
    d,w=map(int,input().split())
    heappush(queue,(d,w))

while queue:
    a=heappop(queue)
    if len(ans)<a[0]:
        heappush(ans,a[1])
    elif len(ans)==a[0] and ans[0]<a[1]:
        heappop(ans)
        heappush(ans,a[1])

print(sum(ans))
