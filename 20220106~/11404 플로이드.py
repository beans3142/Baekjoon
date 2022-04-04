from sys import stdin,maxsize
input=stdin.readline

n=int(input())
m=int(input())

value_table=[[[maxsize,[_+1]] for i in range(n)]for _ in range(n)]

for bus in range(m):
    a,b,c=map(int,input().split())
    value_table[a-1][b-1][0]=min(value_table[a-1][b-1][0],c)


for i in range(n):
    value_table[i][i][0]=0
    for j in range(n):
        for k in range(n):
            cmp=value_table[j][i][0]+value_table[i][k][0]
            if cmp < value_table[j][k][0]:
                value_table[j][k][0]=cmp
                value_table[j][k][1]=value_table[j][i][1]+value_table[i][k][1]

for i in range(n):
    for j in range(n):
        if value_table[i][j][0]==maxsize:
            value_table[i][j][0]=0
        print(value_table[i][j][0],end=' ')
    print()

for i in range(n):
    for j in range(n):
        if value_table[i][j][0]==0:
            print(0)
        else:
            print(len(value_table[i][j][1])+1,*value_table[i][j][1],j+1)
