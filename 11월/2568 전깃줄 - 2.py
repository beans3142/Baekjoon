from sys import stdin
from collections import deque
from bisect import bisect_left

n=int(input())
s=sorted([list(map(int,input().split())) for i in range(n)])
arr=[i[1] for i in s]
ans={i[1]:i[0] for i in s}
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

print(n-len(LIS))
idx=1
result=deque([])

for i in range(start_at,-1,-1):
    if l[i][0]==len(LIS)-idx:
        result.appendleft(arr[l[i][1]])
        idx+=1
        if idx>len(LIS):
            break

for i in result:
    del ans[i]

for i in sorted(ans[i] for i in ans):
    print(i)
