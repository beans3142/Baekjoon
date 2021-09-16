# 

from sys import stdin
input=stdin.readline

n=int(input())
arr=list(map(int,input().split()))
dp=[0]+[1000 for i in range(n-1)] # 1번째는 무조건 0

for idx,i in enumerate(arr): # arr의 길이만큼 반복,
    for j in range(i):
        if idx+j+1<n:
            dp[idx+j+1]=min(dp[idx]+1,dp[idx+j+1])
            # dp안에 저장되어있는 현위치로부터 j+1칸 떨어져있는 곳의 값과
            # dp안에 저장되어있는 현위치+1한 값중 작은 값을
            # dp [현위치로부터 j+1칸 떨어져있는 값]에 저장

print(dp[-1] if dp[-1]!=1000 else -1)
# 만약 dp의 맨 끝의 값이 1000이 아니면 그 값 출력, 1000이면 -1 출력
