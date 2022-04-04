from sys import stdin
from bisect import bisect_left

n=int(input())
arr=list(map(lambda x: -1*int(x),input().split()))
LIS=[arr[0]]
for i in range(n):
    if LIS[-1]<arr[i]:
        LIS.append(arr[i])
    else:
        idx=bisect_left(LIS,arr[i])
        LIS[idx]=arr[i]

print(len(LIS))
