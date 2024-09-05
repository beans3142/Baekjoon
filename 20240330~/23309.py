from collections import defaultdict as dd
import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
#ans = __pypy__.builders.StringBuilder()

os.write(1, ans.build().encode())

n,m=map(int,input().split())
arr=list(map(int,input().split()))
rel={}
ans=[]
#dd(list)
for i in range(n):
    rel[arr[i]]=[arr[i-1],arr[(i+1)%n]]

for i in range(m):
    order=input().split()
    if order[0]=='BN':
        a,b=int(order[-2]),int(order[-1])
        nxt=rel[a][1]
        ans.append(nxt)
        rel[a][1]=rel[nxt][0]=b
        rel[b]=[a,nxt]
    elif order[0]=='BP':
        a,b=int(order[-2]),int(order[-1])
        bef=rel[a][0]
        ans.append(bef)
        rel[a][0]=rel[bef][1]=b
        rel[b]=[bef,a]
    elif order[0]=='CN':
        a=int(order[-1])
        nxt=rel[a][1]
        ans.append(nxt)
        rel[a][1]=rel[nxt][1]
        rel[rel[nxt][1]][0]=a
    else:
        a=int(order[-1])
        bef=rel[a][0]
        ans.append(bef)
        rel[a][0]=rel[bef][0]
        rel[rel[bef][0]][1]=a
print(*ans,sep="\n")
