from sys import *
setrecursionlimit(100000)
input=stdin.readline

def grouping(node):
    check2[node]=1
    group[node]=group_cnt
    for nextnode in graph[node]:
        if check2[nextnode]==0:
            grouping(nextnode)

def gettime(node):
    global nowtime,orderidx
    check[node]=1
    for nextnode in graph[node]:
        if check[nextnode]==0:
            gettime(nextnode)

    time[node]=nowtime
    order[orderidx]=node
    nowtime+=1
    orderidx+=1

case=map(int,stdin.read().split())
    
while True:
    #case=map(int,input().split())
    try:
        n=next(case)
    except:
        break
    m=next(case)
    graph=[[] for i in range(2*n+1)]

    for i in range(m):
        a=next(case)
        b=next(case)
        graph[-a].append(b)
        graph[-b].append(a)

    time=[0]*(2*n+1)
    order=[0]*(2*n+1)
    orderidx=1
    nowtime=1
    group_cnt=1
    check=[0]*(2*n+1)
    check2=[0]*(2*n+1)
    group=[0]*(2*n+1)

    for idx in range(-n,n+1):
        if idx==0:
            continue
        if check[idx]==0:
            gettime(idx)
                
    for idx in range(orderidx-1,0,-1):#,0,-1):
        node=order[idx]
        if check2[-node]==0:
            grouping(-node)
            group_cnt+=1


    ans=1
    for i in range(1,n+1):
        if group[i]==group[-i]:
            ans=0

    print(ans)
