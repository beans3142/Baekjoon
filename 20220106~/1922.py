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
        return True
    elif a==b:
        return False
    else:
        par[a]=b
        return True



n=int(input())
m=int(input())
arr=sorted([list(map(int,input().split()))[::-1] for i in range(m)])

par=[i for i in range(n+1)]

ans=0

for c,a,b in arr:
    if union(a,b):
        ans+=c
    
print(ans)
