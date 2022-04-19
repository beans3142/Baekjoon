from sys import *
setrecursionlimit(100000)
input=stdin.readline

def grouping(x):
    vi[x]=2
    group[-1].append(x)
    groupno[x]=no
    for nextnode in rgraph[x]:
        if vi[nextnode]==1:
            grouping(nextnode)
    

def getorder(x):
    global orderidx
    vi[x]=1
    for nextnode in graph[x]:
        if vi[nextnode]==0:
            getorder(nextnode)
    order[orderidx]=x
    orderidx+=1



while True:
    case=map(int,input().split())
    n=next(case)
    if n==0:
        break
    m=next(case)
    connection=map(int,input().split())

    graph=[[] for i in range(n+1)]
    rgraph=[[] for i in range(n+1)]

    orderidx=1
    groupno=[0]*(n+1)
    group=[[]]
    no=1
    order=[0]*(n+1)
    vi=[0]*(n+1)
    
    for i in range(m):
        a=next(connection)
        b=next(connection)
        graph[a].append(b)
        rgraph[b].append(a)

    for i in range(1,n+1):
        if vi[i]==0:
            getorder(i)

    for i in range(orderidx-1,0,-1):
        node=order[i]
        if vi[node]==1:
            group.append([])
            grouping(node)
            no+=1
    ans=[]
    able=[1]*(no+1)
    for i in range(1,n+1):
        if not able[groupno[i]]:
            continue
        for j in graph[i]:
            if groupno[i]!=groupno[j]:
                able[groupno[i]]=0
                break

    for i in range(1,no):
        if able[i]:
            ans+=group[i]
                
            
        
    if ans:
        print(*sorted(ans))
    else:
        print()
        
    
