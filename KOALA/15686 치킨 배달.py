from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

arr=[list(map(int,input().split())) for i in range(n)]
homelist=[]
chicklist=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            continue
        if arr[i][j]==1:
            homelist.append((j,i))
        else:
            chicklist.append((j,i))

vi=[0]*len(chicklist)

def dfs(l,idx):
    global able
    if len(l)==m:
        able.append(l)
        return
    for i in range(idx,len(chicklist)):
        if vi[idx]==0:
            vi[idx]=1
            dfs(l+[chicklist[i]],i+1)
            vi[idx]=0

able=[]
dfs([],0)
mn=10**10

for i in able:
    val=[100000000000]*len(homelist)
    for j,loc in enumerate(homelist):
        for x,y in i:
            val[j]=min(val[j],abs(loc[1]-y)+abs(loc[0]-x))
    mn=min(mn,sum(val))

print(mn)
            
        
