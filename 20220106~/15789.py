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

    if par[a]<par[b]:
        power[a][0]+=power[par[b]][0]
        par[b]=a
    elif par[a]>par[b]:
        power[b][0]+=power[par[a]][0]
        par[a]=b

n,m=map(int,input().split())
par=[i for i in range(n+1)]
power=[[1,i] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    union(a,b)

c,h,k=map(int,input().split())
find(c)
find(h)

ans=power[c][0]
spower=sorted(power,reverse=True)
cnt=0

for po,idx in spower:
    if cnt==k:
        break
    p=find(idx)
    if p!=par[h] and p!=par[c]:
        union(p,c)
        cnt+=1

print(power[par[c]][0])
