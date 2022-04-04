from sys import stdin,maxsize
input=stdin.readline
inf=maxsize

n,m=map(int,input().split())

small=[[inf]*n for i in range(n)]
tall=[[inf]*n for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    small[a-1][b-1]=1
    tall[b-1][a-1]=1

for i in range(n):
    tall[i][i]=1
    small[i][i]=1
    for j in range(n):
        for k in range(n):
            tall[j][k]=min(tall[j][k],tall[j][i]*tall[i][k])
            small[j][k]=min(small[j][k],small[j][i]*small[i][k])

ans=[]

for i in range(n):
    mn=tall[i].count(1)
    mx=n+1-small[i].count(1)
    if mn>mx:
        print(-1)
        exit()
    ans.append([mn,mx])

for i in ans:
    print(*i)
