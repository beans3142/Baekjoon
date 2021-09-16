from sys import stdin
input=stdin.readline
n=int(input())

matrix=[list(map(int,input().split())) for i in range(n)]
table={}
for i in range(n):
    for j in range(n):
        table[i,j]=1
total=0
unable=False

for i in range(n):
    table[i,i]=0
    for j in range(n):
        for k in range(n):
            if j==i or i==k or j==k: continue;
            if matrix[j][k]==matrix[j][i]+matrix[i][k]:
                #table[j,i]=table[i,k]=0
                table[j,k]=0
            if matrix[j][k]>matrix[j][i]+matrix[i][k]:
                unable=True

for i in table:
    if table[i]==1:
        total+=matrix[i[0]][i[1]]

if unable:
    print(-1)
else:
    print(total//2)
