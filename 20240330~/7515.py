from sys import stdin
input=stdin.readline

dp=[0,2,3]

for i in range(2,41):
    dp.append(dp[-1]+dp[-2])

for i in range(int(input())):
    print(f"Scenario {i+1}:")
    print(dp[int(input())])
    print()
