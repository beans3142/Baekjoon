from sys import stdin
input=stdin.readline

# n = 행의 수, m = 열의 수
# n,m = 5~100
# 플레이어가 클릭한 지점 x,y x는 n y는 m
# 클릭한 지점의 근처 8방향의 지뢰 수 출력
# 클릭한 곳이 지뢰가 있다면 game over 출력

n,m=map(int,input().split())
x,y=map(int,input().split())
# 행과 열의 번호 1부터 시작
# 맞춰주기 위해 -1
x-=1
y-=1

dx=[0,0,1,-1,1,1,-1,-1]
dy=[1,-1,0,0,1,-1,1,-1]

matrix=[[*map(int,input().split())] for i in range(n)]

if matrix[x][y]==1:
    print("game over")
else:
    minenear=0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if -1<nx<n and -1<ny<m:
            if matrix[nx][ny]==1:
                minenear+=1
    print(minenear)

'''
TC

x,y 거꾸로 입력했을 경우

in

3 3
2 1
1 0 1
1 1 1
0 0 0

out

game over

wrong out

5

'''
