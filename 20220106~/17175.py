fibo=[1,1]
mod=10**9+7
for i in range(50):
    fibo.append((fibo[-1]+fibo[-2]+1)%mod)

print(fibo[int(input())])
