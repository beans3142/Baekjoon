from sys import stdin
from collections import defaultdict
input=stdin.readline

n,k,d=map(int,input().split())
arr=[]
dd=defaultdict(list)
now=defaultdict(int)

for i in range(n):
    M,D=map(int,input().split())
    arr.append((D,M,i))
    ai=list(map(int,input().split()))
    for j in ai:
        dd[i].append(j)

arr.sort()

s=0
e=0
ans=0

while s<n and e<n:
    if arr[e][0]-arr[s][0]<=d:
        idx=arr[e][2]
        for i in dd[idx]:
            now[i]+=1
        e+=1
    else:
        idx=arr[s][2]
        for i in dd[idx]:
            now[i]-=1
            if now[i]==0:
                del now[i]
        s+=1
    #print(now,e-s)
    v=0
    cnt=e-s
    le=len(now)
    for i in now:
        if now[i]==cnt:
            le-=1
    ans=max(ans,le*cnt)

print(ans)
