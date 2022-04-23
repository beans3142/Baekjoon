from sys import stdin
input=stdin.readline

fibo=[0,1]
for i in range(1000001):
    fibo.append((fibo[-1]+fibo[-2])%(10**9+7))

n=int(input())
print(fibo[n])
