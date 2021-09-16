from sys import stdin,maxsize
input=stdin.readline
inf = maxsize

n,m=map(int,input().split())
val=[[inf]*n for i in range(n)]

for i in range(m):
    a,b,c=map(int,input().split())
    val[a-1][b-1]=c
    val[b-1][a-1]=c

for i in range(n):
    val[i][i]=0
    for j in range(n):
        for k in range(n):
            val[j][k]=min(val[j][k],val[j][i]+val[i][k])

mn=inf
ans=0
for i in range(n):
    s_val=sum(val[i])
    if s_val<mn:
        mn=s_val
        ans=i+1

print(ans)
