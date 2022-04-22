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
    
    
while True:
    try:
        n,m=map(int,input().split())
        graph=[[] for i in range(2*n+1)]

        for i in range(m):
            a,b=map(int,input().split())
            graph[-a].append(b)
            graph[-b].append(a)

        graph[-1].append(1)


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
                break

        if ans==1:
            print("yes")
        else:
            print("no")
    except:
        break
