from sys import stdin
from collections import deque,defaultdict
from fractions import Fraction as fr
from math import ceil
input=stdin.readline

idx=1
while True:
    n=int(input())
    if n==0: break
    graph=defaultdict(dict)
    vi=defaultdict(int)
    for _ in range(n):
        c1,a,e,c2,b=input().rstrip().split()
        graph[a][b]=(int(c1),int(c2))
        graph[b][a]=(int(c2),int(c1))
    c,s=input().rstrip().split()
    vi[s]=1
    ans=0
    mx=1e10
    ansv=0
    queue=deque([(s,int(c),1)])
    while queue:
        now,boonja,boonmo=queue.popleft()
        for nxt in graph[now]:
            if vi[nxt]==0:
                vi[nxt]=1
                nxtbj=boonja*graph[now][nxt][1]
                nxtbm=boonmo*graph[now][nxt][0]
                intag=ceil(nxtbj/nxtbm)
                nowdif=(intag*nxtbm)/(nxtbj//int(c))-int(c)
                print(nxtbj/nxtbm,(intag*nxtbm)/(nxtbj//int(c)),intag,nowdif)
                if nowdif<mx:
                    ans=nxt
                    mx=nowdif
                    ansv=intag
                queue.append((nxt,nxtbj,nxtbm))
    print(f'Case {idx}: {ansv} {ans}')
    idx+=1
