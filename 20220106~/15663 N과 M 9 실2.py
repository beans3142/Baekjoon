import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
b=sorted(list(map(int,input().split())))
s={}

def bt(idx,arr,V):
    queue=deque([[idx,arr,V]])
    while queue:
        i,l,v=queue.popleft()
        if i == m+1:
            try:
                l=' '.join(map(str,l))
                s[l]
            except KeyError:
                s[l]=1
                print(l)
        else:
            for _ in range(n):
                if v[_]==0:
                    nv=list(v)
                    nv[_]=1
                    queue.append([i+1,l+[b[_]],nv])

bt(1,[],[0]*n)
