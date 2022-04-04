from collections import *
import sys
input=sys.stdin.readline
n=int(input())
arr=[i for i in range(n)]
i=0
arr=deque(arr)
while len(arr)>1:
    x=arr.popleft()
    if i%2==1:
        arr.append(x)
    i+=1

print(arr[0]+1)
