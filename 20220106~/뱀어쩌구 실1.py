import sys
from collections import deque
input=sys.stdin.readline
radder,snake=map(int,input().split())
board=[-1]*101
move={}
for i in range(radder+snake):
	x,y=map(int,input().split())
	move[x]=y


queue=deque([[1,0]])
while queue:
    loc,roll=queue.popleft()
    if board[loc]==-1:
        board[loc]=roll
        for i in range(1,7):
            if loc+i>100:
                break
            else:
                if loc+i in move:
                    queue.append([move[loc+i],roll+1])
                else:
                    queue.append([loc+i,roll+1])


print(board[100])
