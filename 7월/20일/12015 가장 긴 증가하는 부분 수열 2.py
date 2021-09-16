from sys import stdin
from collections import deque
from bisect import bisect_left

n=int(input())
arr=list(map(int,input().split()))
LIS=[arr[0]]
l=[]

for i in range(n):
    if LIS[-1]<arr[i]:
        l.append((len(LIS),i))
        LIS.append(arr[i])
        start_at=i
    else:
        if LIS[-1]==arr[i]:
            start_at=i
        idx=bisect_left(LIS,arr[i])
        LIS[idx]=arr[i]
        l.append((idx,i))

print(len(LIS))
idx=1
result=deque([])

for i in range(start_at,-1,-1):
    if l[i][0]==len(LIS)-idx:
        result.appendleft(arr[l[i][1]])
        idx+=1
        if idx>len(LIS):
            break

print(*result)
