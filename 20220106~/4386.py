from sys import stdin
input=stdin.readline

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def getcost(a,b):
    dx=(loc[a][0]-loc[b][0])**2
    dy=(loc[a][1]-loc[b][1])**2
    dist=(dx+dy)**0.5
    return dist

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        par[a]=b
        return True
    elif a==b:
        return False
    else:
        par[b]=a
        return True

n=int(input())

loc=[(0,0)]
par=[i for i in range(n+1)]

for i in range(n):
    a,b=map(float,input().split())
    loc.append((a,b))

queue=[]

for i in range(1,n+1):
    for j in range(i+1,n+1):
        val=(getcost(i,j),i,j)
        queue.append(val)

queue.sort()
cost=0

for needcost,a,b in queue:
    if union(a,b):
        cost+=needcost

print(cost)
