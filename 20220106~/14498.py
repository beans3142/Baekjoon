from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in graph[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
    return False

def conflict(i,j):
    return wantbuy[i][0]==wantbuy[j][0] or wantbuy[i][1]==wantbuy[j][1]

n,m,k=map(int,input().split())

wantbuy=[[0,0] for i in range(k+1)]
nobuy=[0]*(k+1)

for i in range(k):
    ni,mi,ki=map(int,input().split())
    wantbuy[i][0]=ni
    wantbuy[i][1]=mi
    nobuy[i]=ki

graph=[[] for i in range(k+1)]

for i in range(k):
    for j in range(i+1,k):
        if conflict(i,j) and nobuy[i]!=nobuy[j]:
            if nobuy[i]:
                graph[i].append(j)
            else:
                graph[j].append(i)

rev=[-1]*(k+1)
cnt=0

for i in range(k):
    vi=[False]*(k+1)
    cnt+=dfs(i)

print(cnt)
