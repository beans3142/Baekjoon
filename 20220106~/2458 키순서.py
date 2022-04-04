from sys import stdin
input=stdin.readline

n,m=map(int,input().split())
cnt=0
inf=10**9 
heavy=[[inf for i in range(n)] for _ in range(n)]
light=[[inf for i in range(n)] for _ in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    heavy[a-1][b-1]=1
    light[b-1][a-1]=1

def floid(arr):
    for i in range(n):
        arr[i][i]=0
        for j in range(n):
            for k in range(n):
                arr[j][k]=min(arr[j][k],arr[j][i]+arr[i][k])
    return arr

heavy=floid(heavy)
light=floid(light)

mid=(n+1)//2
cnt=0
for i in range(n):
    able=True
    for j in range(n):
        if heavy[i][j]&light[i][j]==inf:
            able=False
            break
    if able:
        cnt+=1

print(cnt)
