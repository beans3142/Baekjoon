from sys import stdin
from bisect import bisect_left
input=stdin.readline

n=int(input())
narr=list(map(int,input().split()))
m=int(input())
marr=list(map(int,input().split()))
ans=[]
while True:
    add=False
    for i in range(100,0,-1):
        if i in narr and i in marr:
            ans.append(i)
            narr=narr[narr.index(i)+1:]
            marr=marr[marr.index(i)+1:]
            add=True
            break
    if not add:
        break
    
print(len(ans))
print(*ans)