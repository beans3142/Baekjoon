from sys import *
input=stdin.readline
inf=maxsize

n,m=map(int,input().split())
val=[[inf]*n for i in range(n)]

for i in range(m):
    _From,_To,Pass=map(int,input().split())
    val[_From-1][_To-1]=0
    val[_To-1][_From-1]=1 if Pass == 0 else 0

for i in range(n):
    val[i][i]=0
    for j in range(n):
        for k in range(n):
            val[j][k]=min(val[j][k],val[j][i]+val[i][k])
k=int(input())

for i in range(k):
    start,end=map(int,input().split())
    print(val[start-1][end-1])
