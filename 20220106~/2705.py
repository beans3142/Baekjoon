from sys import stdin
input=stdin.readline

dp=[0,1,2,2,4]

for i in range(5,1000+1):
    recur=1
    idx=1
    while idx<=i//2:
        recur+=dp[idx]
        idx+=1
    dp.append(recur)


for i in range(int(input())):
    print(dp[int(input())])
