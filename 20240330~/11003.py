from sys import stdin
from collections import deque
input=stdin.readline

n,l=map(int,input().split())
arr=list(map(int,input().split()))
ans=[0]*n
q=deque([])
if l==1:
    print(*arr)
    exit()
for i in range(l):
    if not q:
        q.append((arr[i],i))
    if q[-1][0]<arr[i]:
        q.append((arr[i],i))
    else:
        while q and q[-1][0]>=arr[i]:
            q.pop()
        q.append((arr[i],i))
    ans[i]=q[0][0]

for i in range(l,n):
    if i-q[0][1]>=l:
        q.popleft()
    if q[-1][0]<arr[i]:
        q.append((arr[i],i))
    else:
        while q and q[-1][0]>=arr[i]:
            q.pop()
        q.append((arr[i],i))
    ans[i]=q[0][0]
    
print(*ans)
