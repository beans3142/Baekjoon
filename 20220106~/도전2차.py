T=int(input())

for i in range(T):
    a,b=map(int,input().split())
    a=a%10
    if a==0:
        a=10
    b=b%4
    if b==0:
        b=4
    if a**b%10==0:
        print(10)
    else:
        print(a**b%10)
    
