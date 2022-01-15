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
    else:
        par[a]=b

n=int(input())
par=list(range(n+1))
m=int(input())
for i in range(n):
    connection=list(map(int,input().split()))
    for j in range(n):
        if i==j:
            continue
        if connection[j]==1:
            union(i+1,j+1)

plan=list(map(int,input().split()))
able=True
for i in range(m-1):
    if find(plan[i])==find(plan[i+1]):
        continue
    able=False
    break

if able:
    print('YES')
else:
    print('NO')
    
