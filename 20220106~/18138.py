from sys import stdin
from math import ceil
input=stdin.readline

n,m=map(int,input().split())
shirt=[]
vi=[False]*201
cara=[0]*(1500)
kara=[]
make=[[] for i in range(n+1)]
made=[0]*(201)
for i in range(n):
    shirt.append(int(input()))
for i in range(m):
    kara.append(int(input()))

for i in range(n):
    for j in range(m):
        if 2*shirt[i]<=kara[j]*4<=shirt[i]*3 or 4*shirt[i]<=4*kara[j]<=shirt[i]*5:
            make[i+1].append(j+1)

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in make[x]:
        if made[i]==0 or dfs(made[i]):
            made[i]=x
            return True
    return False

cnt=0
for i in range(1,n+1):
    for j in range(201):
        vi[j]=False
    if dfs(i):
        cnt+=1

print(cnt)
