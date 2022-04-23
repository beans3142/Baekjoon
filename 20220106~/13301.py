from sys import stdin
input=stdin.readline

fibo=[0,1,1,2]
for i in range(77):
    fibo.append(fibo[-1]+fibo[-2])

n=int(input())
print(fibo[n]*4+fibo[n-1]*2)
