from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
q=int(input())
presum=[[[0,0,0] for i in range(m+1)] for j in range(n+1)]
arr=[input().rstrip() for i in range(n)]
c={"J":0,"O":1,"I":2}

presum[1][1][c[arr[0][0]]]+=1

for i in range(2,n+1):
    for j in range(3):
        presum[i][1][j]+=presum[i-1][1][j]+presum[i][0][j]-presum[i-1][0][j]
    presum[i][1][c[arr[i-1][0]]]+=1

for i in range(2,m+1):
    for j in range(3):
        presum[1][i][j]+=presum[1][i-1][j]+presum[0][i][j]-presum[0][i-1][j]
    presum[1][i][c[arr[0][i-1]]]+=1

for i in range(2,n+1):
    for j in range(2,m+1):
        presum[i][j][c[arr[i-1][j-1]]]+=1
        for k in range(3):
            presum[i][j][k]+=presum[i-1][j][k]+presum[i][j-1][k]-presum[i-1][j-1][k]

for i in range(q):
    a,b,c,d=map(int,input().split())
    for k in range(3):
        rightdown=presum[c][d][k]
        leftdown=presum[c][b-1][k]
        rightup=presum[a-1][d][k]
        leftup=presum[a-1][b-1][k]
        print(rightdown-leftdown-rightup+leftup,end=' ')
    print()
        
