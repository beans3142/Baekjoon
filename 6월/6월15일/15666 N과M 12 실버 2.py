import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
b=sorted(list(map(int,input().split())))
s={}

def bt(idx,arr):
    queue=deque([[idx,arr]])
    while queue:
        i,l=queue.popleft()
        if i == m+1:
            try:
                l=' '.join(map(str,l))
                s[l]
            except KeyError:
                s[l]=1
                print(l)
        else:
            for _ in range(n):
                if not l:
                    queue.append([i+1,l+[b[_]]])
                else:
                    if l[-1]<=b[_]:
                        queue.append([i+1,l+[b[_]]])

bt(1,[])
