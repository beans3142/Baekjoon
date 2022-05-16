from sys import stdin,setrecursionlimit
setrecursionlimit(100000)
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in able[x]:
        if rev[i]==-1 or dfs(rev[i]):
            rev[i]=x
            return True
    return False
        

dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]

n,m=map(int,input().split())

unable=set()

for i in range(m):
    a,b=map(int,input().split())
    unable.add((b-1,a-1))

able=[[] for i in range(n**2)]

for i in range(n):
    for j in range(n):
        if (i-j)%2 and (j,i) not in unable:
            for k in range(8):
                ni=i+dx[k]
                nj=j+dy[k]
                if -1<ni<n and -1<nj<n:
                    if (nj,ni) not in unable:
                        able[i*n+j].append(ni*n+nj)
                    
rev=[-1]*(n**2)
ans=n**2
cnt=0
for i in range(n**2):
    if able[i]:
        vi=[False]*(n**2)
        if dfs(i):
            ans-=1

print(ans-m)
