from sys import stdin
input=stdin.readline

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        par[b]=a
    else:
        par[a]=b

n,m=map(int,input().split())
par=[i for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    union(a,b)

order=list(map(int,input().split()))
cnt=0

for i in range(1,n):
    if find(order[i])!=find(order[i-1]):
        cnt+=1
    

print(cnt)
