from sys import stdin
input=stdin.readline

fibo=[0,1]
n=int(input())
for i in range(2,n+1):
    fibo.append(fibo[i-1]+fibo[i-2])

print(fibo[n])
