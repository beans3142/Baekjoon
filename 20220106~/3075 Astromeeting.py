from sys import stdin
from math import inf
input=stdin.readline

for _ in range(int(input())):
    n,p,q=map(int,input().split())
    people=[]
    for i in range(n):
        people.append(int(input()))
    galaxy=[[inf for i in range(p)]for i in range(p)]
    for i in range(q):
        a,b,c=map(int,input().split())
        galaxy[a-1][b-1]=galaxy[b-1][a-1]=min(galaxy[a-1][b-1],c)
    for i in range(p):
        galaxy[i][i]=0
        for j in range(p):
            for k in range(p):
                galaxy[j][k]=min(galaxy[j][k],galaxy[j][i]+galaxy[i][k])

    mn=inf
    loc=0
    for i in range(p):
        now_value=0
        for person in people:
            now_value+=galaxy[person-1][i]**2
        if now_value<mn:
            loc=i+1
            mn=now_value

    print(loc,mn)
