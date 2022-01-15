from sys import stdin
input=stdin.readline

def find(tar):
    if tar==par[tar]:
        return tar
    par[tar]=find(par[tar])
    return par[tar]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        par[b]=a
    elif a==b:
        par[b]=a
        unable.append(a)
    else:
        par[a]=b

idx=1

while True:
    n,m=map(int,input().split())
    unable=[0]
    if n==m==0:
        break
    par=list(range(n+1))
    for i in range(m):
        a,b=map(int,input().split())
        union(a,b)
    for i in range(n):
        find(i+1)
    unable=[find(i) for i in unable]
    cnt=len(set(par))-len(set(unable))
    if cnt==1:
        print(f'Case {idx}: There is one tree.')
    elif cnt>1:
        print(f'Case {idx}: A forest of {cnt} trees.')
    else:
        print(f'Case {idx}: No trees.')
    idx+=1

        
