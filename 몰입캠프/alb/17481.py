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


n,m=map(int,input().split())
graph=[[] for i in range(n)]
stoi={}
for i in range(m):
    name=input().rstrip()
    stoi[name]=i

for i in range(n):
    c,*names=input().rstrip().split()
    for name in names:
        graph[i].append(stoi[name])

rev=[-1]*(m)

cnt=0

for i in range(n):
    vi=[False]*(n+1)
    cnt+=dfs(i)

if n==cnt:
    print("YES")
else:
    print(f"NO\n{cnt}")
