from sys import stdin
from collections import deque
input=stdin.readline
a,b=map(int,input().split())
queue=deque([(a,0,0)])
vi=[set(),set()];vi[0].add(a)
mx=1000000
while queue:
    now,move,magic=queue.popleft()
    if now==b:
        print(move)
        exit()
    for i in [1,now]:
        nxt=now+i
        if nxt not in vi[magic] and nxt<=mx:
            vi[magic].add(nxt)
            queue.append((nxt,move+1,magic))
    if magic==0:
        nxt=now*10
        if nxt not in vi[1] and nxt<=mx:
            vi[1].add(nxt)
            queue.append((nxt,move+1,1))
    
