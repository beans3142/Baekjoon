from sys import stdin
from heapq import heappop,heappush
from collections import deque
input=stdin.readline

n=int(input())
lecture=deque()
for i in range(n):
    no,start,end=map(int,input().split())
    lecture.append((start,end))
lecture=deque(sorted(lecture))
ends=[-1]

cnt=0

while lecture:
    time=lecture.popleft()
    print(ends)
    if time[0]>=ends[0]:
        heappop(ends)
        heappush(ends,time[1])
    else:
        cnt+=1
        heappush(ends,time[1])
        

print(len(ends))
