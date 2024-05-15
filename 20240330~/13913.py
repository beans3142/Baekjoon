from sys import stdin
from collections import deque
input=stdin.readline

n,k=map(int,input().split())
if n==k:
    print(0)
    print(n)
    exit()
vi=[-1]*100001
ans=[k]
queue=deque([n])
vi[n]=n

while queue:
    now=queue.popleft()
    for i in [1,-1,now]:
        nxt=now+i
        if -1<nxt<100001 and vi[nxt]==-1:
            vi[nxt]=now
            queue.append(nxt)
            if nxt==k:
                while vi[k]!=n:
                    k=vi[k]
                    ans.append(k)

                print(len(ans))
                print(n,*ans[::-1])
                exit()
