import sys
import math
input = sys.stdin.readline
#sys.stdin=open("input.txt", "rt")

INF = int(1e9)
n,m=map(int,input().split())
# 최단 경로를 체크한 리스트 생성
board = [[INF]*n for _ in range(n)]
# 경유지를 체크할 리스트 생성
stopover = [[0]*n for _ in range(n)]

# 기본 입력 사항 체크
for _ in range(m):
    a,b,c = map(int,input().split())
    board[a-1][b-1]=c
    board[b-1][a-1]=c
    stopover[a-1][b-1]=b
    stopover[b-1][a-1]=a

for a in range(n):
    for b in range(n):
        if a==b:
            board[a][b]=0
            stopover[a][b]=-1

# 플루이드 워셜로 모든 경우의수 체크하기
for k in range(n):
    for a in range(n):
        for b in range(n):
            if board[a][b] > board[a][k]+board[k][b]:
                board[a][b] = board[a][k]+board[k][b]
                stopover[a][b] = stopover[a][k] # 길이가 갱신될때 맨 처음 stopover[a][k]를 이어간다.

# 출력하기
for a in range(n):
    for b in range(n):
        if a==b :
            print("-",end=' ')
        else:
            print(stopover[a][b], end=' ')
    print()
