from sys import stdin
input=stdin.readline

for i in range(int(input())):
    p,q=map(int,input().split())
    dp=[0,1]
    for j in range(2,p+1):
        dp.append((dp[-1]+dp[-2])%q)
    print(f'Case #{i+1}: {dp[-1]%q}')
