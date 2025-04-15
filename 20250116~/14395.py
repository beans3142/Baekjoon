from sys import stdin;input=stdin.readline
from collections import deque
s,t=map(int,input().split())
vi=set()
def bfs():
    queue=deque([(0,s),(1,s*s),(2,s+s),(3,0),(4,1)])
    vi.union([0,1,s,s+s,s*s])
    cal=[0,lambda x:x*x,lambda x:x+x,lambda x:x-x,lambda x:x//x]
    while queue:
        acc,now=queue.popleft()
        if now==t:
            return acc
        for i in range(1,3):
            nxt=cal[i](now)
            if nxt not in vi and nxt<=10**9:
                vi.add(nxt)
                queue.append((acc*10+i,nxt))
    return -1
res=bfs()
if res<=0:
    print(res)
else:
    ans=[]
    while res:
        ans.append('*+-/'[res%10-1])
        res//=10
    print(*ans[::-1],sep='')
