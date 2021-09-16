from sys import stdin,maxsize
inf=maxsize
input=stdin.readline

n=int(input())
rel=[[inf]*n for i in range(n)]
person=sorted([list(map(int,input().split()))+[i] for i in range(n)])
for i in range(n):
    for j in range(i+1,n):  
        if person[i][0]<=person[j][0]<=person[i][1]:
            rel[person[i][2]][person[j][2]]=1
            rel[person[j][2]][person[i][2]]=1

for i in range(n):
    rel[i][i]=1
    for j in range(n):
        for k in range(n):
            rel[j][k]=min(rel[j][k],rel[j][i]+rel[i][k])

m=int(input())

for i in range(m):
    a,b=map(int,input().split())
    print(rel[a-1][b-1] if rel[a-1][b-1] != inf else -1)
            
