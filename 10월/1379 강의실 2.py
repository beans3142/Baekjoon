from sys import stdin
from heapq import heappop,heappush
from collections import deque,defaultdict
input=stdin.readline

n=int(input())
lecture=deque()
ans=defaultdict(int)
for i in range(n):
    cno,start,end=map(int,input().split())
    lecture.append((start,end,cno))

lecture=deque(sorted(lecture))
ends=[[-1,1]]
no=1

while lecture:
    time=lecture.popleft()
    if time[0]>=ends[0][0]:
        endtime,No=heappop(ends)
        ans[time[2]]=No
        heappush(ends,(time[1],No))
    else:
        no+=1
        ans[time[2]]=no
        heappush(ends,(time[1],no))
        

print(len(ends))
for i in range(1,n+1):
    print(ans[i])
