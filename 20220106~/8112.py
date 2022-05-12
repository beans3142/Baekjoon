from sys import stdin
from collections import deque
input=stdin.readline

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
    vi[1]=1

    while queue:
        now=queue.popleft()

        for i in range(2):
            nxt=add(now,i)%n
            if nxt!=0:
                if vi[nxt]==0:
                    vi[nxt]=add(vi[now],i)
                    queue.append(nxt)
                    
            else:
                return add(vi[now],i)
                return add(vi[now][0],i)
    return False
                    

for _ in range(int(input())):
    n=int(input())
    vi=[0 for i in range(1000001)]
    if able(n):
        print(n)
    else:
        res=bfs(n)
        if res>0:
            print(res)
        else:
            print("BRAK")
    
