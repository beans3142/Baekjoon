from sys import stdin
input=stdin.readline
from collections import deque

S=input().rstrip()
E=input().rstrip()

s=sum([2**i*int(S[~i]) for i in range(len(S))])
e=sum([2**i*int(E[~i]) for i in range(len(E))])
vi=[-1]*2100
vi[s]=0
queue=deque([s])

while queue:
    now=queue.popleft()
    for i in range(10):
        xor=2**i
        if xor>now//2:
            break
        if vi[now^xor]==-1:
            vi[now^xor]=vi[now]+1
            queue.append(now^xor)
    if vi[now+1]==-1 and now+1<1024:
        vi[now+1]=vi[now]+1
        queue.append(now+1)
    if vi[now-1]==-1 and now-1>0:
        vi[now-1]=vi[now]+1
        queue.append(now-1)

print(vi[e])
