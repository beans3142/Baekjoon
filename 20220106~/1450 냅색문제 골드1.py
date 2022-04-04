from sys import stdin
from collections import deque

n,c=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
while arr[-1]>c:
    arr.pop()

queue=deque([[0,[0 for i in range(len(arr))],0]])
cnt=1
while queue:
    l,v,s=queue.popleft()
    for i in range(l,len(arr)):
        ns=s+arr[i]
        if v[i]==0 and s+arr[i]<=c:
            v[i]=1
            queue.append([i,v,s+arr[i]])
            cnt+=1
            v[i]=0

print(cnt)
