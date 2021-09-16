from sys import stdin,maxsize
from collections import defaultdict as dd
inf=maxsize
input=stdin.readline

v,e=map(int,input().split())
val=[[inf]*v for i in range(v)]
mn=inf
for i in range(e):
    a,b,c=map(int,input().split())
    val[a-1][b-1]=c
    
for i in range(v):
    for j in range(v):
        for k in range(v):
            val[j][k]=min(val[j][i]+val[i][k],val[j][k])


for i in range(v):
    for j in range(v):
        mn=min(mn,val[i][j]+val[j][i])

print(mn)
