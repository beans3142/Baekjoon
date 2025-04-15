'''
다해보는건 2^100이니까 안된다
일단 생긴건 매우매우 DP인데
그래프로 풀려면 풀리려나?
V=200
E=V*3정도?
다익스트라 쓰면 음..
그냥 DP로 풀자
'''

# 정답 검증용 2^n 코드
'''
from random import randint

n=randint(1,15)
room=[[randint(1,100) for i in range(n)] for i in range(2)]
move=[[randint(1,100) for i in range(n-1)] for i in range(2)]

def solve():
    ans=float('inf')
    def bf(time,now,s):
        nonlocal ans
        if time==n:
            ans=min(ans,s)
            return
        other=1-now
        bf(time+1,now,s+room[now][time])
        bf(time+1,other,s+move[now][time-1]+room[other][time])
    bf(1,0,room[0][0])
    bf(1,1,room[1][0])
    return ans

print(solve())

'''

from sys import stdin
input=stdin.readline


n=int(input())
room=[list(map(int,input().split())) for i in range(2)]
move=[list(map(int,input().split())) for i in range(2)]


dp=[[0]*n for i in range(2)]
dp[0][0]=room[0][0]
dp[1][0]=room[1][0]

for time in range(1,n):
    for now in range(2):
        other=1-now
        dp[now][time]=room[now][time]+min(move[other][time-1]+dp[other][time-1],dp[now][time-1])
print(min(dp[1][-1],dp[0][-1]))

'''
TC
움직X
in
5
1 1 1 1 1
5 5 5 5 5
3 3 3 3
3 3 3 3

out
5

계속 움직
in
5
1 9 1 9 1
9 1 9 1 9
1 9 1 9
9 1 9 1

out
9

'''
