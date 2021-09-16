from sys import stdin,maxsize
input=stdin.readline
inf=maxsize
mn=inf

n,m=map(int,input().split())
city=[[inf]*n for i in range(n)]

for i in range(m):
    a,b,t=map(int,input().split())
    city[a-1][b-1]=t
    #city[b-1][a-1]=t

k=int(input())

friends=list(map(int,input().split()))

for i in range(n):
    city[i][i]=0
    for j in range(n):
        for k in range(n):
            city[j][k]=min(city[j][k],city[j][i]+city[i][k])

ans=[]

for i in range(n):
    T=0
    for j in friends:
        T=max(city[j-1][i]+city[i][j-1],T)
    if T<mn:
        mn=T
        ans=[i+1]
    elif T==mn:
        ans.append(i+1)

print(*ans)
