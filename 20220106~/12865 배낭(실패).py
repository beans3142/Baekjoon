#https://www.acmicpc.net/problem/12865

n,k=map(int,input().split())

item=[[0,0]]

for i in range(0,n):
    item.append(list(map(int,input().split())))

dp=[[0]*(k+1) for i in range(n+1)]
#dp [[0,0]...]의 배열을 갖고 [i,j]
for i in range(1,n+1): #무게가 i일때 
    print(dp)
    for j in range(1,k+1): #j 가
        #print(dp)
        if j>=item[i][0]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-item[i][0]]+item[i][1])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[n][k])

'''
dp [i][j] = max(dp[i - 1][j], dp[i - 1][j - weight [i]] + value [i]]

dp [i - 1][j]: i번째 아이템을 챙기지 않았을 때의 최댓값
(새로운 아이템을 주울수 없을때 함수를 진행시킬때 사용)

dp [i - 1][j - weight [i]] + value [i]]: i번째 아이템을 챙겼을 때 갖는 최댓값


'''
