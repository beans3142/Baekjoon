from sys import stdin
input=stdin.readline

dp=[1,1,3]
for i in range(3,251):
    dp.append(dp[-1]+2*dp[-2])

while True:
    try:
        n=int(input())
        print(dp[n])
    except:
        break
