from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
arr=[10000]*(100000)

queue=deque([(1,0)])

while queue:
    now,pushtime=queue.popleft()
    if now>99999 or arr[now]<=pushtime:
        continue
    arr[now]=pushtime
    queue.append((now*2,pushtime+1))
    queue.append((now//3,pushtime+1))
    
print(arr[n])
