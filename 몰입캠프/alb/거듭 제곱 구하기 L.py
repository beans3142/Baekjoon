def fastpow(n,m):
    val=1
    a=n
    while m:
        if m&1:
            val=(val*a)%10007
        a=a**2%10007
        m>>=1
    return val
            
n,m=map(int,input().split())
print(fastpow(n,m))
