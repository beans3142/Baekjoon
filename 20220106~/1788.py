fibo=[0,1]
for i in range(1000001):
    fibo.append((fibo[-1]+fibo[-2])%10**9)

n=int(input())
if n<0:
    if n%2==0:
        print(-1)
    else:
        print(1)
elif n==0:
    print(0)
else:
    print(1)
print(fibo[abs(n)])
