from sys import stdin
from collections import defaultdict
from collections import deque
input=stdin.readline
n=int(input())
bb=defaultdict(list)
times=[]
left=n
completetime=[0]*n
bef=[0]*(n)
for i in range(n):
    li=[*map(int,input().split())]
    times.append(li[0])
    for j in range(1,len(li)-1):
        bef[i]+=1
        bb[li[j]-1].append(i)


queue=deque([])

for i in range(n):
    if bef[i]==0:
        queue.append([i,0])

while queue:
    nowbuild,totaltime=queue.popleft()
    completetime[nowbuild]=max(completetime[nowbuild],totaltime)+times[nowbuild]
    for i in bb[nowbuild]:
        completetime[i]=max(totaltime+times[nowbuild],completetime[i])
    for building in bb[nowbuild]:
        bef[building]-=1
        if bef[building]==0:
            queue.append([building,completetime[building]])

for i in completetime:
    print(i)
