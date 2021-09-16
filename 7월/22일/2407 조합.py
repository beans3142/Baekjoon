fac=[0,1]+[0]*(99)
for i in range(2,101):
    fac[i]=i*fac[i-1]


n,m=map(int,input().split())
print((fac[n]-fac[n-m])//fac[m])
