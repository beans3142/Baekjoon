from sys import stdin
input=stdin.readline

def find(x):
    if par[x]==x:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b):
    c=find(a)
    d=find(b)
    if c==d:
        return
    graph[a].append(b)
    if par[c]<par[d]:
        par[b]=c
    else:
        par[a]=d

def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)

def crossed(x1,y1,x2,y2,x3,y3,x4,y4):
    first=ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)
    second=ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)
    if first==0 and second==0:
        if [x1,y1]<=[x4,y4] and [x3,y3]<=[x2,y2]:
            return True
    return False

def dfs(x):
    global ans
    vi[x]=1
    if not graph[x]:
        ans+=1
        return
    for i in graph[x]:
        if vi[i]==0:
            dfs(i)
    

n=int(input())
arr=[list(map(lambda x:int(float(x)*1000),input().split())) for i in range(n)]
arr=[min([x1,y1,x2,y2],[x2,y2,x1,y1]) for x1,y1,x2,y2 in arr]
#arr=sorted([list(map(lambda x:int(float(x)*1000),input().split())) for i in range(n)])
par=[i for i in range(n+1)]
graph=[[] for i in range(n+1)]
vi=[0]*(n+1)
ans=0

for i in range(n):
    for j in range(i+1,n):
        if crossed(*arr[i],*arr[j]):
            union(i+1,j+1)
'''
for i in range(1,n+1):
    if vi[i]==0:
        dfs(i)

'''
for i in range(1,n+1):
    if not graph[i]:
        ans+=1
        
print(ans)
#print(len(set(par))-1)
