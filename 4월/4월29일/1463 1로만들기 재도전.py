#https://www.acmicpc.net/problem/1463

n=int(input())

dp=[0,0,1,1]

for i in range(4,n+1): # 기존에 만들어논 dp배열의 길이 이상에서 시작n에 도달까지
    dp.append(dp[i-1]+1) # dp에 dp[i-1]+1을 추가 dp[i-1]은 이전까지의 수행 횟수
                        #dp[i]는 각 숫자의 수행횟수를 나타내줌
                        #dp[i] 위치에 계속 값을 추가해줌
    print(dp,dp[i],i) 
    if i%2==0: # 만약 i%2==0이라면
        print(dp[i//2]+1,dp[i],2)
        dp[i]=min(dp[i//2]+1,dp[i]) #dp[i//2]=i가 절반이었을때 수행횟수에서
                                    #*2연산을 한 것이므로 +1을 더해줌
                                    #근데 이것이 dp[i]의 연산횟수보다 크면
                                    #dp[i]를 그대로 냅둠
    if i%3==0:
        print(dp[i//3]+1,dp[i],3)
        dp[i]=min(dp[i//3]+1,dp[i])

print(dp[n])
