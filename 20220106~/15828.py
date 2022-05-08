from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
queue=deque([])

while True:
    a=int(input())
    if a==-1:
        break
    if a==0:
        if queue:
            queue.popleft()
            continue
    if len(queue)>=n:
        continue
    queue.append(a)

if queue:
    print(*queue)
else:
    print('empty')
    
