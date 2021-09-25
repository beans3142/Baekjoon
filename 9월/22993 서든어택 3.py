from sys import stdin
from collections import deque
input=stdin.readline
n=int(input())
arr=deque(map(int,input().split()))
p1=arr.popleft()
arr=sorted(arr)
able=True
for i in arr:
    if i>=p1:
        able=False
        break
    elif i<p1:
        p1+=i

if able:
    print("Yes")
else:
    print("No")
    
