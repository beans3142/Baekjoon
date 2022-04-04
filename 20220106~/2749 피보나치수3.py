#https://www.acmicpc.net/problem/2749

m=10**6
cycle=15*10**5 #(m=10**k일때 cycle은 15*10**(k-1))
n=int(input())%cycle

memo=[0,1]+[0]*n

for i in range(2,n+1):
    memo[i]=(memo[i-1]+memo[i-2])%m

print(memo[n])

# 피사노 주기 활용 문제
# 참고한 것 https://sexycoder.tistory.com/62
