from sys import stdin
input=stdin.readline

inf=float('inf')

def get_two_five(a):
    twocnt=0
    two=a
    while two%2==0 and two>1:
        two//=2
        twocnt+=1
    fivecnt=0
    five=a
    while five%5==0 and five>4:
        five//=5
        fivecnt+=1

    return [twocnt,fivecnt]

def fill(arr1,arr2,arr3):
    a2=[arr2[0]+arr1[0],arr2[1]+arr1[1]]
    a3=[arr3[0]+arr1[0],arr3[1]+arr1[1]]
    if a2<a3:
        return a2
    else:
        return a3

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
dp=[[[0,0] for i in range(n)]for i in range(n)]
# 0의 수, 2의 개수, 5의 개수, 0이 곱해졌는가

for i in range(n):
    for j in range(n):
        if arr[i][j]!=0:
            arr[i][j]=get_two_five(arr[i][j])
        else:
            arr[i][j]=[inf,inf]

dp[0][0]=arr[0][0]

for i in range(1,n):
    dp[0][i]=fill(dp[0][i-1],arr[0][i],[inf,inf])
    dp[i][0]=fill(dp[i-1][0],arr[i][0],[inf,inf])

for i in range(1,n):
    for j in range(1,n):
        for k in range(2):
            dp[i][j][k]=arr[i][j][k]+min(dp[i-1][j][k],dp[i][j-1][k])

print(min(dp[-1][-1][0],dp[-1][-1][1]))
