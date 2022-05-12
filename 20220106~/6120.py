from sys import stdin
input=stdin.readline


def chn(x):
    arr=set()
    while x:
        if x%10!=0:
            arr.add(x%10)
        x//=10
    return max(arr),min(arr)

dp=[0]*1000001
for i in range(1,10):
    dp[i]=1

for i in range(10,1000001):
    
    for j in chn(i):
        if dp[i-j]!=1:
            dp[i]=1
            break

for i in range(int(input())):
    n=int(input())
    if dp[n]:
        print('YES')
    else:
        print('NO')
        
