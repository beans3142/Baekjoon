from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

board=[list(input().rstrip())for i in range(n)]

def gravity():
    for i in range(n-1,-1,-1):
        for j in range(m):
            if board[i][j]=='a':
                start=i
                while True:
                    if 0<=start+1<n:
                        if board[start+1][j]=='.':
                            board[start+1][j]=board[start][j]
                            board[start][j]='.'
                            start+=1
                        else:
                            break
                    else:
                        break

gravity()

for i in range(n):
    print(''.join(board[i]))
