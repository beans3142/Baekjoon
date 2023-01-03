from sys import stdin
input=stdin.readline

def find(x):
    if x==par[x]:
        return x
    par[x]=find(par[x])
    return par[x]

def union(a,b):
    a=find(a)
    b=find(b)

    if a<b:
        par[b]=a
    elif a==b:
        return False
    else:
        par[a]=b
    return True

def check():
    graph=False
    for i in range(m):
        a,b=map(int,input().split())
        if not union(a,b):
            graph=True

    for i in range(1,n+1):
        find(i)
    
    if len(set(par))!=1:
        graph=True
        
    return graph

for i in range(int(input())):
    n=int(input())
    m=int(input())
    par=[i for i in range(n+1)]
    par[0]=1
    if check():
        print('graph')
    else:
        print('tree')
        
