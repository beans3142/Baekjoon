from sys import stdin
from collections import deque
input=stdin.readline

n,m=map(int,input().split())
#arr=[[False,False]for i in range(n+1)]
jul=[]
v=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    if a+b==0:
        print(0)
        exit()
    jul.append((a,b))

def dfs(vi):
    print(vi)
    sat(vi)
    for i in range(1,n+1):
        if vi[i]==0:
            vi[i]=1
            dfs(vi)
            vi[i]=0
    

def sat(to_check):
    for xi,xj in jul:
        jul1=to_check[xi] if xi>0 else not to_check[-1*xi]
        jul2=to_check[xj] if xj>0 else not to_check[-1*xj]
        #print(jul1,jul2,xi,xj)
        if (jul1 or jul2)==0:
            return 0
        '''
    print(1)
    for i in range(1,n+1):
        print(to_check[i],end=' ')
    #exit()
    '''

dfs([0 for i in range(n+1)])
print(0)
