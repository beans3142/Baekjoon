from sys import stdin
from math import inf
from collections import defaultdict
input=stdin.readline

for t in range(int(input())):
    n,m,w=map(int,input().split())
    matrix=[[inf for i in range(n)]for ii in range(n)]
    vi=defaultdict(int)
    for i in range(m):
        a,b,c=map(int,input().split())
        c=min(matrix[a-1][b-1],c)
        matrix[a-1][b-1]=matrix[b-1][a-1]=c
    for i in range(w):
        a,b,c=map(int,input().split())
        vi[a,b]=max(vi[a,b],c)

    for val in vi:
        a,b=val
        c=vi[val]
        if matrix[a-1][b-1] != inf:
            matrix[a-1][b-1]=matrix[a-1][b-1]-c
        else:
            matrix[a-1][b-1]=-c
    for i in range(n):
        matrix[i][i]=min(0,matrix[i][i])
        for j in range(n):
            for k in range(n):
                matrix[j][k]=min(matrix[j][k],matrix[j][i]+matrix[i][k])
    able=False
    for i in range(n):
        if matrix[i][i]<0:
            able=True
    if able:
        print('YES')
    else:
        print('NO')
            
        
