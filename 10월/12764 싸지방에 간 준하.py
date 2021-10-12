from sys import stdin
from heapq import heappop,heappush
from collections import deque
input=stdin.readline

n=int(input())
lecture=deque()
for i in range(n):
    start,end=map(int,input().split())
    lecture.append((start,end))
lecture=deque(sorted(lecture))
ends=[[-1,0]]
able=[]
no=0
ans=[0]

cnt=0

while lecture:
    time=lecture.popleft()
    #print(ends)
    if time[0]>=ends[0][0]:
        while ends and time[0]>=ends[0][0]:
            t,No=heappop(ends)
            heappush(able,[No,t])
    #print(able)
    if able and time[0]>=able[0][1]:
        No,t=heappop(able)
        ans[No]+=1
        heappush(ends,[time[1],No])
    else:
        cnt+=1
        ans.append(1)
        no+=1
        heappush(ends,[time[1],no])

print(len(ans))
print(*ans)
