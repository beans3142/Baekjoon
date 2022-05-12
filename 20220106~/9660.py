dp=['CY','SK','CY','SK','SK']

for i in range(2):
    if dp[-1]==dp[-3]==dp[-4]=='SK':
        dp.append('CY')
    else:
        dp.append('SK')

n=int(input())
print(dp[n%7])
