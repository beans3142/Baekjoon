from sys import stdin
input=stdin.readline


n=int(input())

fibo=[0,0,2,3]
for i in range(4,n+1):
    fibo.append((fibo[-1]+fibo[-2])%10)
print(fibo[n])
