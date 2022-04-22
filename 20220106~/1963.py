from sys import stdin
from collections import *
input=stdin.readline

prime=[1]*10000
prime[0]=prime[1]=0
for i in range(2,101):
    if prime[i]==0:
        continue
    for j in range(i+i,10000,i):
        prime[j]=0

n=int(input())
vi=[0]*(10001)

def bfs(s,e):
    queue=deque([s])
    change=0
    vi[s]=1
    while queue:
        le=len(queue)
        for i in range(le):
            now=queue.popleft()
            if now==e:
                return change
            
            thou=now%1000
            hun=now-(now%1000//100)*100
            ten=now-(now%100//10)*10
            one=now-(now%10)
            for i in range(1,10):
                num=thou+1000*i
                if vi[num]==0 and prime[num]==1:
                    vi[num]=1
                    queue.append(num)
            for i in range(10):
                num=hun+100*i
                if vi[num]==0 and prime[num]==1:
                    vi[num]=1
                    queue.append(num)
            for i in range(10):
                num=ten+10*i
                if vi[num]==0 and prime[num]==1:
                    vi[num]=1
                    queue.append(num)
            for i in range(1,10):
                num=one+i
                if vi[num]==0 and prime[num]==1:
                    vi[num]=1
                    queue.append(num)
        change+=1
    return -1
            
        

for i in range(n):
    vi=[0]*10001
    p1,p2=map(int,input().split())
    ans=bfs(p1,p2)
    if ans>-1:
        print(ans)
    else:
        print('Impossible')
