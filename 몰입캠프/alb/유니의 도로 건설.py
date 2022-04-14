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
    if par[a]>par[b]:
        par[a]=b
    elif par[a]<par[b]:
        par[b]=a
    else:
        return -1

n=int(input())
arr=sorted([list(map(int,input().split())) for i in range(n)])
par=[i for i in range(2*n+1)]

for i in arr:
    a,b,c,d,e=i
    union(b,c)
    union(d,e)

ans=0
#print(par)
for i in arr:
    a,b,c,d,e=i
    if find(b)!=find(d):
        ans+=a
        union(b,d)
        union(c,e)
        #print(par)

print(ans)
