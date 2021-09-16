import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
nl={i for i in range(1,n+1)}
min_dif=100000000
can_team=[]
matrix=[list(map(int,input().split())) for i in range(n)]

def bt(idx,arr):
    global min_dif
    queue=deque([[idx,arr]])
    while queue:
        i,l=queue.popleft()
        if i == n//2+1:
            if 1 not in l:
                break
            l=set(l)
            team=0
            for p in l:
                for j in l:
                    team+=matrix[p-1][j-1]
            for p in nl-l:
                for j in nl-l:
                    team-=matrix[p-1][j-1]
            min_dif=min(min_dif,abs(team))
                    
            
        else:
            for _ in range(max(l),n+1):
                if _ not in l:
                    queue.append([i+1,l+[_]])

bt(2,[1])

print(min_dif)
