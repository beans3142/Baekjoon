from sys import stdin
from collections import deque
input=stdin.readline

def check(a,b,c):
    return a**2+b**2+c**2==k*(a*b+b*c+c*a)+1

k,n=map(int,input().split())

queue=deque([(0,0,1)])
used=set()
ans=[]
mx=10**101

while queue:
    if len(ans)>=n:
        break
    a,b,c=queue.popleft()
    for i in range(3):
        nn=k*b+k*c-a
        if 0<nn<mx:
            queue.append([nn,b,c])
        a,b,c=b,c,a
    if a not in used and b not in used and c not in used:
        if a!=b and b!=c and a!=c and min(a,b,c)>0:
            used.add(a)
            used.add(b)
            used.add(c)
            ans.append([a,b,c])
            
    

for i in range(n):
    print(*ans[i])
