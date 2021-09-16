import sys
input=sys.stdin.readline

def bfs(x,y):

n=int(input())
visited_x=[[False for i in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        
