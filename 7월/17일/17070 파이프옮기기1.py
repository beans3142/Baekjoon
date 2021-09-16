from sys import stdin
from collections import deque

input=stdin.readline

n=int(input())
arr=[input().rstrip().split() for i in range(n)]
cnt=0

queue=deque([[0,0,1,0]])

while queue:
    x1,y1,x2,y2=queue.popleft()
    if x2==n-1 and y2==n-1:
        cnt+=1
        continue
    if x1!=x2:
        if x2+1<n and arr[y2][x2+1]=='0':
            queue.append([x2,y2,x2+1,y2])
    if y1!=y2:
        if y2+1<n and arr[y2+1][x2]=='0':
            queue.append([x2,y2,x2,y2+1])
    if y2+1<n and x2+1<n:
        if arr[y2+1][x2+1]=='0' and arr[y2+1][x2]=='0' and arr[y2][x2+1]=='0':
            queue.append([x2,y2,x2+1,y2+1])

print(cnt)
