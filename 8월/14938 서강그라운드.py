from sys import *
input=stdin.readline
inf=maxsize

n,m,r=map(int,input().split())
item=list(map(int,input().split()))
mx=0
ground=[[inf]*n for i in range(n)]

for i in range(r):
    a,b,l=map(int,input().split())
    ground[a-1][b-1]=min(ground[a-1][b-1],l)
    ground[b-1][a-1]=min(ground[b-1][a-1],l)

for i in range(n):
    ground[i][i]=0
    for j in range(n):
        for k in range(n):
            ground[j][k]=min(ground[j][k],ground[j][i]+ground[i][k])
        
            
for i in range(n):
    mx=max(sum([item[j] for j in range(n) if ground[i][j]<=m]),mx)

print(mx)
