from sys import stdin
from heapq import *
input=stdin.readline

n=int(input())
left=sorted([list(map(int,input().split())) for i in range(n)])
end=[]
cnt=0

while left:
    s,e=heappop(left)
    if end and s>=end[0]:
        heappop(end)
        heappush(end,e)
    else:
        heappush(end,e)
        cnt+=1

print(cnt)
