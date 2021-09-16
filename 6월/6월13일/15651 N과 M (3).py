
#https://www.acmicpc.net/problem/15651
import sys
from collections import deque

input=sys.stdin.readline

a,l=map(int,input().split())

def bt(idx,ls):
    queue=deque([[idx,ls]])
    while queue:
        depth,arr=queue.popleft()
        if depth==l:
            print(' '.join(arr))
        else:
            for i in range(1,a+1):
                queue.append([depth+1,arr+[str(i)]])

bt(0,[])

#뭐지 미친새낀가 ㅋㅋㅋㅋㅋ
'''
n,m=input().split()
n=int(n);m=int(m)

for i in range(0,n**m):
    for j in range(1,m+1):
        print(i//(n**(m-j))%n+1,end=' ' if j!=m else '\n')
'''
