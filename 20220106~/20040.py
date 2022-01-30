from sys import stdin,setrecursionlimit
input=stdin.readline
setrecursionlimit(250000)
n,m=map(int,input().split())
par=list(range(n))

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        par[a]=b
        return 1
    elif a<b:
        par[b]=a
        return 1
    else:
        return 0

end=0


for i in range(m):
    a,b=map(int,input().split())
    if not union(a,b):
        end=i+1
        break

print(end)
