from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

matrix=[[0]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    line=list(map(int,input().split()))
    for j in range(n):
        matrix[i][j+1]=matrix[i][j]+line[j]

for i in range(m):
    x1,y1,x2,y2=map(int,input().split())
    s=0
    for j in range(x1,x2+1):
        s+=matrix[j][y2]-matrix[j][y1-1]
    print(s)
