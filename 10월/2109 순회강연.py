from sys import stdin
input=stdin.readline
n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((b,a))

arr.sort()
arr+=[(10001,10001)]
ans=0

for i in range(n):
    if arr[i][0]<arr[i+1][0]:
        ans+=arr[i][1] 

print(ans)

# 나중에 다 시 풀 예정
