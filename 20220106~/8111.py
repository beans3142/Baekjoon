from sys import stdin
from collections import deque
input=stdin.readline

vi=[[0,0] for i in range(20001)]
no=1

def add(n1,n2):
    return n1*10+n2
    

def able(n):
    while n:
        if n%10<2:
            n//=10
        else:
            return False
    return True

def bfs(n):
    global vi
    queue=deque([1])
    vi[1]=[1,no]

    while queue:
        now=queue.popleft()

        for i in range(2):
            nxt=add(now,i)%n
            if nxt!=0:
                if vi[nxt][1] != no:
                    vi[nxt]=[add(vi[now][0],i),no]
                    queue.append(nxt)
            else:
                return add(vi[now][0],i)
                    

for _ in range(int(input())):
    n=int(input())
    if able(n):
        print(n)
    else:
        res=bfs(n)
        print(res)
    no+=1
    
