def fib(n):
    a=[0,1]+[0]*n
    if n<3:
        if n==2:
            print(1,1)
        elif n==1:
            print(0,1)
        else:
            print(1,0)
    else:
        for i in range(2,n+1):
            a[i]=a[i-1]+a[i-2]
        print(a[n-1],a[n])

for i in range(int(input())):
    fib(int(input()))
