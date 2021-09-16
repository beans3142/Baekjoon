import sys
input=sys.stdin.readline

n,m,h=map(int,input().split())

matrix=[input().rstrip().split() for i in range(n)]
mintchoco=[]
max_eat=0

for i in range(n):
    for j in range(n):
        if matrix[i][j]=='0':
            continue
        elif matrix[i][j]=='2':
            mintchoco.append((j,i))
        else:
            home_x,home_y=j,i

def dfs(now_x,now_y,hp,cnt):
    global max_eat
    for x,y in mintchoco:
        if matrix[y][x]=='2':
            length=abs(now_x-x)+abs(now_y-y)
            if length>hp:
                continue
            matrix[y][x]='0'
            dfs(x,y,hp-length+h,cnt+1)
            matrix[y][x]='2'
    from_home=abs(home_x-now_x)+abs(home_y-now_y)

    if from_home>hp:
        return
    max_eat=max(max_eat,cnt)

dfs(home_x,home_y,m,0)

print(max_eat)
