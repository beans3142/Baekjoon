import sys
from collections import deque
input=sys.stdin.readline

def dslr():
    queue=deque()
    queue.append([N,''])
    while queue:
        n,before=queue.popleft()
        d=(n*2)%10000
        if d==end:  
            return before+'D'
        elif visited[d]==0:
            visited[d]=1
            queue.append([d,before+'D'])
        s=n-1 if n!=0 else 9999
        if s==end:
            return before+'S'
        elif visited[s]==0:
            visited[s]=1
            queue.append([s,before+'S'])
        l=n%1000*10+n//1000
        if l==end:
            return before+'L'
        elif visited[l]==0:
            visited[l]=1
            queue.append([l,before+'L'])
        r=n%10*1000+n//10
        if r==end:
            return before+'R'
        elif visited[r]==0:
            visited[r]=1
            queue.append([r,before+'R'])
        
for i in range(int(input())):
    N,end=map(int,input().split())
    visited=[0 for i in range(10000)]
    print(dslr())
