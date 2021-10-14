from sys import stdin
input=stdin.readline

n,m=map(int,input().split())

arr=[input().rstrip() for i in range(n)]
dp=[[[0]*m for i in range(n)] for i in range(4)]
# [ 위 우 하 좌 ]
for i in range(n):
    for j in range(m):
        if arr[i][j]=='1':
            for idx in range(4):
                dp[idx][i][j]=1
        else:
            continue
        for ii in range(i-1,-1,-1):
            if arr[ii][j]=='0':
                break
            dp[0][i][j]+=1
        for jj in range(j+1,m):
            if arr[i][jj]=='0':
                break
            dp[1][i][j]+=1
        for ii in range(i+1,n):
            if arr[ii][j]=='0':
                break
            dp[2][i][j]+=1
        for jj in range(j-1,-1,-1):
            if arr[i][jj]=='0':
                break
            dp[3][i][j]+=1
        

ans=0

for i in range(n):
    for j in range(m):
        if arr[i][j]=='1':
            for d in range(0,min(dp[2][i][j],dp[3][i][j])+1):
                try:
                    if d>=dp[0][i+d][j+d] and d>=dp[1][i+d][j+d]:
                        ans=(d+1)**2
                except:
                    pass

print(ans)

# 다채ㅝ야아 하는 정사각형이였음 ㅋㅋㅋ;; 아 테두리만인줄 ㅋ
