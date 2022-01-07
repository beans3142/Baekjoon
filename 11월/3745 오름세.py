from sys import stdin
from bisect import bisect_left

try:
    while True:
        n=int(input())
        arr=list(map(int,input().split()))
        LIS=[arr[0]]
        for i in range(len(arr)):
            if LIS[-1]<arr[i]:
                LIS.append(arr[i])
            else:
                idx=bisect_left(LIS,arr[i])
                LIS[idx]=arr[i]

        print(len(LIS))
except:
    pass
