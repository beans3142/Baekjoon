def fib2(n):
    F = [0,1] + [0] * (n-1)
    print(F)
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]

for n in range(1,16):
    print(n,fib2(n))
    
