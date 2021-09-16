from sys import stdin,maxsize
input=stdin.readline
inf = maxsize

n=int(input())
m=int(input())
val=[[inf]*n for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    val[b-1][a-1]=1

for i in range(n):
    val[i][i]=0
    for j in range(n):
        for k in range(n):
            val[j][k]=min(val[j][k],val[j][i]+val[i][k])

ans=[]
for i in range(n):
    cnt=0
    for j in range(n):
        if val[i][j]==val[j][i]==inf:
            cnt+=1
    ans.append(cnt)

for i in ans:
    print(i)
