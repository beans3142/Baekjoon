from sys import stdin
input=stdin.readline

n=int(input())
check=[False]*(n+1)
check2=[False]*(n+1)
time=[0]*(n+1)
nowtime=1
order=[0]*(n+1)
idx=1
graph=[[] for i in range(n+1)]
rev=[[] for i in range(n+1)]
ans=[]
dp=[0]*(n+1)
mx=0

def div(num):
    s=0
    while num:
        s+=num%10
        num//=10
    return s

def gettime(x):
    global nowtime,idx,depth
    check[x]=True
    for i in graph[x]:
        if check[i]==False:
            gettime(i)
    time[x]=nowtime
    order[idx]=x
    nowtime+=1
    idx+=1
    depth+=1

def scc(x):
    global ans
    check2[x]=True
    for i in rev[x]:
        if check2[i]==False:
            scc(i)
    ans[-1].append(x)
    ans[-1][0]+=1

def dfs(x,depth):
    global cnt
    cnt=max(cnt,depth)
    check3[x]=1
    for i in rev[x]:
        if check3[i]==False:
            dfs(i,depth+1)


for i in range(1,n+1):
    add=div(i)
    nextnode=(i+add)%n
    nextnode=n if nextnode==0 else nextnode
    graph[i].append(nextnode)
    rev[nextnode].append(i)

for i in range(1,n+1):
    if check[i]==False:
        depth=0
        gettime(i)
        mx=max(depth,mx)
        

for i in range(n,0,-1):
    now=order[i]
    if check2[now]==False:
        ans.append([0])
        scc(now)

check3=[0]*(n+1)

for i in sorted(ans,reverse=True):
    tosearch=[]
    for j in range(1,len(i)):
        check3[i[j]]=1
        for k in rev[i[j]]:
            tosearch.append(k)
    mx=max(mx,i[0])
    for j in tosearch:
        if check3[j]==0:
            cnt=0
            dfs(j,0)
            mx=max(mx,i[0]+cnt+1)

print(mx)
