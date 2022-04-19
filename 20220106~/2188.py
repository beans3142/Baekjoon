from sys import stdin
input=stdin.readline

def dfs(x):
    if vi[x]:
        return False
    vi[x]=True
    for i in want[x]:
        if place[i]==0 or dfs(place[i]):
            place[i]=x      
            return True
    return False
n,m=map(int,input().split())

want=[[] for i in range(201)]
vi=[False]*(201)
place=[0]*(201)

for i in range(1,n+1):
    info=map(int,input().split())
    for j in range(next(info)):
        want[i].append(next(info))

cnt=0
for i in range(1,n+1):
    for j in range(m+1):
        vi[j]=False
    if dfs(i):
        cnt+=1

print(cnt)
