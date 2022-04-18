from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in myNotebook[x]:
        if owner[i]==0 or dfs(owner[i]):
            owner[i]=x
            return True

n,m=map(int,input().split())
myNotebook=[[] for i in range(n+1)]
vi=[0]*(101)
owner=[0]*(101)
for i in range(m):
    a,b=map(int,input().split())
    myNotebook[a].append(b)

cnt=0
for i in range(1,n+1):
    for j in range(101):
        vi[j]=False
    if dfs(i):
        cnt+=1

print(cnt)
