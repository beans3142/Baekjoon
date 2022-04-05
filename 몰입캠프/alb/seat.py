from sys import stdin
input=stdin.readline

# 달팽이 문제와 비슷한 문제.

# 해당 순서로 이동하면 상 우 하 좌 이순서로 이동
dx=[0,1,0,-1]
dy=[-1,0,1,0]

r,c=map(int,input().split())
k=int(input())

arr=[[0 for i in range(r)] for i in range(c)]
x,y=0,c-1
now=1
d=0 # 방향
if k>r*c:
    print(0)
else:
    while True:
        arr[y][x]=now
        if now==k:
            break
        nx=x+dx[d]
        ny=y+dy[d]
        if -1<ny<c and -1<nx<r and arr[ny][nx]==0 :
            x=nx
            y=ny
            now+=1
        else:
            d=(d+1)%4

    print(x+1,c-y)

'''
TC

r*c보다 k가 큰 경우
in
3 3
10

out
0

맨 처음 시작을 잘못 짠 경우
in
5 5
1

out
1 1

기타 회전
in
5 5
6

out
2 5

in
5 5
11

out
5 3

in
5 5
17

out
2 2
'''
