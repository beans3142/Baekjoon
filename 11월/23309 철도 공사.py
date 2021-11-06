from sys import stdin
from collections import defaultdict as dd
input=stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))
rel=dd(list)
for i in range(n):
    rel[arr[i]]=[arr[i-1],arr[(i+1)%n]]

for i in range(m):
    order=input().rstrip().split()
    if order[0]=='BN':
        a,b=int(order[-2]),int(order[-1])
        nxt=rel[a][1]
        print(nxt)
        rel[a][1]=rel[nxt][0]=b
        rel[b]=[a,nxt]
    elif order[0]=='BP':
        a,b=int(order[-2]),int(order[-1])
        bef=rel[a][0]
        print(bef)
        rel[a][0]=rel[bef][1]=b
        rel[b]=[bef,a]
    elif order[0]=='CN':
        a=int(order[-1])
        nxt=rel[a][1]
        print(nxt)
        rel[a][1]=rel[nxt][1]
        rel[rel[nxt][1]][0]=a
    else:
        a=int(order[-1])
        bef=rel[a][0]
        print(bef)
        rel[a][0]=rel[bef][0]
        rel[rel[bef][0]][1]=a
