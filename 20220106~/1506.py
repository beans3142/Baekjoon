from sys import stdin
input=stdin.readline

n=int(input())
cost=list(map(int,input().split()))
check=[False]*(n+1)
check2=[False]*(n+1)
time=[0]*(n+1)
nowtime=1
order=[0]*(n+1)
idx=1
graph=[[] for i in range(n+1)]
rev=[[] for i in range(n+1)]
ans=[]

for i in range(n):
    l=input().rstrip()
    for j in range(n):
        if l[j]=='1':
            graph[i+1].append(j+1)
            rev[j+1].append(i+1)

def gettime(x):
    global nowtime,idx
    check[x]=True
    for i in graph[x]:
        if check[i]==False:
            gettime(i)
    time[x]=nowtime
    order[idx]=x
    nowtime+=1
    idx+=1

def scc(x):
    check2[x]=True
    for i in rev[x]:
        if check2[i]==False:
            scc(i)
    ans[-1].append(x)

for i in range(1,n+1):
    if check[i]==0:
        gettime(i)

for i in range(n,0,-1):
    now=order[i]
    if check2[now]==False:
        ans.append([])
        scc(now)

totalcost=0
for i in ans:
    mn=10**9
    for j in i:
        mn=min(mn,cost[j-1])
    totalcost+=mn

print(totalcost)
