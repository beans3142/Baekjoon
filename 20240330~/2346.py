from sys import stdin
from collections import deque
input=stdin.readline

n=int(input())
bol=deque()
for idx,val in enumerate(map(int,input().split())):
    bol.append([val,idx+1])
front=bol.popleft()
ans=[front[1]]
while bol:
    if front[0]>0:
        for i in range(front[0]):
            bol.append(bol.popleft())
        front=bol.pop()
    else:
        for i in range(abs(front[0])):
            bol.appendleft(bol.pop())
        front=bol.popleft()
    ans.append(front[1])
print(*ans)
