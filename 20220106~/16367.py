from sys import *
setrecursionlimit(100000)
input=stdin.readline

def innode(a,b):
    rgraph[a].append(-b)
    rgraph[b].append(-a)
    graph[-a].append(b)
    graph[-b].append(a)

def grouping(node):
    if check2[node]:
        return
    check2[node]=1
    group[node]=group_cnt
    for nextnode in rgraph[node]:
        if check2[nextnode]==0:
            grouping(nextnode)

def gettime(node):
    global nowtime,orderidx
    check[node]=1
    for nextnode in graph[node]:
        if check[nextnode]==0:
            gettime(nextnode)

    stack.append(node)
    
    

n,m=map(int,input().split())
graph=[[] for i in range(2*n+1)]
rgraph=[[] for i in range(2*n+1)]

for _ in range(m):
    arr=list(input().rstrip().split())
    ch=[]
    for i in range(len(arr)//2):
        v=int(arr[i*2])
        if arr[i*2+1]=='R':
            v*=-1
        ch.append(v)
    a,b,c=ch
    
    innode(a,b)
    innode(b,c)
    innode(c,a)



time=[0]*(2*n+1)
order=[0]*(2*n+1)
orderidx=1
nowtime=1
group_cnt=1
check=[0]*(2*n+1)
check2=[0]*(2*n+1)
group=[0]*(2*n+1)
stack=[]

for idx in range(-n,n+1):
    if idx==0:
        continue
    if check[idx]==0:
        gettime(idx)

while stack:
    now=stack.pop()
    if not check2[now]:
        group_cnt+=1
        grouping(now)


ansarr=[0]*n
ans=1
for i in range(1,n+1):
    if group[i]==group[-i]:
        ans=0
    if group[i]<group[-i]:
        ansarr[i-1]=1

if ans==1:
    print(*['R' if i%2 else 'B' for i in ansarr],sep='')
else:
    print(-1)
